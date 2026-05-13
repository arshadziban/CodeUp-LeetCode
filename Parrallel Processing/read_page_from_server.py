import sys
import threading
import time
from http.server import HTTPServer, SimpleHTTPRequestHandler
import urllib.request
import urllib.error

SERVER_PORT = 8000
SERVER_HOST = 'localhost'
SERVER_URL = f"http://{SERVER_HOST}:{SERVER_PORT}/"


print(SERVER_URL)

class SimplePageHandler(SimpleHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)

        self.send_header('Content-type', 'text/html')
        self.end_headers()

        html_content = f"""
        <html>
            <head>
                <title>Welcome Page</title>
                <style>
                    body {{
                        font-family: Arial, sans-serif;
                        margin: 50px;
                        background-color: #f0f0f0;
                    }}
                    h1 {{
                        color: #333;
                    }}
                    p {{
                        font-size: 18px;
                    }}
                </style>
            </head>
            <body>
                <h1>Welcome to Simple Server!</h1>
                <p>This is a beginner-level web server example.</p>
                <p>Your request path was: {self.path}</p>
                <p>Server is running successfully!</p>
            </body>
        </html>
        """

        self.wfile.write(html_content.encode())

    def log_message(self, format, *args):
        pass


def start_server():
    server_address = ('', SERVER_PORT)
    httpd = HTTPServer(server_address, SimplePageHandler)
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.shutdown()


def read_page_from_server():
    try:
        response = urllib.request.urlopen(SERVER_URL)
        page_content = response.read().decode('utf-8')
    except urllib.error.URLError as e:
        print(f"Error: Could not connect to server - {e.reason}")
    except Exception as e:
        print(f"Error: {e}")


def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py [server|client|both]")
        return
    
    mode = sys.argv[1].lower()
    
    if mode == "server":
        start_server()
    elif mode == "client":
        read_page_from_server()
    elif mode == "both":
        server_thread = threading.Thread(target=start_server, daemon=False)
        server_thread.start()
        time.sleep(2)
        read_page_from_server()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            pass
    else:
        print(f"Error: Unknown mode '{mode}'")


if __name__ == "__main__":
    main()
