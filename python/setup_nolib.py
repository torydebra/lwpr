from distutils.core import setup, Extension
from distutils.sysconfig import get_python_lib, parse_config_h
import os

lwprsources = ['lwprmodule.c', 
               '../src/lwpr.c', 
               '../src/lwpr_xml.c', 
               '../src/lwpr_math.c', 
               '../src/lwpr_binio.c', 
               '../src/lwpr_mem.c', 
               '../src/lwpr_aux.c']

# Try to find lwpr_config.h (either in source or build directory)
config_path = '../include/lwpr_config.h'
if not os.path.exists(config_path):
    config_path = '../build/lwpr_config.h'

configs = parse_config_h(open(config_path))

if 'HAVE_LIBEXPAT' in configs and configs['HAVE_LIBEXPAT']:
   module = Extension('lwpr', 
      include_dirs = ['../include', '../build', os.path.join(get_python_lib(),'numpy','core','include')],
      libraries = ['expat'],   
      sources = lwprsources)
else:
   module = Extension('lwpr',
      include_dirs = ['../include', '../build', os.path.join(get_python_lib(),'numpy','core','include')],
      sources = lwprsources)

setup (name = 'LWPR Module',
       version = '1.2.6',
       description = 'Python 3 wrapper around LWPR library',
       ext_modules = [module])
