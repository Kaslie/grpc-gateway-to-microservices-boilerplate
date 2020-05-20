import grpc

from modules.api_services.calculate.calculate_interface import CalculateInterface
from modules.protos import calculate_pb2_grpc, calculate_pb2
from google.protobuf import json_format


class Calculate(CalculateInterface):
    def __init__(self, stub):
        self.stub = stub

    @classmethod
    def build(cls, dns, port):
        channel = grpc.insecure_channel('{}:{}'.format(dns, port))
        stub = calculate_pb2_grpc.CalculateStub(channel)

        return cls(stub)

    def health_check_request(self):
        health_check_request = calculate_pb2.HealthCheckRequest()
        response = self.stub.health_check(health_check_request)

        return json_format.MessageToDict(response, including_default_value_fields=True)

    def calculate_request(self, first_number: int, second_number: int):
        calculate_request = calculate_pb2.CalculateRequest(first_number=first_number, second_number=second_number)
        auth_credentials = grpc.access_token_call_credentials("Token auth")

        metadata = [("auth", "toEterdcken")]

        response = self.stub.calculate(calculate_request, credentials=auth_credentials, metadata=metadata)

        return json_format.MessageToDict(response, including_default_value_fields=True)