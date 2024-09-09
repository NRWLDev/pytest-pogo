# Pytest plugin for Pogo migrate - asyncpg migration tooling
[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
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
