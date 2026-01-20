import contextlib
import sys

pytest_plugins = ("pytester",)


# Work-around known issue in pytest:
# https://github.com/pytest-dev/pytest/issues/935
# Related to pytest-cov loading after this plugin itself, producing an
# incomplete coverage report.
# Removing the plugin here ensures that it will be reloaded next time
# it's imported.
with contextlib.suppress(KeyError):
    del sys.modules["pytest_pogo"]
