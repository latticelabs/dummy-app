from setuptools import setup, find_packages

__version__ = '1.0.0'
setup(
    name='demoapp',
    version=__version__,
    description='Demo App for testing on the platform',
    author='Seven Bridges Genomics',
    author_email='kaushik.ghose@sbgenomics.com',
    py_modules=['dummy'],
    entry_points={
      'console_scripts': ['tool = demo_tool:cli', 'meta = demo_meta_analysis:cli']
    },
    install_requires=['click>=3.3'],
)