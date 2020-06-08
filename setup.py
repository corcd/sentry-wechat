#!/usr/bin/env python
# coding: utf-8

#############################################
# File Name: setup.py
# Author: whzcorcd
# Mail: whzcorcd@gmail.com
# Created Time:  2020-06-08
#############################################

from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="sentry-wechat",
    version='0.0.2',
    author='whzcorcd',
    author_email='whzcorcd@gmail.com',
    url='https://github.com/corcd/sentry-wechat',
    description='A sentry extension which share information to Wechat Work',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT',
    keywords='sentry wechat',
    include_package_data=True,
    zip_safe=False,
    package_dir={'': 'src'},
    packages=find_packages('src'),
    install_requires=[
        'sentry>=9.0.0',
        'requests',
    ],
    entry_points={
        'sentry.plugins': [
            'sentry_wechat = sentry_wechat.plugin:WechatPlugin'
        ]
    },
    classifiers=[
        'Programming Language :: Python :: 2.7',
        "License :: OSI Approved :: MIT License",
    ]
)
