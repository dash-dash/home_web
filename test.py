import tornado.ioloop
import tornado.web

HAS_NEO = True

try:
    import neopixel as neo
except ImportError:
    HAS_NEO = False


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])


if __name__ == "__main__":

    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
    print('test')
