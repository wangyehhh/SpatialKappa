from distutils.core import setup
import os
import shutil
VERSION = '2.1.1'
SKJAR_FILE = 'SpatialKappa-v' + VERSION + '.jar'
SKJAR_FILE_PATH = os.path.join('..', SKJAR_FILE)
ANTLRJAR_FILE = 'ant-antlr-3.2.jar'
ANTLRJAR_FILE_PATH = os.path.join('..', ANTLRJAR_FILE)
SHARE_DIR = 'SpatialKappa/share/SpatialKappa'
try:
    os.makedirs()
except:
    pass

shutil.copyfile(ANTLRJAR_FILE_PATH, os.path.join(SHARE_DIR, ANTLRJAR_FILE))
shutil.copyfile(SKJAR_FILE_PATH, os.path.join(SHARE_DIR, SKJAR_FILE))

setup(name='SpatialKappa',
      version=VERSION,
      packages=['SpatialKappa'],
      package_dir={'SpatialKappa': 'SpatialKappa'},
      package_data={'SpatialKappa': ['share/SpatialKappa/*']})

os.unlink(os.path.join(SHARE_DIR, ANTLRJAR_FILE))
os.unlink(os.path.join(SHARE_DIR, SKJAR_FILE))
