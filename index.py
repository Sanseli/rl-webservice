import tornado.web
import tornado.ioloop
import json


class basicRequestHandler(tornado.web.RequestHandler):
    def get(self):
        grid = self.get_argument('grid')
        print(grid)
        self.write(json.dumps([
                {"configuration": [[2, 0], [1, 3]], "action": "Left"},
                {"configuration": [[2, 3], [0, 1]], "action": "Right"},
                {"configuration": [[3, 1], [0, 2]], "action": "Up"},
                {"configuration": [[2, 3], [1, 0]], "action": "Up"},
                {"configuration": [[3, 0], [2, 1]], "action": "Down"},
                {"configuration": [[0, 1], [3, 2]], "action": "Right"},
                {"configuration": [[1, 2], [3, 0]], "action": "Down"},
                {"configuration": [[1, 0], [3, 2]], "action": "Down"},
                {"configuration": [[3, 1], [2, 0]], "action": "Left"},
                {"configuration": [[1, 2], [0, 3]], "action": "Right"},
                {"configuration": [[0, 2], [1, 3]], "action": "Down"},
                {"configuration": [[0, 3], [2, 1]], "action": "Down"}
        ]))
        self.set_header("Access-Control-Allow-Origin", "*")

    def options(self):
            self.set_status(204)
            self.finish()


if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/solve", basicRequestHandler)
    ])

    app.listen(8881)
    print("im listening on port 8881")
    tornado.ioloop.IOLoop.current().start()
