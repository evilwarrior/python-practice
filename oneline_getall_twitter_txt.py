import os, re

print('\n'.join(filter(lambda txt: 'axfc' in txt, map(lambda file: '\n'.join((re.match(r'^SHIELD1001-(\d+)-.*\.txt$', file).group(1), open(file, 'r', encoding='utf8').read())), filter(lambda file: file != 'a.py', os.listdir())))))
print('\n'.join(filter(lambda txt: 'axfc' in txt, map(lambda file: '\n'.join((re.match(r'^asakota0-(\d+)-.*\.txt$', file).group(1), open(file, 'r', encoding='utf8').read())), filter(lambda file: file != 'a.py', os.listdir())))))
