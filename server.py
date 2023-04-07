from http.server import HTTPServer, SimpleHTTPRequestHandler

PORT = 8000

handler = SimpleHTTPRequestHandler()

with HTTPServer(("", PORT), handler) as server:
    print(f"Serving at http://localhost:{PORT}")
    server.serve_forever()
