image:
		sh -c "docker build . -t flask-api-gateway:1.0.0"
deployment:
		sh -c "kubectl delete service flask-api-gateway-dev-service-np || true"
		sh -c "kubectl delete deployment flask-api-gateway-dev || true"
		sh -c "kubectl apply -f ./build/yamls/dev/configmap.yaml"
		sh -c "kubectl apply -f ./build/yamls/dev/deployment.yaml"
		sh -c "kubectl apply -f ./build/yamls/dev/service.yaml"
		sh -c "kubectl apply -f ./build/yamls/dev/ingress.yaml"