from distutils.core import setup, Extension
import os

dir_file = os.path.join(os.path.dirname(__file__))

module = Extension(
    '_udt',
    sources=['udt_py.cxx'],
    include_dirs=[".", os.path.abspath(os.path.join(dir_file,
                                                    '..', 'udt4/src')), os.path.abspath(os.path.join(os.path.sep, 'usr', 'include', 'udt'))],
    libraries=['udt'],
    library_dirs=[os.path.abspath(os.path.join(dir_file,
                                               '..', 'udt4/src')), os.path.abspath(os.path.join(os.path.sep, 'usr', 'include', 'udt'))],
    extra_link_args=['-Wl,-R' + os.path.abspath(os.path.join(dir_file,
                                                '..', 'udt4/src')), os.path.abspath(os.path.join(os.path.sep, 'usr', 'include', 'udt')), 
                     '-lresolv']
)

setup(
    name='udt_py',
    version='1.0',
    description='Python bindings for UDT',
    ext_modules=[module],
    py_modules=['udt']
)
