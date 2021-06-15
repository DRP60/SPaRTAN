import pathlib
from setuptools import find_packages, setup
from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize
from numpy import get_include

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()


extensions = [
    Extension("PySPaRTAN/cythLeastR", ['PySPaRTAN/cythLeastR/cythLeastR.pyx', 'PySPaRTAN/cythLeastR/ep21R.c', 'PySPaRTAN/cythLeastR/epph.c'], include_dirs=['PySPaRTAN', 'PySPaRTAN/cythLeastR', get_include()]),
    Extension("PySPaRTAN/cythKronPlus", ["PySPaRTAN/cythKronPlus/cythKronPlus.pyx"]),
    ]

setup(
    
)
# This call to setup() does all the work
setup(
    name="PySPaRTAN",
    version="1.0.0",
    author="Xiaojun Ma",
    description="Single-cell Proteomic and RNA based Transcription factor Activity Network",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/osmanbeyoglulab/SPaRTAN/tree/main/SPaRTAN_python",
    author_email="xim33@pitt.edu",
    ext_modules=cythonize(extensions),
    # include_dirs=np.get_include(),
    license="MIT",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=find_packages(exclude=("tests",)),
    include_package_data=False,
    install_requires=[
          'Cython;platform_system=="Windows"',
          'pandas',
          'numpy', 
          'scipy',
          'scikit-learn',
          'matplotlib',
     ],
    setup_requires=['wheel'],	
)


# https://github.com/osmanbeyoglulab/PySPaRTAN/archive/refs/tags/0.1.tar.gz
# from distutils.core import setup
