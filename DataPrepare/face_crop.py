#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# (c) 2016 chenbingfeng
#

def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application(), ssl_options={
           "certfile": os.path.join(os.path.abspath("."), "certificate.pem"),
           "keyfile": os.path.join(os.path.abspath("."), "server.key.unsecure"),
       })
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()
