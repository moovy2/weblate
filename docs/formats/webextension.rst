.. _webex:

WebExtension JSON
-----------------

File format used when translating extensions for Mozilla Firefox or Google Chromium.

.. note::

   While this format is called JSON, its specification allows including
   "//"-style comments. Weblate does strip these comments while parsing the
   files and discards them when saving.

.. seealso::

    * :doc:`tt:formats/json`
    * `Google chrome.i18n <https://developer.chrome.com/docs/extensions/reference/api/i18n>`_
    * `Mozilla Extensions Internationalization <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/Internationalization>`_

Example file:

.. literalinclude:: ../../weblate/trans/tests/data/cs-webext.json
    :language: json

Weblate configuration
+++++++++++++++++++++

+-------------------------------------------------------------------+
| Typical Weblate :ref:`component`                                  |
+================================+==================================+
| File mask                      | ``_locales/*/messages.json``     |
+--------------------------------+----------------------------------+
| Monolingual base language file | ``_locales/en/messages.json``    |
+--------------------------------+----------------------------------+
| Template for new translations  | `Empty`                          |
+--------------------------------+----------------------------------+
| File format                    | `WebExtension JSON file`         |
+--------------------------------+----------------------------------+
