#!/usr/bin/env python

from setuptools import setup, find_packages

install_requires = [
    'gdax==1.0.6',
    'ConfigParser'
]

tests_require = [
    'pytest',
    ]

setup(
    name='icyhot_traderbot',
    version='1.0.0',
    author='mahae',
    author_email='mahaekoh@gmail.com',
    license='MIT',
    url='https://github.com/mahaekoh/icyhot-traderbot',
    packages=find_packages(),
    install_requires=install_requires,
    tests_require=tests_require,
    description='IcyHot Trader Bot',
    download_url='https://github.com/mahaekoh/icyhot-traderbot/archive/master.zip',
    keywords=['gdax', 'gdax-api', 'orderbook', 'trade', 'bitcoin', 'ethereum', 'BTC', 'ETH', 'client', 'api', 'wrapper', 'exchange', 'crypto', 'currency', 'trading', 'trading-api', 'coinbase'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Financial and Insurance Industry',
        'Intended Audience :: Information Technology',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
