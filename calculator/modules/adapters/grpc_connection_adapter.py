import grpc
from concurrent import futures

from modules.protos import calculate_pb2, calculate_pb2_grpc

from modules.api_services.calculate.calculate_servicer import CalculatorServicerImpl
from modules.api_services.health.health_servicer import HealthServicerImpl

from grpc_health.v1 import health_pb2_grpc

from config import Config


class GRPCConnectionAdapter(object):
    def __init__(self):
        print("MAX WORKER: {}".format(Config.GRPC_MAX_WORKERS))
        self.app = grpc.server(futures.ThreadPoolExecutor(max_workers=int(Config.GRPC_MAX_WORKERS)))
        self.app.add_insecure_port('{}:{}'.format(Config.HOST, Config.PORT))
        self.register_services()

    def register_services(self):
        calculate_pb2_grpc.add_CalculateServicer_to_server(CalculatorServicerImpl(), self.app)
        health_pb2_grpc.add_HealthServicer_to_server(HealthServicerImpl(), self.app)

    def run(self):
        self.app.start()
        print("GRPC Server is running at {}:{}".format(Config.HOST, Config.PORT))
        self.app.wait_for_termination()