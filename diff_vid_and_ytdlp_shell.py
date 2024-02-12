import os, re
from pprint import pprint

vimeo_id_re = re.compile(r'.* \[(\d+)\]\.mp4$')
vimeo_set = set(map(lambda vid: re.match(vimeo_id_re, vid).group(1), filter(lambda file: re.match(vimeo_id_re, file), os.listdir())))

with open('b.sh', 'r') as _f:
    pre_vimeo_set = set(map(lambda cmd: cmd.split()[-1].split('/')[-1], _f.readlines()))

print(len(vimeo_set))
print(len(pre_vimeo_set))
pprint(pre_vimeo_set-vimeo_set)
