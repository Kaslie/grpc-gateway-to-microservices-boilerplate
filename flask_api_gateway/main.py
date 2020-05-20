from flask import Flask, jsonify
from modules.blueprints.calculator_blueprint import CalculatorBlueprint
from config import Config

app = Flask(__name__)


@app.route('/')
def health():
    return jsonify({ "message": "OK"})

app.register_blueprint(CalculatorBlueprint.build())

if __name__ == "__main__":
    app.run(host=Config.HOST, port=Config.PORT, debug=False)