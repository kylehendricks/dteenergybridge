===============
dteenergybridge
===============


.. image:: https://img.shields.io/pypi/v/dteenergybridge.svg
        :target: https://pypi.python.org/pypi/dteenergybridge

.. image:: https://img.shields.io/travis/kylehendricks/dteenergybridge.svg
        :target: https://travis-ci.org/kylehendricks/dteenergybridge


Library for retrieving data from a DTE Energy Bridge


* Free software: MIT license


Usage
--------

.. code-block:: python

    from dteenergybridge import DteEnergyBridge

    dte = DteEnergyBridge('192.168.1.1', 1)

    print(dte.get_current_energy_usage())

DTE Energy Bridge hardware versions
------------------------------------

There are currently two versions of the DTE Energy Bridge.

Version 1 looks like:
http://aemstatic-ww1.azureedge.net/content/dam/elp/print-articles/PGI/05/Powerly_EB.jpg

Version 2 looks like:
https://www.newlook.dteenergy.com/wps/wcm/connect/6e6840c4-11ae-4a91-ac93-45ec68d3560e/bridge-hero.jpg?MOD=AJPERES&CACHEID=6e6840c4-11ae-4a91-ac93-45ec68d3560e

Credits
---------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage

