# -*- coding: utf-8 -*-
import re, sys, logging, requests
from bs4 import BeautifulSoup


def _log():
    logging.basicConfig(level=logging.DEBUG,
                        filename='v2ex.log',
                        format='[%(levelname)s] : [%(asctime)s] : %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S'
                        )
    handler = logging.StreamHandler()
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter('[%(levelname)s] : [%(asctime)s] : %(message)s')
    handler.setFormatter(formatter)
    logging.getLogger('').addHandler(handler)
    return logging



if __name__ == '__main__':
    pass

