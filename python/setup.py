from distutils.core import setup, Extension
from distutils.sysconfig import get_python_lib
import os

# Add the CMake build directory to find lwpr_config.h
build_dir = os.path.join(os.path.dirname(__file__), '..', 'build')
include_dirs = ['../include', build_dir,
                os.path.join(get_python_lib(),'numpy','core','include')]

module = Extension('lwpr',
                    include_dirs = include_dirs,
                    libraries = ['lwpr'],    
                    sources = ['lwprmodule.c'])

setup (name = 'LWPR Module',
       version = '1.2.6',
       description = 'Python 3 wrapper around LWPR library',
       ext_modules = [module])
