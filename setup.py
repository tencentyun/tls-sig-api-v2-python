from setuptools import setup, find_packages

setup (
        name='tls-sig-api-v2',
        version='1.0',
        packages=find_packages(),
        author_email='weijunyi@tencent.com',
        py_modules=[
            'TLSSigAPI'
            ],
        url='https://github.com/tencentyun/tls-sig-api-v2-python',
        license='MIT'
        )
