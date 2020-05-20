# grpc-gateway-to-microservices-boilerplate

****
### My Machine specification:
* MacBook Pro (13-inch, 2017, Two Thunderbolt 3 ports)
* Processor: 2,3 GHz Dual-Core Intel Core i5
* Memory: 8 GB 2133 MHz LPDDR3
****
### Requirements:
* Programming Language: [Python 3](https://realpython.com/installing-python/)
* Framework: [Flask](https://flask.palletsprojects.com/en/1.1.x/)
* Deployment: [Learn Kubernetes Minikube](https://kubernetes.io/docs/setup/learning-environment/minikube/) / [Docker](https://docs.docker.com/get-started/)
* isolated environment: [virtualenv](https://pypi.org/project/virtualenv/)
* Support: REST API / [GRPC](https://grpc.io/)
****

### How to start:
Before you start to build the apps, make sure you have install all required package by run `python3 -m pip install -r requirements.txt` at each directory (`grpc_protos`, `flask_api_gateway` , `{your_service_name_dir}`)

Example: `service_name` is `payment`
1. Define Proto
    1. Define your proto at `grpc_protos` folder
    1. Generate your protos with `make proto`
    1. Checking your `client/modules/protos` and `server/modules/protos` directory, should have new proto definition
2. Define Your Service
    1. Define your business logic at `/modules/services`
    2. Define the interface or edit the interface before you create the **blueprint** or **servicers** at `modules/api_services/payment`.
    3. create the **servicer** class for GRPC and **blueprint** class for REST at `modules/api_services/payment`.
    4. In the **servicer** / **blueprint** file, remember to inherit the **interface** that you defined. and add additional **Flask's Blueprint** class to your own blueprint class.
    5. You will have to inherit the function that you defined at the interface, call your business logic inside the function.
    6. Register Blueprint or Servicer to Adapter
        * [GRPC] Register your **servicer** at `/modules/adapters/grpc_connection_adapter`.
        * [REST API] Register your blueprint at `/modules/adapters/rest_connection_adapter`.
3. Add the service's endpoint to your `api-gateway`
    1. define `payment_grpc`, `payment_interface` and `payment_rest` with your need at `modules/api_services/payment` 
    2. Add new blueprint for the new service that you have created with the endpoint for user to access.
    
    
****
### How to run:
1. change to each dir and run `pip install -r requirements.txt`
2. Check the `config.py` file and change as you need
3. If the calculator service's communication type is `GRPC`, Your service must use `GRPC` also. or it will fail.
4. After each service is running, just send the request through your `api-gateway`.
****
### How to deploy:
1. change current dir to `calculator` and `flask_api_gateway`
2. Run `make image`
3. Run `make deployment` on `flask_api_gateway` directory
4. Run `make deployment-grpc` or `make deployment-rest` on `calculator` directory

****
Note: 
This is not the best approach to enable your service support REST and GRPC. There's a new tools
called [grpc-gateway](https://github.com/grpc-ecosystem/grpc-gateway) that enable reverse-proxy between REST and GRPC.
I haven't research the tools yet. So I don't know whether it support `python`. 
****
### Additional Resources:
- [Set minikube ingress](https://kubernetes.io/docs/tasks/access-application-cluster/ingress-minikube/)

