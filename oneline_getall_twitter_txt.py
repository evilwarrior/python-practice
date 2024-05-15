import os, re, itertools
print('\n'.join(filter(lambda txt: 'axfc' in txt, map(lambda file: '\n'.join((re.match(r'^SHIELD1001-(\d+)-.*\.txt$', file).group(1), open(file, 'r', encoding='utf8').read())), filter(lambda file: file != 'a.py', os.listdir())))))
print('\n'.join(itertools.chain.from_iterable(filter(lambda pair: 'axfc' in pair[1].lower(), map(lambda file: (file.split('-')[1], open(file, 'r', encoding='utf8').read().lower()), filter(lambda file: file != 'a.py', os.listdir()))))))
