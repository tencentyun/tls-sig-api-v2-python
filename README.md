## pip 集成
```shell
pip install tls-sig-api-v2
```

## 调用接口

``` python
import TLSSigAPI

api = TLSSigAPI.TLSSigAPI(1400000000, '5bd2850fff3ecb11d7c805251c51ee463a25727bddc2385f3fa8bfee1bb93b5e')
sig = api.gen_sig("xiaojun")
print(sig)
```
