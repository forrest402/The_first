import base64
import codecs
import math
import random
from Crypto.Cipher import AES

def random_str(length):
    string = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    i = 0
    random_strs = ""
    while i<length:
        e = random.random() * len(string)
        e = math.floor(e)
        random_strs = random_strs +list(string)[e]
        i += 1
    return random_strs
def get_AES(msg, key):
    padding = 16 -len(msg) % 16
    msg = msg+padding * chr(padding)
    iv = '0102030405060708'
    iv = iv.encode("utf-8")
    key = key.encode("utf-8")
    msg = msg.encode("utf-8")
    ciper = AES.new(key, AES.MODE_CBC, iv)
    encry = ciper.encrypt(msg)
    encodestrs = base64.b64encode(encry)
    entexts = encodestrs.decode("utf-8")
    return entexts
def get_RSA(random_strs, key, f):
    string = random_strs[::-1]
    text = bytes(string, "utf-8")
    seckey = int(codecs.encode(text, encoding="hex"), 16)** int(key, 16) % int(f, 16)
    return format(seckey, "x").zfill(256)
def get_params(page):
    offset = str((page - 1) * 20)
    msg = '{"offset":' + str(offset) + ',"total":"True","limit":"20","csrf_token":""}'
    key = '0CoJUm6Qyw8W8jud'
    f = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
    e = '010001'
    enctext = get_AES(msg, key)
    i = random_str(16)
    encText = get_AES(enctext, i)
    encSecKey = get_RSA(i, e, f)
    return encText, encSecKey
get_params(4)
