#! /usr/bin/python
# coding:utf-8


import hmac
import hashlib
import base64
import zlib
import json
import time


def base64_encode_url(data):
    """ base url encode 实现"""
    base64_data = base64.b64encode(data)
    base64_data_str = bytes.decode(base64_data)
    base64_data_str = base64_data_str.replace('+', '*')
    base64_data_str = base64_data_str.replace('/', '-')
    base64_data_str = base64_data_str.replace('=', '_')
    return base64_data_str


def base64_decode_url(base64_data):
    """ base url decode 实现"""
    base64_data_str = bytes.decode(base64_data)
    base64_data_str = base64_data_str.replace('*', '+')
    base64_data_str = base64_data_str.replace('-', '/')
    base64_data_str = base64_data_str.replace('_', '=')
    raw_data = base64.b64decode(base64_data_str)
    return raw_data


class TLSSigAPIv2:
    __sdkappid = 0
    __version = '2.0'
    __key = ""

    def __init__(self, sdkappid, key):
        self.__sdkappid = sdkappid
        self.__key = key

    def __hmacsha256(self, identifier, curr_time, expire, base64_userbuf=None):
        """ 通过固定串进行 hmac 然后 base64 得的 sig 字段的值"""
        raw_content_to_be_signed = "TLS.identifier:" + str(identifier) + "\n"\
                                   + "TLS.sdkappid:" + str(self.__sdkappid) + "\n"\
                                   + "TLS.time:" + str(curr_time) + "\n"\
                                   + "TLS.expire:" + str(expire) + "\n"
        if None != base64_userbuf:
            raw_content_to_be_signed += "TLS.userbuf:" + base64_userbuf + "\n"
        return base64.b64encode(hmac.new(self.__key.encode('utf-8'),
                                         raw_content_to_be_signed.encode('utf-8'),
                                         hashlib.sha256).digest())

    def __gen_sig(self, identifier, expire=180*86400, userbuf=None):
        """ 用户可以采用默认的有效期生成 sig """
        curr_time = int(time.time())
        m = dict()
        m["TLS.ver"] = self.__version
        m["TLS.identifier"] = str(identifier)
        m["TLS.sdkappid"] = int(self.__sdkappid)
        m["TLS.expire"] = int(expire)
        m["TLS.time"] = int(curr_time)
        base64_userbuf = None
        if None != userbuf:
            base64_userbuf = bytes.decode(base64.b64encode(userbuf))
            m["TLS.userbuf"] = base64_userbuf

        m["TLS.sig"] = bytes.decode(self.__hmacsha256(
            identifier, curr_time, expire, base64_userbuf))

        raw_sig = json.dumps(m)
        sig_cmpressed = zlib.compress(raw_sig.encode('utf-8'))
        base64_sig = base64_encode_url(sig_cmpressed)
        return base64_sig

    def gen_sig(self, identifier, expire=180*86400):
        """ 用户可以采用默认的有效期生成 sig """
        return self.__gen_sig(identifier, expire, None)

    def gen_sig_with_userbuf(self, identifier, expire, userbuf):
        """ 带 userbuf 生成签名 """
        return self.__gen_sig(identifier, expire, userbuf)


def main():
    api = TLSSigAPIv2(1400000000, '5bd2850fff3ecb11d7c805251c51ee463a25727bddc2385f3fa8bfee1bb93b5e')
    sig = api.gen_sig("xiaojun")
    print(sig)
    sig = api.gen_sig_with_userbuf("xiaojun", 86400*180, "abc".encode("utf-8"))
    print(sig)


if __name__ == "__main__":
    main()
