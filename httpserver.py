#! /usr/bin/env python

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SocketServer
import json
import random

class MyHttpServer(BaseHTTPRequestHandler):

   def _set_headers(self):
      self.send_response(200)
      self.send_header('Content-type', 'text/html')
      self.end_headers()

   def do_GET(self):
      self._set_headers()
      f = open("index.html", "r")
      self.wfile.write(f.read())

   def do_HEAD(self):
      self._set_headers()

   def do_POST(self):
      self._set_headers()
      self.data_string = self.rfile.read(int(self.headers['Content-Length']))

      self.send_response(200)
      self.end_headers()

      data = json.loads(self.data_string)
      print data
      #data = simplejson.loads(self.data_string)
      #print "{}".format(data)
      return

def run(server_class=HTTPServer, handler_class=MyHttpServer, port=80):
   server_address = ('', port)
   httpd = server_class(server_address, handler_class)
   print 'Starting thread...'
   httpd.serve_forever()

if __name__ == "__main__":
   from sys import argv
   if len(argv) == 2:
      run(port=int(argv[1]))
   else:
      run()