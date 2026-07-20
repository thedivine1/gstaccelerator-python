import atexit
import sys
from setuptools import setup
from setuptools.command.install import install

class PostInstallCommand(install):
    """Post-installation for installation mode."""
    def run(self):
        install.run(self)
        def _post_install():
            print('\033[96m\n======================================================\033[0m')
            print('\033[96mThanks for installing GST Accelerator!\033[0m')
            print('Run your first lookup in seconds by getting a free API key at \033[94mhttps://gstaccelerator.in\033[0m')
            print('You can check the docs at \033[94mhttps://gstaccelerator.in/docs\033[0m')
            print('\033[96m======================================================\n\033[0m')
        
        atexit.register(_post_install)

setup(
    name="gstaccelerator",
    version="0.3.1",
    cmdclass={
        'install': PostInstallCommand,
    },
)
