from setuptools import setup, find_packages

setup(

    name = 'fpastebin',
    version = '0.0.1,',
    description='A tool to upload text to http://paste.fedoraproject.org/',
    url = 'http://github.com/surajssd/fpastebin',
    author = 'Suraj Deshmukh',
    author_email = 'surajssd009005@gmail.com',

    license = 'MIT',

    packages = ['fpastebin'],
    install_requires = ['requests']
)
