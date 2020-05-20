from flask import Blueprint, jsonify, request

from modules.services.calculator import Calculator
from modules.api_services.calculate.calculate_interface import CalculateInterface


class CalculatorBlueprint(Blueprint, CalculateInterface):
    def health_check(self):
        return jsonify({ 'message': 'ok'})

    def calculate(self):
        a = int(request.args.get('first_number') or 0)
        b = int(request.args.get('second_number') or 0)

        # Using Business Logic

        result = {
            "add": Calculator.add(a, b),
            "multiply": Calculator.multiply(a, b),
            "division": Calculator.division(a, b),
            "subtract": Calculator.subtract(a, b)
        }

        return jsonify({ "result": result })

    @classmethod
    def build(cls):
        blueprint = cls(cls.__name__, __name__)
        blueprint.route('/health', methods=["GET"])(blueprint.health_check)
        blueprint.route('/calculate', methods=["GET"])(blueprint.calculate)

        return blueprint
