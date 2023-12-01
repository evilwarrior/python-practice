import os, re
from json import loads
from pprint import pprint
from itertools import chain

sm_re  = re.compile(r'.*\[(sm\d+)\]\.info\.json$')
#url_re = re.compile(r"h ?t ?t ?p ?s? ?: ?/ ?/[ &%_\-~!\*'();:@&=\+$./\?#\[\]0-9a-zA-Z]+")
url_re = re.compile(r"https?://[&%_\-~!\*'();:@&=\+$./\?#\[\]0-9a-zA-Z]+")
ban = ['nicovideo.jp', 'youtu.be', 'youtube.com', 'deviantart.com', 'webry.info', 'blogspot.jp', 
       'bowlroll.net', 'bilibili.com', 'blog.shinobi.jp', 'pixiv.net', 'hdrlabs.com',
       'ninja-web.net', 'dip.jp', 'wikia.com', 'so-net.ne.jp', 'fc2.com', 'hackadoll.com',
       'imarine-project.jp', 'docs.google.com', 'mmdcup.org', 'github.com', 'koteri.com', 'ch2.cc',
       'free-texture.net', 'lolipop.jp', 'blender.rgr.jp', 'sites.google.com', 'sblo.jp',
       'patreon.com', 'baidu.com', 'spring-fragrance.mints.ne.jp', 'flickr.com', 'aokcub.net',
       'seesaa.net', 'kakegurui-anime.com', 'yukishigure.com', 'cgbookcase.com', 'xmedia-recode.de',
       'news.yahoo.co.jp', 'note.com', 'mrtska.net', 'piapro.jp']
allow = ['goo.gl', 'drive.google.com', 'onedrive.live.com', 'mediafire.com']
ban = ban + allow

url_colle = dict()
for json in os.listdir():
    sm = re.match(sm_re, json)
    if sm is None :
        continue
    sm = sm.group(1)
    with open(json, 'r', encoding='utf8') as _f:
        #desc = loads(_f.read())['_api_data']['video'].get('description')
        desc = loads(_f.read()).get('description')
    if desc is None:
        continue
    urls = []
    for line in desc.split('\n'):
        urls = urls + re.findall(url_re, line)
    url_colle[sm] = urls

#with open('tmp.txt', 'a+') as _f:
#    for sm, urls in url_colle.items():
#        _f.write(sm+'\n'+'\n'.join(urls)+'\n')

urls = list(filter(lambda url: any(map(lambda key: key in url, allow)), chain.from_iterable(url_colle.values())))
#urls = list(filter(lambda url: not any(map(lambda key: key in url, ban)), chain.from_iterable(url_colle.values())))

with open('tmp.txt', 'a+') as _f:
    _f.write('\n'.join(urls))
