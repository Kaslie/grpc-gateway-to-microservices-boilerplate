proto:
		sh -c "python3 -m grpc_tools.protoc -I . --python_out=../calculator --grpc_python_out=../calculator ./modules/protos/*.proto"
		sh -c "python3 -m grpc_tools.protoc -I . --python_out=../flask_api_gateway --grpc_python_out=../flask_api_gateway ./modules/protos/*.proto"