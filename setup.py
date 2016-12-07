from setuptools import setup, find_packages

print find_packages()
setup(name='python_utils',
    version='0.0.1',
    description='common functions i find myself writing over and over',
    author='lynzt',
    url='https://github.com/lynzt/python_utils',
    packages=['utils'],
    )
