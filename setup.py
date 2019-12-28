from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(

    name='buptgw',  

    version='0.0.2',  

    description='login to gw.bupt.edu.cn to access the Internet',  

    long_description=long_description, 
    long_description_content_type='text/markdown',  

    url='https://github.com/sxwxs/buptGateway',  

    author='sxwxs',  

    author_email='sxwxs@msn.com',  

    classifiers=[
        'Development Status :: 4 - Beta',

        'Intended Audience :: End Users/Desktop',
        'Topic :: Utilities',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],

    keywords='bupt network gateway login',

    package_dir={'': 'src'},

    packages=find_packages(where='src'),

    python_requires='>=3.5',

    install_requires=['requests'], 

    entry_points={  
        'console_scripts': [
            'buptgw=buptgw:main',
        ],
    },

    project_urls={ 
        'Bug Reports': 'https://github.com/sxwxs/buptGateway/issues',
        'Funding': 'https://i.loli.net/2019/12/28/pv8PUd4eKGyNDiV.png',
        # 'Say Thanks!': '',
        'Source': 'https://github.com/sxwxs/buptGateway',
    },
)