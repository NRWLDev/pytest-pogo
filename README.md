# Pytest plugin for Pogo migrate - asyncpg migration tooling
[![image](https://img.shields.io/pypi/v/pytest-pogo.svg)](https://pypi.org/project/pytest-pogo/)
[![image](https://img.shields.io/pypi/l/pytest-pogo.svg)](https://pypi.org/project/pytest-pogo/)
[![image](https://img.shields.io/pypi/pyversions/pytest-pogo.svg)](https://pypi.org/project/pytest-pogo/)
![style](https://github.com/NRWLDev/pytest-pogo/actions/workflows/style.yml/badge.svg)
![tests](https://github.com/NRWLDev/pytest-pogo/actions/workflows/tests.yml/badge.svg)
[![codecov](https://codecov.io/gh/NRWLDev/pytest-pogo/branch/main/graph/badge.svg)](https://codecov.io/gh/NRWLDev/pytest-pogo)


Provides `pogo_engine` fixture which will apply local migrations at the start
of the test session, and roll them back at the end.

Additionally `pytest-pogo` honours pytests `-v/--verbose` flags to increase log
verbosity, if migrations don't appear to be applying correctly, this will
capture more verbose logs.
