# 是打包程序配置文件，需要设置一些选项。此外，setup.cfg是包含setup.py额外配置信息的文件，我没有用到这其中的设置，所以本项目中其是空的。

from setuptools import setup, find_packages

setup(
    name = 'group-signature',
    version = '0.1.0',
    keywords='CS97 cryptology group-signature MIT',
    description = 'This is a python library that implements the CS97 solution for group signature.',
    license = 'MIT License',
    url = '',
    author = 'YeYiChen',
    author_email = '20151733@hdu.edu.cn',
    packages = find_packages(),
    include_package_data = True,
    platforms = 'any',
    install_requires = [],
)