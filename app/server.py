import Queue
import threading
import time
import sys

import tornado.ioloop
import tornado.web
import tornado.websocket
from tornado import template
from pyjade.ext.tornado import patch_tornado

from newer_yahoo import FantasyApp
from app.session import session

patch_tornado()

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.jade')

class EchoWebSocket(tornado.websocket.WebSocketHandler):
    def open(self):
        print "WebSocket opened"
        self.running = True
        self.initial = True
        if self.initial:
            self.fantasy_app = FantasyApp()
            self.fantasy_app.startup()
        self.send_stats()
        self.thread = threading.Thread(target=self.ticker)
        self.thread.start()
        self.initial = False

    def on_message(self, message):
        pass
        # self.write_message(u"You said: " + message)

    def ticker(self):
        while self.running:
            time.sleep(4)
            self.update_stats()

    def update_stats(self):
        try:
            updates = self.fantasy_app.update_stats()
            if len(updates) > 0:
                self.send_stats(updates)
        except:
            print(sys.exc_info()[0])

    def send_stats(self, updates=[]):
        stats = {
            'data': []
        }
        for matchup in self.fantasy_app.matchups:
            stats['data'].append(matchup.serialize(self.initial))
        self.write_message(stats)

    def on_close(self):
        print "WebSocket closed"
        self.running = False

application = tornado.web.Application([
    (r"/", MainHandler),
    (r'/static/(.*)', tornado.web.StaticFileHandler, {'path': '.'}),
    (r"/stats", EchoWebSocket),
], debug=True)

if __name__ == "__main__":
    application.listen(8888)
    application.compiled_template_cache=False
    tornado.ioloop.IOLoop.instance().start()