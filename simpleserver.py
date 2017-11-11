import http.server

server_address = ("", 8000)
handler_calss = http.server.CGIHTTPRequestHandler
simple_server = http.server.HTTPServer(server_address, handler_calss)
simple_server.serve_forever()
