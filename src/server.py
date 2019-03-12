from flask import *
from flask.json import jsonify

class Server():
    
    def __init__(self, controller):
        self.controller = controller
        self.app = Flask(__name__, static_url_path='')
        self.app.add_url_rule('/', view_func=self.index, methods=['GET'])
        self.app.add_url_rule('/api/junctions', view_func=self.get_junctions, methods=['GET'])
        self.app.add_url_rule('/api/junction/<junction>/route', view_func=self.get_route, methods=['GET'])
        self.app.add_url_rule('/api/junction/<junction>/routes', view_func=self.get_routes, methods=['GET'])
        self.app.add_url_rule('/api/junction/<junction>/route', view_func=self.set_route, methods=['POST'])

    def index(self):
        return self.app.send_static_file('index.html')

    def get_junctions(self):
        return jsonify(self.controller.get_junctions())

    def get_route(self, junction):
        return jsonify(self.controller.get_route(junction))

    def get_routes(self, junction):
        return jsonify(self.controller.get_routes(junction))

    def set_route(self, junction):
        if not request.is_json:
            return abort(400)
        data = request.get_json()
        if 'route' not in data:
            return abort(400)
        self.controller.change_route(junction, data['route'])
        return jsonify({ 'response': 'ok '})

    def run(self, port):
        self.app.run('0.0.0.0', port)