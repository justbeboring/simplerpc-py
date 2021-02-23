# simplerpc-py
a simple rpc-frame over grpc with registry(etcd/consul/zookeeper/redis) and load-balance(weighted-round-roubin/weighted-random).

server:

    addr = '127.0.0.1:50051'
    service = naming.service('test',addr)
    service.add_registry(type='etcd',host='127.0.0.1',port=2379)
    # service.add_registry(type='consul', host='127.0.0.1', port=8500)
    # service.add_registry(type='zookeeper', host='127.0.0.1', port=2181)
    # service.add_registry(type='redis', host='127.0.0.1', port=6379)
    service.register()
    greeter = Greeter(addr)
    pb2_grpc.add_HelloServiceServicer_to_server(greeter,service.grpc_server)
    service.run()
    
client:

    resv = resolver.resolver(name='/simple_rpc/test')
    resv.add_registry(type='etcd',host='127.0.0.1',port=2379)
    resv.resolving()
    channel = resv.get_channel()
    stub = pb2_grpc.HelloServiceStub(channel)
    response = stub.Echo(pb2.Payload(data='hello'))
    print(response)
