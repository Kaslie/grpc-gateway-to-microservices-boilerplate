## How to use this template

#### Before you start to edit this project, the require step are:
1. Define your proto at `grpc_protos` folder
2. Generate your protos with `make proto-build`
3. Checking your `client/modules/protos` and `server/modules/protos` directory, should have new proto definition

### Step:
1. Define your business logic at `/modules/services`
2. **Define** the interface or **edit** the interface before you create the **blueprint** or **servicers** at `modules/api_services/{service_name}`.
3. create the **servicer** class for GRPC and **blueprint** class for REST at `modules/api_services/{service_name}`.
4. In the **servicer** / **blueprint** file, remember to inherit the **interface** that you defined. and add additional **Flask's Blueprint** class to your own blueprint class.
5. You will have to inherit the function that you defined at the interface, call your business logic inside the function.
6. * [GRPC] Register your **servicer** at `/modules/adapters/grpc_connection_adapter`.
   * [REST API] Register your blueprint at `/modules/adapters/rest_connection_adapter`.
   
   
### BEFORE DEPLOY:
1. Make sure download GRPC-HEALTH-PROBE from https://github.com/grpc-ecosystem/grpc-health-probe/
2. Build the docker images into registry
3. Include the image in your Application's Dockerfile

### ON DEPLOY:
1. Remember to run the GRPC-HEALTH-PROBE at Kubernetes' Readiness Probe
2. 