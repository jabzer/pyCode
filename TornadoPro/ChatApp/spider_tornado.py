#!/usr/bin/python3
import time
from datetime import timedelta

from html.parser import HTMLParser
from urllib.parse import urljoin,urldefrag

from tornado import httpclient,gen,ioloop,queues

#base_url = 'http://tornado-zh.readthedocs.io/zh/latest/'
base_url = 'http://www.piaov.com/'
concurrency = 10

@gen.coroutine
def get_links_from_url(url):
    try:
        response = yield httpclient.AsyncHTTPClient().fetch(url)
        print('fetched %s'%url)
        html = response.body if isinstance(response.body,str) else response.body.decode()
        urls = [urljoin(url,remove_fragment(new_url)) for new_url in get_links(html)]
    except Exception as e :
        print('Exception : %s %s' %(e,url))
        raise gen.Return([])
    raise gen.Return(urls)

def remove_fragment(url):
    pure_url,frag = urldefrag(url)
    return pure_url

def get_links(html):
    class URLSeeker(HTMLParser):
        def __init__(self):
            HTMLParser.__init__(self)
            self.urls=[]
        def handle_starttag(self, tag, attrs):
            href = dict(attrs).get('href')
            if href and tag =='a':
                self.urls.append(href)

    url_seeker = URLSeeker()
    url_seeker.feed(html)
    return url_seeker.urls

@gen.coroutine
def main():
    q = queues.Queue()
    start = time.time()
    fetching,fetched = set(),set()
    @gen.coroutine
    def fetch_url():
        current_url = yield q.get()
        try:
            if current_url in fetching:
                return
            print('fetching %s' % current_url)
            fetching.add(current_url)
            urls = yield get_links_from_url(current_url)
            fetched.add(current_url)

            for new_url in urls:
                if new_url.startswith(base_url):
                    yield q.put(new_url)
        finally:
            q.task_done()
    @gen.coroutine
    def worker():
        while True:
            yield fetch_url()

    q.put(base_url)

    for _ in range(concurrency):
        worker()
    yield q.join(timeout=timedelta(seconds=300))
    assert fetching ==fetched
    print('Done in %s seconds,fetched %s Urls.'% (time.time()-start,len(fetched)))

if __name__ == '__main__':
    import logging
    logging.basicConfig()
    io_loop = ioloop.IOLoop.current()
    io_loop.run_sync(main)