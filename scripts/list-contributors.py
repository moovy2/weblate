#!/usr/bin/env python3

# Copyright © Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: GPL-3.0-or-later

import argparse
from collections import defaultdict
from pathlib import Path
from typing import Literal

from git import Commit, Repo
from git.diff import Diff

import weblate.utils.version

VERSION = weblate.utils.version.VERSION_BASE
ROOT_DIR = Path(__file__).parent.parent

CategoryType = Literal["code", "translations", "docs"]

IGNORE_AUTHORS: set[str] = {"GitHub", "Anonymous", "Hosted Weblate"}

CATEGORIES: dict[CategoryType, str] = {
    "code": "Code contributions",
    "translations": "Translations contributions",
    "docs": "Documentation contributions",
}

TEMPLATE = """
{label}
    .. only:: not gettext

       {contributors}"""


def get_file_category(filename: str) -> CategoryType:
    if filename.endswith((".po", ".pot")):
        return "translations"
    if filename.endswith(".rst") or filename.startswith("docs/"):
        return "docs"
    return "code"


def get_diff_categories(diff: list[Diff]) -> set[CategoryType]:
    categories = set()
    for item in diff:
        if item.a_path:
            categories.add(get_file_category(item.a_path))
        if item.b_path:
            categories.add(get_file_category(item.b_path))

    return categories


def is_valid_author(author: str) -> bool:
    return (
        "(bot)" not in author
        and "[bot]" not in author
        and "add-on" not in author
        and author not in IGNORE_AUTHORS
    )


def get_commit_authors(commit: Commit) -> set[str]:
    authors: list[str] = [str(commit.author)]
    if commit.committer:
        authors.append(str(commit.committer))
    authors.extend(
        line[15:].split("<")[0].strip()
        for line in str(commit.message).splitlines()
        if line.lower().startswith("co-authored-by:")
    )
    return {author for author in authors if is_valid_author(author)}


def get_contributors() -> dict[CategoryType, list[str]]:
    contributors: dict[CategoryType, list[str]] = defaultdict(list)
    repo = Repo.init(ROOT_DIR)
    tags = sorted(repo.tags, key=lambda tag: tag.commit.committed_date)
    recent_tag = tags[-1]
    commits = list(repo.iter_commits(f"{recent_tag}..HEAD"))
    previous = recent_tag.object.object
    for commit in reversed(commits):
        authors = get_commit_authors(commit)
        if authors:
            diff = previous.diff(commit.tree)
            for category in get_diff_categories(diff):
                for author in authors:
                    if author not in contributors[category]:
                        contributors[category].append(author)
        previous = commit.tree
    return contributors


def get_contributors_text() -> str:
    all_contributors = get_contributors()
    output = []

    for category, label in CATEGORIES.items():
        contributors = all_contributors[category]
        if contributors:
            output.append(
                TEMPLATE.format(label=label, contributors=", ".join(contributors))
            )

    return "\n".join(output)


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="list-contributors.py",
        description="Lists contributors in a repository since last tag",
    )
    parser.add_argument(
        "-u", "--update", action="store_true", help="Updates docs/changes.rst"
    )

    args = parser.parse_args()

    text = get_contributors_text()
    if args.update:
        changelog_file = (
            ROOT_DIR / "docs" / "changes" / "contributors" / f"{VERSION}.rst"
        )
        changelog_file.write_text(f"{text}\n")
    else:
        print(text)


if __name__ == "__main__":
    main()
