import os
import platform
from setuptools import setup
from setuptools.command.build import build


class UnsupportedPython(RuntimeError):
    pass


class BuildCommand(build):
    def run(self):
        if os.getenv('DISABLE_UNSUPPORTED_PYTHON', None) is None:
            raise UnsupportedPython('One or more of your installed packages '
                                    'have indicated that they do not support '
                                    'your version of Python ('
                                    + platform.python_version() + ')')
        return super().run()


setup(cmdclass={'build': BuildCommand})
