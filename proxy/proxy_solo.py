#!/usr/bin/env python
#
#  ______                             _____  _                      _         _
#  | ___ \                           /  ___|| |                    | |       | |
#  | |_/ / _ __   ___  __  __ _   _  \ `--. | |_   __ _  _ __    __| |  __ _ | |  ___   _ __    ___
#  |  __/ | '__| / _ \ \ \/ /| | | |  `--. \| __| / _` || '_ \  / _` | / _` || | / _ \ | '_ \  / _ \
#  | |    | |   | (_) | >  < | |_| | /\__/ /| |_ | (_| || | | || (_| || (_| || || (_) || | | ||  __/
#  \_|    |_|    \___/ /_/\_\ \__, | \____/  \__| \__,_||_| |_| \__,_| \__,_||_| \___/ |_| |_| \___|
#                              __/ |
#                             |___/

import urllib.request
from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer
import urllib.request
import urllib.parse

headers = {}
headers ['user-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:71.0) Gecko/20100101 Firefox/71.0'

class GetHandler(BaseHTTPRequestHandler):
	def do_GET(self):
		parsed_path = urllib.parse.urlparse(self.path)
		req = urllib.request.Request(self.path, headers = headers)
		html = urllib.request.urlopen(req).read()

		self.send_response(200)
		self.end_headers()
		self.wfile.write(html)

if __name__ == '__main__':
	server = HTTPServer(('localhost', 8080), GetHandler)
	print('Starting proxy')
	server.serve_forever()


