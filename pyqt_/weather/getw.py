#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys, requests


def getw(city='101010100'):
    rep = requests.get('http://www.weather.com.cn/data/sk/{0}.html'.format(city))
    rep.encoding = 'utf-8'
    print('返回结果:%s' % rep.json())
    return rep.json()


def transCityName(cityName):
    cityCode=''
    city={'北京':'101010100','上海':'101020100','东莞':'101281601','广州':'101280101'}
    try:
        cityCode=city[cityName]
    except:
        print('没找到这城市')
    return cityCode

if __name__ == '__main__':
    cityName = '广州'
    json = getw(transCityName(cityName))
    print('城市:%s' % json['weatherinfo']['city'])
