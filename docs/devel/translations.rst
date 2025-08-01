Managing translations
=====================

.. _adding-strings:

Adding new strings
------------------

New strings can be made available for translation when they appear in the base file,
called :ref:`component-new_base` (see :ref:`component`).
If your file format doesn't require such a file, as is the case with most monolingual
translation flows, you can start with empty files.

Weblate can add new strings to existing files for most of the file formats. You
can also specify :guilabel:`Context` for bilingual formats to distinguish same
strings used in different context. :guilabel:`Auto-adjust context when an
identical string already exists.` can be used to automatically adjust
:guilabel:`Context` by adding a numeric suffix in case such a string already
exist in the translation.

.. seealso::

   :ref:`format-context`

.. _adding-translation:

Adding new translations
-----------------------

New languages can be added right away when requested by a user in Weblate, or a
notification will be sent to project admins for approval and manual addition.
This can be done using :ref:`component-new_lang` in :ref:`component`.

Some formats expect to start with an empty file and only translated strings to
be included (for example :ref:`aresource`), while others expect to have all
keys present (for example :ref:`gettext`). The document-based formats (for
example :ref:`odf`) start with a copy of the source document and all strings
marked as needing editing. In some situations this really doesn't depend on
the format, but rather on the framework you use to handle the translation (for
example with :ref:`json`).

When you specify :ref:`component-new_base` in :ref:`component`, Weblate uses
this file to start new translations. Any existing translations is
removed from the file when doing so.

When :ref:`component-new_base` is empty and the file format
supports it, an empty file is created where new strings are added once they are
translated.

The :ref:`component-language_code_style` allows you to customize language code
used in generated filenames. Additionally, any mappings defined in
:ref:`project-language_aliases` are applied in reverse.

.. seealso::

   * :ref:`component-new_lang`
   * :ref:`component-new_base`
   * :ref:`component-language_code_style`
   * :ref:`language-code`
   * :ref:`project-language_aliases`
   * :ref:`language-parsing-codes`

.. note::

    If you add a language file in connected remote repository, respective
    translation is added to the component when Weblate updates local repository.

    More info on the repository update settings can be found on the :ref:`update-vcs`.

.. _removing-translation:

Removing existing translations
------------------------------

Languages, components, or the projects they are in, can be removed (deleted from Weblate
and remote repository if used) from the menu :guilabel:`Operations` ↓ :guilabel:`Removal`
of each project, component, or language.

Initiating the :guilabel:`Removal` action shows the list of components to be removed.
You have to enter the object's `slug` to confirm the removal. The `slug` is the
project's, language's, or component's pathname as it can be seen in the URL.

If you want to remove just some specific strings, there are following ways:

- Manually in the source file. They will be removed from the
  translation project as well upon Weblate's repository update.

.. versionadded:: 4.5

- In Weblate’s UI via button :guilabel:`Operations` ↓ :guilabel:`Remove` while editing the string.
  This has differences between file formats, see: :ref:`component-manage_units`

.. note::

     If you delete a language file in connected remote repository, respective
     translation will be removed from the component when Weblate updates local repository.

     More info on the repository update settings can be found on the :ref:`update-vcs`.


.. _variants:

String variants
---------------

Variants are useful to group several strings together so that translators can
see all variants of the string at one place.

.. hint::

      Abbreviations (shortened forms, contractions) are a good example of variants.

Automated key based variants
++++++++++++++++++++++++++++

You can define regular expression to group the strings based on the key of
monolingual translations in the :ref:`component`:

.. image:: /screenshots/variants-settings.webp

In case the :guilabel:`Key` matches the expression, the matching part is
removed to generate root key of the variant. Then all the strings with the same
root key become part of a single variant group, also including the string with
the key exactly matching the root key.

The following table lists some usage examples:

+---------------------------+-------------------------------+-----------------------------------------------+
| Use case                  | Regular expression variant    | Matched translation keys                      |
+===========================+===============================+===============================================+
| Suffix identification     | ``(Short|Min)$``              | ``monthShort``, ``monthMin``, ``month``       |
+---------------------------+-------------------------------+-----------------------------------------------+
| Inline identification     | ``#[SML]``                    | ``dial#S.key``, ``dial#M.key``, ``dial.key``  |
+---------------------------+-------------------------------+-----------------------------------------------+

Manual variants
+++++++++++++++

.. versionadded:: 4.5

You can manually link specific strings using ``variant:SOURCE`` flag. This can
be useful for bilingual translations which do not have keys to group strings
automatically, or to group strings which keys are not matching, but
should be considered together when translating.

The additional variant for a string can also be added using the :guilabel:`Tools` while translating
(when :ref:`component-manage_units` is turned on):

.. image:: /screenshots/glossary-tools.webp

.. note::

   The variant source string has to be at most 768 characters long. This is a
   technical limitation due to compatibility with MySQL database.

.. seealso::

   * :ref:`custom-checks`
   * :ref:`glossary-variants`

Variants while translating
++++++++++++++++++++++++++

The variant is later grouped when translating:

.. image:: /screenshots/variants-translate.webp

.. _labels:

String labels
-------------

Split component translation strings into categories by text and colour in the project configuration.

.. image:: /screenshots/labels.webp

.. hint::

    Labels can be assigned to units in :ref:`additional` by bulk editing, or using the :ref:`addon-weblate.flags.bulk` add-on.
