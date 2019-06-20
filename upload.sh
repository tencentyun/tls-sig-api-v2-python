#! /bin/sh

rm -rf dist

python setup.py sdist

# 需要确保 twine 已经安装，如果没有安装，安装命令如下
# pip install twine

# 在 ~/ 目录下建立 .pypirc，内如如下
# [distutils]
# index-servers = pypi
# 
# [pypi]
# username:你的PyPi用户名
# password:你的PyPi密码

twine upload dist/*.tar.gz

