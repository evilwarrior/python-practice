import os, re

start_re = re.compile(r'^\[youtube\+AGB\] Extracting URL: (https://www\.youtube\.com/watch\?v=[-_0-9a-zA-Z]+)')
fin_re = re.compile(r'^\[download\] Downloading item \d+? of 225$')
endsentence = '[download] Finished downloading playlist: Xtremist - Videos')
last_line, last_url = '', ''
url_h_pair = dict()
recording = False

with open('formats.txt', 'r') as _f:
  lines = _f.readlines()

for line in lines:
  if recording:
    if line.strip() == endsentenc:
      url_h_pair[last_url] = int(last_line.split()[2].split('x')[1])
      break
    if re.match(fin_re, line):
      recording = False
      url_h_pair[last_url] = int(last_line.split()[2].split('x')[1])
      continue
    last_line = line
    continue
  start_at = re.match(start_re, line)
  if start_at:
    recording = True
    last_url = start_at.group(1)

_mp4_f = open('mp4.txt', 'a+')
_webm_f = open('webm.txt', 'a+')
for url, h in url_h_pair.items():
  if h > 1080:
    _webm_f.write(url+'\n')
  else:
    _mp4_f.write(url+'\n')
