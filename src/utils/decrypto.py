import base64
import json
from Crypto.Cipher import DES


def des_decrypto(key, data):
    """
    对data进行des解密

    :param key: 密钥
    :param data: 待解密数据
    :return: 解密后数据
    """
    crypter = DES.new(key.encode(), DES.MODE_ECB)
    s = base64.b64decode(data)
    return json.loads(crypter.decrypt(s).decode().replace("\x04", ""))
