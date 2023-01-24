from setuptools import setup
from Cython.Build import cythonize

setup(
    name='Hello world app',
    ext_modules=cythonize("bench_ext.pyx", language_level=3),
    zip_safe=False,
)