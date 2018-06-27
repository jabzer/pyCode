#!/usr/bin/python3
import re
import uuid
import subprocess,os
import requests


HEADERS = {
    'cookie':'_zap=65073f3c-81cb-498d-8f94-210d66ed23a4; z_c0=Mi4xeG1nT0FBQUFBQUFBTUNBOEo3ZDlEUmNBQUFCaEFsVk45VFRNV3dEVnFsUVhVcjNPYUduTjQ0a1RrdVhJVkFLOW13|1524557557|3996ad6f3d6dd3b45f31747e0a28d0ca681de0a3; d_c0="AFDg3y7siA2PTi5yTiff1p7M6abTHUxaPV4=|1525307018"; q_c1=65f53053bf0645229a6bf451d57ad9a2|1527554855000|1524557551000; __utma=51854390.1305797009.1529811468.1529811468.1529811468.1; __utmz=51854390.1529811468.1.1.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/people/jiang-niao-mu/collections; __utmv=51854390.100-1|2=registration_date=20130611=1^3=entry_date=20130611=1; tgw_l7_route=29b95235203ffc15742abb84032d7e75; _xsrf=b3ffc6ef-7b58-4b67-8470-26a86467476f',
    'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36',
}

QUALITY = 'ld' # 支持是 'ld' 'sd' 'hd' 分别是低清、中清、高清

def get_video_ids_from_url(url):
    html = requests.get(url,headers = HEADERS).text
    video_ids =   re.findall(r'data-lens-id="(\d+)"', html)
    if video_ids:
        return set([int(video_id) for video_id in video_ids])
    return []

def yield_video_m3u8_url_from_video_ids(video_ids):
    for video_id in video_ids:
        api_video_url =  'https://lens.zhihu.com/api/videos/{}'.format(int(video_id))
        r = requests.get(api_video_url,headers = HEADERS)
        playlist = r.json()['playlist']
        m3u8_url = playlist[QUALITY]['play_url']
        yield m3u8_url

def download(url):
    print('get video_ids')
    video_ids = get_video_ids_from_url(url)
    print('get m3u8_list')
    m3u8_list = list(yield_video_m3u8_url_from_video_ids(video_ids))
    filename = '{}.mp4'.format(uuid.uuid4())
    for idx,m3u8_url in enumerate(m3u8_list):
        print('下载 : {}'.format(m3u8_url))
        print(filename.format(str(idx)))
        #subprocess.call(['ffmpeg','-i',m3u8_url,filename.format(str(idx))])
        os.system("ffmpeg -i {0} {1}".format(m3u8_url,filename.format(str(idx))))


if __name__ == '__main__':
    url = 'https://zhuanlan.zhihu.com/p/38541232'
    download(url)

