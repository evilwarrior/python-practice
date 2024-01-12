urls = ['https://test.com/1234567890?f=test.jpg']

from aria2_rpc_client import DefaultClient
from aria2_rpc_client import DefaultConnection
from aria2_rpc_client import FileDownloadOptions

connection = DefaultConnection('nas.lan', '6800', '')
client = DefaultClient(connection)
for i, url in enumerate(urls):
    options = FileDownloadOptions()
    options.set_dir('/mnt/')
    options.set_filename('{:03}_{}'.format(i, url.split('?f=')[1]))
    options._options['all-proxy'] = '127.0.0.1:1080'
    options._options['split'] = '1'
    client.add_uri([url], options)
