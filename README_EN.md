## Note
This project is the python implementation of tls-sig-api-v2. Previous asymmetric keys cannot use APIs of this version. To enable them to use APIs of this version,[see here](https://github.com/tencentyun/tls-sig-api-python)。

## integration
It can be integrated using pip or source code.

### pip
```shell
pip install tls-sig-api-v2
```

### source code
Just download the file `TLSSigAPIv2.py` to the local.

## use

``` python
import TLSSigAPIv2

api = TLSSigAPIv2.TLSSigAPIv2(1400000000, '5bd2850fff3ecb11d7c805251c51ee463a25727bddc2385f3fa8bfee1bb93b5e')
sig = api.gen_sig("xiaojun")
print(sig)
```
