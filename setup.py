from setuptools import setup, find_packages

__version__ = '1.0.0'
setup(
    name='dummy-app',
    version=__version__,
    description='Dummy App',
    author='Seven Bridges Genomics',
    author_email='kaushik.ghose@sbgenomics.com',
    py_modules=['dummy'],
    entry_points={
      'console_scripts': ['dummy = dummy:cli']
    },
    install_requires=['click>=3.3'],
)