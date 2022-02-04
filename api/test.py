from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    self.wfile.write('hello world')

  def translate_post(self):
    try:
      length = int(self.headers['content-length'])
    except TypeError:
      return None
    data = self.rfile.read(length)
    return data
  
  def do_POST(self):
    self.send_response(200)
    self.send_header('Content-type','text/html')
    self.end_headers()
    data = self.translate_post()
    self.wfile.write(data)
