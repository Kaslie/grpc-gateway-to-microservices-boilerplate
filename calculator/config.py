import os


class Config(object):
    HOST = os.getenv('HOST', '0.0.0.0')
    PORT = os.getenv("PORT", "5010")
    COMMUNICATION_TYPE = os.getenv("COMMUNICATION_TYPE", "GRPC") # Switch between GRPC or REST
    GRPC_MAX_WORKERS = os.getenv('GRPC_MAX_WORKERS', 2)

