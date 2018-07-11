#!/usr/bin/python3
#-*- coding:utf-8 –*-
from urllib import request
from bs4 import BeautifulSoup
import re
import os
import time

def getDownloadUrl(url):
    print(url)
    req = request.Request(url)
    #req.add_header("User-Agent","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36")
    req.add_header("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36")
    resp = request.urlopen(req).read().decode("gbk")
    soup=BeautifulSoup(resp,"html.parser")
    listUrl=soup.findAll("a",href=re.compile("://"))
    for url in listUrl:
        if 'http://' not in url["href"]:
            #print(url["href"]+"----------"+url.string)
            print(url["href"])

if __name__ == "__main__":
    url='http://www.hao6v.com/dlz/2018-07-10/31469.html'
    K2url='http://www.6vhao.com/rj/2016-09-24/27839.html'
    Westworldurl='http://www.6vhao.com/mj/2016-10-03/27892.html'
    getDownloadUrl(url)