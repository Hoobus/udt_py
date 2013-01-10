from distutils.core import setup, Extension

from os.path import join

module = Extension(
    '_udt',
    sources = ['udt_py.cxx'],
    include_dirs = [".", "../udt4/src"],
    libraries = ['udt'],
    library_dirs = ['../udt4/src'],
    extra_link_args = ['-Wl,-R../udt4/src/', '-lresolv'],
)

setup (
    name = 'udt_py',
    version = '1.0',
    description = 'Python bindings for UDT',
    ext_modules = [module]
)
