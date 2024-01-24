import os, re

pid_re = r'^patreon - 51040771 - (\d+) - .*\.txt$'
link_re = r'(https?://(?:[\w_-]+(?:(?:\.[\w_-]+)+))(?:[\w.,@?^=%&:\/~+#-]*[\w@?^=%&\/~+#-]))'
root = r'./'
pairs = dict()
for file in os.listdir(root):
    pid = re.match(pid_re, file).group(1)
    with open(os.path.join(root, file), 'r', encoding='utf8') as _f:
        txt = _f.read()
    links = re.findall(link_re, txt)
    if not links:
        continue
    pairs[pid] = links

with open('out.txt', 'w', encoding='utf8') as _f:
    _f.write('\n'.join(map(lambda pair: '\n'.join((pair[0], *pair[1])), pairs.items())))
