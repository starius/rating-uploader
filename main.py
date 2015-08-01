import BaseHTTPServer
import urlparse

import config
import worksheet
import rating

HOST_NAME = config.HOST_NAME
PORT_NUMBER = config.PORT_NUMBER

# based on https://wiki.python.org/moin/BaseHttpServer

global wsk

class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_GET(self):
        """Respond to a GET request."""
        path, query = self.path.split('?', 1)
        qs = urlparse.parse_qs(query)
        login = qs['login'][0]
        task = qs['task'][0]
        rating1 = qs['rating'][0]
        password = qs['password'][0]
        assert password == config.password # protection
        print('Rating %s %s %s' % (login, task, rating1))
        rating.update_rating(wks, login, task, rating1)
        print('Rating updated')
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write("Ok")

if __name__ == '__main__':
    wks = worksheet.get_worksheet()
    print('Connected to Google Sheets')
    server_class = BaseHTTPServer.HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
