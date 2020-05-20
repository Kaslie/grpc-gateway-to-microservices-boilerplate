from flask import Blueprint, request, jsonify

from modules.api_services.calculate.calculate_grpc import Calculate as CalculateGRPCGateway
from modules.api_services.calculate.calculate_rest import Calculate as CalculateRESTGateway

from config import Config

class CalculatorBlueprint(object):
    @classmethod
    def build(cls):
        blueprint = Blueprint(cls.__name__, __name__)
        dns = Config.CALCULATOR_HOST
        port = Config.CALCULATOR_PORT

        calculate_service = CalculateGRPCGateway.build(dns, port) \
            if Config.CALCULATOR_COMMUNICATION_TYPE == "GRPC" \
            else CalculateRESTGateway.build(dns, port)

        @blueprint.route('/calculate/health', methods=["GET"])
        def health_check():
            response = calculate_service.health_check_request()

            return response

        @blueprint.route('/calculate', methods=["GET"])
        def calculate():
            first_number = request.args.get('first_number')
            second_number = request.args.get('second_number')

            if first_number is None and second_number is None:
                return jsonify({ "messages": "No first_number and second_number arguments specified"})

            response = calculate_service.calculate_request(int(first_number), int(second_number))

            return response

        return blueprint
