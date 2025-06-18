from http.server import HTTPServer, BaseHTTPRequestHandler

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"Merhaba Dunya!")

with HTTPServer(('', 8000), Handler) as httpd:
    print("sunucu baslatildi, port 8000")
    httpd.serve_forever()
  
