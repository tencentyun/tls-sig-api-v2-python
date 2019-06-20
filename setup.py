# coding: utf-8
from setuptools import setup, find_packages

setup (
        name = 'tls-sig-api-v2',
        version = '1.1',
        description ='tls-sig-api-v2 适用于腾讯云通信生成用户账号签名。',
        long_description = "适用于新版 key，之前非对称密钥不适用，使用非对称密钥参考 https://github.com/tencentyun/tls-sig-api-python",
        author = 'weijunyi',
        author_email = 'weijunyi@tencent.com',
        license = 'MIT Licence',
        packages = find_packages(),
        py_modules = [
            'TLSSigAPIv2'
            ],
        install_requires = [],
        url = 'https://github.com/tencentyun/tls-sig-api-v2-python',
        platforms = "any"
        )
