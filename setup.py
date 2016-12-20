from setuptools import setup, find_packages

setup(name='python_utils',
    version='0.0.3',
    description='common functions i find myself writing over and over',
    author='lynzt',
    url='https://github.com/lynzt/python_utils',
    packages=['utils'],
    install_requires=[
        'awesome-slugify',
        'unidecode',
        'freezegun',
        'requests',
    ],
)
