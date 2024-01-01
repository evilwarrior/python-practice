 import os, re

pair_re = re.compile(r':lengthi(\d+?)e4:pathl(?:4|10):(.*?)ee(?:d6|e4)')

with open(r'MMD_SamOne_2023-10.torrent', 'rb') as _f:
    torrent_content = _f.read()
    torrent_content = torrent_content[:torrent_content.find(b'name20')]
    torrent_content = torrent_content.decode()

torrent_pair = dict(map(lambda pair: (pair[0][7:], pair[1]), filter(lambda pair: '2023' in pair[0] and '.mp4' in pair[0], map(lambda pair: (pair[1], int(pair[0])), re.findall(pair_re, torrent_content)))))

from pprint import pprint

root_path = r'Y:\520-Douga\521-MMD\SamOneOne (SamOne)\Samone\2023'
files_pair = dict()
for root, dirs, files in os.walk(root_path):
    if not files:
        continue
    files_pair.update(dict(filter(lambda pair: '.mp4' in pair[0], map(lambda file: (file, os.stat(os.path.join(root, file)).st_size), files))))

for ex in set(set(torrent_pair.items()) - set(files_pair.items())):
    print(ex)
