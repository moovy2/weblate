Weblate frontend
================

The frontend is currently built using Bootstrap, jQuery and few third-party libraries.

Supported browsers
------------------

Weblate supports the latest, stable releases of all major browsers and
platforms.

Alternative browsers which use the latest version of WebKit, Blink, or Gecko,
whether directly or via the platform’s web view API, are not explicitly
supported. However, Weblate should (in most cases) display and function
correctly in these browsers as well.

Older browsers might work, but some features might be limited.

Dependency management
---------------------

Installing and managing `3rd party` libraries in the `client` of a Django project
can be a bit tricky. This section provides a step-by-step guide on how to install
and manage 3rd party libraries used by the `client side` of Weblate using `Webpack`.

Prerequisites
+++++++++++++

Before proceeding with an installation, make sure you have the following prerequisites:

- ``Nodejs`` version 14 or higher.
- The ``yarn`` package manager is installed on your system.
- Run ``cd client``.
- Run ``yarn install``.

Installation
++++++++++++

To install a library, first run the following command:

.. code-block:: bash

    yarn add <lib-name>

Importing the Library
+++++++++++++++++++++

Then, there are two ways to import the library:

1. If it is a project-wide library (it is used/needed in all/most pages):
    - Import the library in ``src/main.js``.
    - And declare it in the global scope (if needed).

2. If it is page-specific library (library is used in a specific page or template):
    - Create a new file named ``src/<lib-name>.js``.
    - Import the library in it. Then inject it into the ``window`` object to be globally accessible.
    - Add an entry in ``webpack.config.js``:
      ``<lib-name>: "src/<lib-name>.js"``.
    - Add library name in ``excludePrefixes`` array in ``mainLicenseTransform`` in ``webpack.config.js``.
    - Add license file name in ``additionalFiles`` in ``LicensePlugin`` in ``plugins`` array in ``webpack.config.js``.
    - Create a ``<lib-name>LicenseTransform`` function for the license file introduced in the previous steps and use it.

   Note: Replace ``<lib-name>`` with the actual name of the 3rd party library.

Building the Library
++++++++++++++++++++

Build the libraries used by the project, by running the following command:

.. code-block:: bash

    yarn build

Including the Library
+++++++++++++++++++++

Now the library is built and ready for use. To include it follow these steps:

1. If the library was imported in ``src/main.js``, no further steps are required (as it is already included in ``base.html``).

2. If the library was imported in its specific file ``src/<lib-name>.js``, in ``weblate/templates`` use the include tags to link to the built static JavaScript file:

.. code-block:: django

    {% load static %}
    <script src="{% static 'js/vendor/<lib-name>.js' %}"></script>

Coding style
------------

Weblate relies on `Biome`_ for formatting and linting the JavaScript and CSS code.

.. _Biome: https://biomejs.dev/


Localization
------------

Should you need any user visible text in the frontend code, it should be
localizable. In most cases, all you need is to wrap your text inside ``gettext``
function, but there are more complex features available:

.. code-block:: javascript

    document.write(gettext('this is to be translated'));

    var object_count = 1 // or 0, or 2, or 3, ...
    s = ngettext('literal for the singular case',
            'literal for the plural case', object_count);

    fmts = ngettext('There is %s object. Remaining: %s',
            'There are %s objects. Remaining: %s', 11);
    s = interpolate(fmts, [11, 20]);
    // s is 'There are 11 objects. Remaining: 20'

.. seealso::

   :doc:`Translation topic in the Django documentation <django:topics/i18n/translation>`

Icons
-----

Weblate currently uses `Material Design Icons`_, in case you are looking for new
symbol, check that.

Additionally, there is :file:`scripts/optimize-svg` to reduce size of the SVG
as most of the icons are embedded inside the HTML to allow styling of the
paths.

.. _Material Design Icons: https://pictogrammers.com/library/mdi/
