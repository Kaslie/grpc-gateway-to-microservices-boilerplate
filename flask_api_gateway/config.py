import os


class Config(object):
    HOST = os.getenv('HOST', '0.0.0.0')
    PORT = os.getenv('PORT', '5001')

    CALCULATOR_HOST = os.getenv('CALCULATOR_HOST', '0.0.0.0')
    CALCULATOR_PORT = os.getenv("CALCULATOR_PORT", "5010")
    # Switching between GRPC / REST
    CALCULATOR_COMMUNICATION_TYPE = os.getenv("CALCULATOR_COMMUNICATION_TYPE", "GRPC")

