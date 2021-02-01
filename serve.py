# Copyright 2018 Google LLC

# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import SimpleHTTPServer
import SocketServer
import time

PORT = 8093

def main():

    class Handler(SimpleHTTPServer.SimpleHTTPRequestHandler):
        pass
    Handler.extensions_map['.js'] = 'application/javascript'
    # Without the correct MIME type, async compilation doesn't work
    Handler.extensions_map['.wasm'] = 'application/wasm'

    httpd = SocketServer.TCPServer(("", PORT), Handler)

    httpd.serve_forever()

if __name__ == '__main__':
    while True:
        try:
            main()
        except BaseException:
            print('except!')
        else:
            print('error!')
        time.sleep(2)
       


