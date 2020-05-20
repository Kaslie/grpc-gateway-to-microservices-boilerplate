from config import Config

from modules.adapters.connection_adapter import ConnectionAdapter
from modules.adapters.grpc_connection_adapter import GRPCConnectionAdapter
from modules.adapters.rest_connection_adapter import RESTConnectionAdapter

print("Application has started to build with {} workers".format(Config.GRPC_MAX_WORKERS))

connectionAdapterType = GRPCConnectionAdapter() \
    if Config.COMMUNICATION_TYPE == "GRPC" \
    else RESTConnectionAdapter()

app = ConnectionAdapter(connectionAdapterType)

print("Adapter Connected with {} Communication Type".format(Config.COMMUNICATION_TYPE))

def main(environ=None, start_response=None):
    if __name__ == "__main__":
        app.run()
    else:
        app.run(environ=environ, start_response=start_response)

    print("Application is running")

if __name__ == "__main__":
    main()