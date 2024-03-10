# Pytest plugin for Pogo migrate - asyncpg migration tooling
[![image](https://img.shields.io/pypi/v/pytest-migrate.svg)](https://pypi.org/project/pytest-migrate/)
[![image](https://img.shields.io/pypi/l/pytest-migrate.svg)](https://pypi.org/project/pytest-migrate/)
[![image](https://img.shields.io/pypi/pyversions/pytest-migrate.svg)](https://pypi.org/project/pytest-migrate/)
![style](https://github.com/NRWLDev/pytest-pogo/actions/workflows/style.yml/badge.svg)
![tests](https://github.com/NRWLDev/pytest-pogo/actions/workflows/tests.yml/badge.svg)
[![codecov](https://codecov.io/gh/NRWLDev/pytest-pogo/branch/main/graph/badge.svg)](https://codecov.io/gh/NRWLDev/pytest-pogo)


Provides `pogo_engine` fixture which will apply local migrations at the start
of the test session, and roll them back at the end.
