## 说明
此项目为 tls-sig-api-v2 版本的 python 实现。之前非对称的秘钥无法使用此版本的 api，如果有需要请查看[这里](https://github.com/tencentyun/tls-sig-api-python)。

## 集成
使用 pip 或者源码方式都可以集成。

### pip
```shell
pip install tls-sig-api-v2
```

### 源码
直接将文件 `TLSSigAPIv2.py` 下载到本地即可。

## 使用

``` python
import TLSSigAPIv2

api = TLSSigAPIv2.TLSSigAPIv2(1400000000, '5bd2850fff3ecb11d7c805251c51ee463a25727bddc2385f3fa8bfee1bb93b5e')
sig = api.gen_sig("xiaojun")
print(sig)
```
