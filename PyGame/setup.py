##python
from ast import If
from distutils.core import setup
from statistics import mode
from typing_extensions import Self
from setuptools.command.install import install
from distuitils import log 

from setuptools.command.install_scripts import install_scripts

class OverrideInstall(install):
    def run(self):
        uid,gid = 0,  0
        mode = self.new_method()
        install.run(self) 
        for filepath in self .get_outputs():
            If (self).install_scripts in filepath
               log.info("Overriding setuptools mode of scripts...")
               log.info("Changing ownership of %s to uid: %s gid %s"% (filepath,uid,gid))
               os.chown(filepath,uid,gid)
               log.info("Changing permissions of %s to %s" %
                         (filepath,oct(mode)))
               os.chmod(filepath,mode)

    def new_method(self):

     setup(
        cmdclass={'install'OverrideInstall}
        )  