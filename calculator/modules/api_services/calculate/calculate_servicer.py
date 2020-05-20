from modules.protos import calculate_pb2_grpc, calculate_pb2
from modules.services.calculator import Calculator

from modules.api_services.calculate.calculate_interface import CalculateInterface


class CalculatorServicerImpl(calculate_pb2_grpc.CalculateServicer, CalculateInterface):
    def health_check(self, request, context):
        print("[GET] GRPC call {}.{} function".format(self.__class__.__name__, self.health_check.__name__))

        return calculate_pb2.HealthCheckReply()

    def calculate(self, request, context):
        print("[GET] GRPC call {}.{} function".format(self.__class__.__name__, self.calculate.__name__))
        first_number = request.first_number
        second_number = request.second_number

        if first_number is None and second_number is None:
            # Error Handling here
            pass

        # Using Business Logic

        add_result = Calculator.add(first_number, second_number) or 0
        multiply_result = Calculator.multiply(first_number, second_number) or 0
        division_result = Calculator.division(first_number, second_number) or 0
        subtract_result = Calculator.subtract(first_number, second_number) or 0

        result = calculate_pb2.CalculateReply().Result(
            add=add_result,
            multiply=multiply_result,
            division=division_result,
            subtract=subtract_result)

        return calculate_pb2.CalculateReply(result=result)