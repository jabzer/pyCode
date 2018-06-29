#!/usr/bin/python3
import sys, base64

###基础算法
#base64加密
def encryptBase64(str):
    str = bytes(str,encoding='utf8')
    str2 = base64.encodestring(str)
    return str2.decode()

#base64解密
def decryptBase64(str):
    str = bytes(str, encoding='utf8')
    str2 = base64.decodestring(str)
    return str2.decode()


##实际应用
#迅雷地址转ed2k
def thunderToed2k(tlink):
    if tlink[:10]!='thunder://':
        print('链接不是迅雷地址')
    else:
        link = tlink.replace('thunder://','')
        ed2k = decryptBase64(link)
        return ed2k[2:-2]


if __name__ == '__main__':
    s = 'QUFlZDJrOi8vfGZpbGV8JTVCJUU5JUEzJTk4ViVFNyVCRCU5MXBpYW92LmNvbSU1RCVFNiVCNyVCMSVFNSVBRSVBQiVFOCVBRSVBMSU1QiVFNyVCMiVBNCVFOCVBRiVBRCU1RDIzLm1wNHwzNjEwMTA3NTZ8QzA2MEQxQTUwMjk4Q0RGMThBREQwOEZCMTg2RjdDMjN8aD0yRE5DRFhQQUE1RlBRNENKVEtZTlJMUVJRS0NBUUNCS3wvWlo='
    print(decryptBase64(s))
    tlink = 'thunder://QUFlZDJrOi8vfGZpbGV8JWUzJTgwJTkwbG9sJWU3JTk0JWI1JWU1JWJkJWIxJWU1JWE0JWE5JWU1JWEwJTgyd3d3LmxvbGR5dHQuY29tJWUzJTgwJTkxJUU2JTg4JTkxJUU3JTlGJUE1JUU1JUE1JUIzJUU0JUJBJUJBJUU1JUJGJTgzLkJEMTI4MCVFOCVCNiU4NSVFNiVCOCU4NSVFNSU5QiVCRCVFNyVCMiVBNCVFNSU4RiU4QyVFOCVBRiVBRCVFNCVCOCVBRCVFNSVBRCU5Ny5tcDR8MjY2NzEwMzYxMHxFRkJERDAxOEEyNDNENjk1NDUzRTg5RkRCQzI4Qzg0RHxoPVozTUhZNFJBV1hRN09PTkJQM0Y2T1dMQklRS0pIVEwyfC9aWg=='

    print(thunderToed2k(tlink))