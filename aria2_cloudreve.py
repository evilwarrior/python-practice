import requests, json
from aria2_rpc_client import DefaultClient
from aria2_rpc_client import DefaultConnection
from aria2_rpc_client import FileDownloadOptions

api_url = 'https://<domain>/api/v3/share/'
headers = {
    'Cookie': 'cloudreve-session=<cloudreve-session>',
    'User-Agent': '<user-agent>'
}
proxies = {
    'http': '<http_proxy>',
    'https': '<http_proxy>',
    'ftp': '<http_proxy>'
}

conn = DefaultConnection("<aria2_server>", "6800", "<token>")
client = DefaultClient(conn)
options = FileDownloadOptions()

for year in range(2019, 2025):
    res = requests.get(f'{api_url}list/G5t2%2F{year}', headers=headers, proxies=proxies)
    files = map(lambda item: item['name'], json.loads(res.content.decode())['data']['objects'])
    for file in files:
        res = requests.put(f'{api_url}download/G5t2?path=/{year}/{file}', headers=headers, proxies=proxies)
        src = json.loads(res.content.decode())['data']
        options.set_dir(f'/mnt/{year}')
        options.set_filename(f'{file}')
        options._options['split'] = '8'
        client.add_uri([src], options)
