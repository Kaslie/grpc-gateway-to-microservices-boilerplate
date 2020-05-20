from flask import Flask

from modules.api_services.calculate.calculate_blueprint import CalculatorBlueprint
from config import Config


class RESTConnectionAdapter(object):
    def __init__(self):
        self.app = Flask(__name__)
        self.register_blueprints()

    def register_blueprints(self):
        calculator_blueprint = CalculatorBlueprint.build()

        self.app.register_blueprint(calculator_blueprint)

    def run(self, environ=None, start_response=None):
        print("REST API Server is running at {}:{}".format(Config.HOST, Config.PORT))
        if environ is not None and start_response is not None:
            self.app(environ, start_response)
        else:
            self.app.run(host=Config.HOST, port=Config.PORT, debug=False)
