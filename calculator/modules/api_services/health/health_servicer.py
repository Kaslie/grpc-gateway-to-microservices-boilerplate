from grpc_health.v1 import health_pb2_grpc, health_pb2
import grpc

# This servicer will be removed when the grpc_health.v1 package has been fixed,
# currently there's a bug that cause the health check always fail
class HealthServicerImpl(health_pb2_grpc.HealthServicer):
    def Check(self, request, context):
        status = request.service
        if status is None:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            return health_pb2.HealthCheckResponse()
        elif status != "SERVING":
            context.set_code(grpc.StatusCode.UNAVAILABLE)
            return health_pb2.HealthCheckResponse()

        return health_pb2.HealthCheckResponse(status=status)