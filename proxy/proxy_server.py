#!/usr/bin/env python
#
#  ______                             _____
#  | ___ \                           /  ___|
#  | |_/ / _ __   ___  __  __ _   _  \ `--.   ___  _ __ __   __  ___  _ __
#  |  __/ | '__| / _ \ \ \/ /| | | |  `--. \ / _ \| '__|\ \ / / / _ \| '__|
#  | |    | |   | (_) | >  < | |_| | /\__/ /|  __/| |    \ V / |  __/| |
#  \_|    |_|    \___/ /_/\_\ \__, | \____/  \___||_|     \_/   \___||_|
#                              __/ |
#                             |___/

from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer
import urllib.request
import urllib.parse

headers = {}
headers ['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:71.0) Gecko/20100101 Firefox/71.0'


class GetHandler(BaseHTTPRequestHandler):
	def do_GET(self):
		URL = self.path[1:]
		print(URL)
		req = urllib.request.Request(URL, headers = headers)
		with urllib.request.urlopen(req) as response:
			the_page = response.read()
		self.send_response(200)
		self.end_headers()
		self.wfile.write(the_page)

if __name__ == '__main__':
	server = HTTPServer(('', 80), GetHandler)
	server.serve_forever()

