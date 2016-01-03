import BaseHTTPServer, SimpleHTTPServer, ssl, os

# configuration
site_path = '_site'
pem_path = '_server.pem'
port = 443

httpd = BaseHTTPServer.HTTPServer(('localhost', port), SimpleHTTPServer.SimpleHTTPRequestHandler)
httpd.socket = ssl.wrap_socket (httpd.socket, certfile=pem_path, server_side=True)
os.chdir(site_path)
httpd.serve_forever()