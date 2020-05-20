image:
		sh -c "docker build . -t calculator-server:1.0.0"
deployment-grpc:
		sh -c "kubectl delete service calculator-server-dev-service-np || true"
		sh -c "kubectl delete deployment calculator-server-dev || true"
		sh -c "kubectl apply -f ./build/yamls/dev/configmap.yaml"
		sh -c "kubectl apply -f ./build/yamls/dev/deployment-grpc.yaml"
		sh -c "kubectl apply -f ./build/yamls/dev/service.yaml"
deployment-rest:
		sh -c "kubectl delete service calculator-server-dev-service-np || true"
		sh -c "kubectl delete deployment calculator-server-dev || true"
		sh -c "kubectl apply -f ./build/yamls/dev/configmap.yaml"
		sh -c "kubectl apply -f ./build/yamls/dev/deployment-rest.yaml"
		sh -c "kubectl apply -f ./build/yamls/dev/service.yaml"