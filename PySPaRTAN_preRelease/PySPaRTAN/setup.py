from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize
from numpy import get_include

extensions = [
    Extension("cythLeastR", ['cythLeastR/cythLeastR.pyx', 'cythLeastR/ep21R.c', 'cythLeastR/epph.c'], include_dirs=['.', 'cythLeastR', get_include()]),
    Extension("cythKronPlus", ["cythKronPlus/cythKronPlus.pyx"]),
    ]

setup(
    ext_modules=cythonize(extensions),
)

# from distutils.core import setup
# from distutils.extension import Extension
# from numpy import get_include

# extensions = [
    # Extension("cythLeastR", ['cythLeastR/cythLeastR.c'], include_dirs=['.', 'cythLeastR', get_include()]),
    # Extension("cythKronPlus", ["cythKronPlus/cythKronPlus.c"]),
    # ] 
# setup(
    # ext_modules = extensions
# )
# try:
    # from Cython.Distutils import build_ext
# except ImportError:
    # use_cython = False
# else:
    # use_cython = True

# cmdclass = {}
# ext_modules = []

# if use_cython:
    # ext_modules = [
        # Extension("cythLeastR", ['cythLeastR/cythLeastR.pyx', 'cythLeastR/ep21R.c', 'cythLeastR/epph.c'], include_dirs=['.', 'cythLeastR', get_include()]),
        # Extension("cythKronPlus", ["cythKronPlus/cythKronPlus.pyx"]),
    # ] 
    # cmdclass.update({'build_ext': build_ext})
# else:
    # ext_modules = [
        # Extension("cythLeastR", ['cythLeastR/cythLeastR.c'], include_dirs=['.', 'cythLeastR', get_include()]),
        # Extension("cythKronPlus", ["cythKronPlus/cythKronPlus.c"]),
    # ]

# setup(
    # cmdclass=cmdclass,
    # ext_modules=ext_modules,
# )