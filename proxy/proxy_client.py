#!/usr/bin/env python
#
#  ______                             _____  _  _               _
#  | ___ \                           /  __ \| |(_)             | |
#  | |_/ / _ __   ___  __  __ _   _  | /  \/| | _   ___  _ __  | |_
#  |  __/ | '__| / _ \ \ \/ /| | | | | |    | || | / _ \| '_ \ | __|
#  | |    | |   | (_) | >  < | |_| | | \__/\| || ||  __/| | | || |_
#  \_|    |_|    \___/ /_/\_\ \__, |  \____/|_||_| \___||_| |_| \__|
#                              __/ |
#                             |___/

from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer
import urllib.request
import urllib.parse

headers = {}
headers ['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:71.0) Gecko/20100101 Firefox/71.0'

# IP Proxy SQUID
proxy = {'http': '142.93.230.147'}

class GetHandler(BaseHTTPRequestHandler):
	def do_GET(self):
		parsed_path = self.path

		# Requete vers serveur proxy python
		req = urllib.request.Request('http://149.91.81.60/'+parsed_path, headers = headers)

		# Proxy SQUID
		handler = urllib.request.ProxyHandler(proxy)
		opener = urllib.request.build_opener(handler)
		urllib.request.install_opener(opener)

		with urllib.request.urlopen(req) as response:
			the_page = response.read()

		self.send_response(200)
		self.end_headers()
		self.wfile.write(the_page)


if __name__ == '__main__':
	server = HTTPServer(('localhost', 8123), GetHandler)
	server.serve_forever()


