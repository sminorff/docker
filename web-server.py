import tornado.ioloop
import tornado.web
import socket

class MainHandler(tornado.web.RequestHandler) :
	def get(self):
		self.write("Hostname: " + socket.gethostname())

def make_app(self):
	return tornado.web.Application([(r"/", MainHandler), ])

if __name__ == "_main_":
	app = make_app()
	app.listen(8888)
	tornado.ioloop.IOLoop.current().start()
