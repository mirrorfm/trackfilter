========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis|
        | |codecov|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|
.. |docs| image:: https://readthedocs.org/projects/trackfilter/badge/?style=flat
    :target: https://readthedocs.org/projects/trackfilter
    :alt: Documentation Status

.. |travis| image:: https://api.travis-ci.org/mirrorfm/trackfilter.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/mirrorfm/trackfilter

.. |codecov| image:: https://codecov.io/github/mirrorfm/trackfilter/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/mirrorfm/trackfilter

.. |version| image:: https://img.shields.io/pypi/v/trackfilter.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/trackfilter

.. |wheel| image:: https://img.shields.io/pypi/wheel/trackfilter.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/trackfilter

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/trackfilter.svg
    :alt: Supported versions
    :target: https://pypi.org/project/trackfilter

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/trackfilter.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/trackfilter

.. |commits-since| image:: https://img.shields.io/github/commits-since/mirrorfm/trackfilter/v1.0.0.svg
    :alt: Commits since latest release
    :target: https://github.com/mirrorfm/trackfilter/compare/v1.0.0...master



.. end-badges

Remove YouTube-related garbage from song titles.

* Free software: MIT license

Installation
============

::

    pip install trackfilter

You can also install the in-development version with::

    pip install https://github.com/mirrorfm/trackfilter/archive/master.zip


Documentation
=============

https://trackfilter.readthedocs.io/


Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
