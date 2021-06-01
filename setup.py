from setuptools import setup, find_packages

setup(name='python_utils',
    version='0.0.5',
    description='common functions i find myself writing over and over',
    author='lynzt',
    url='https://github.com/lynzt/python_utils',
    packages=['utils'],
    install_requires=[
        'awesome-slugify==1.6.5',
        'beautifulsoup4==4.6.0',
        'certifi==2017.11.5',
        'chardet==3.0.4',
        'freezegun==0.3.9',
        'html5lib==0.999999999',
        'idna==2.6',
        'lxml==4.1.1',
        'python-dateutil==2.6.1',
        'regex==2017.11.9',
        'requests==2.18.4',
        'six==1.11.0',
        'Unidecode==0.4.21',
        'urllib3==1.26.5',
        'webencodings==0.5.1',
    ],
)
