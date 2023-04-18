
unsupported-python
==================

This package can be used as a conditional dependency to indicate lack of
support for particular versions of Python.

```toml
[project]
name = "my-test-package"
version = "1.0.0"
dependencies = [
    # package does not work on Python 3.11 and beyond
    "unsupported-python; python_version>='3.11'",
]
```

Installing a package which depends on `unsupported-python` will fail with an
error message, without going back to earlier versions of said package.
