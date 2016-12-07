from setuptools import setup, find_packages

print find_packages()
setup(name='python_read_file_generator',
    version='0.0.1',
    description='read a file | convert row/list values to dict',
    author='lynzt',
    url='https://github.com/lynzt/python_read_file_generator',
    packages=['read_file_generator'],
    )
