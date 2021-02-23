# coding=utf-8
import proto.hello_pb2 as pb2
import proto.hello_pb2_grpc as pb2_grpc
import time
import naming
from registry.registry_type import regisrty_type

class Greeter(pb2_grpc.HelloServiceServicer):
    addr = '127.0.0.1:50051'
    def __init__(self,address):
        self.address = address
    def Echo(self,request,context):
        print('request from: ' + context.peer())
        return pb2.Payload(data='response from:' + self.addr)

def main():
    # naming = nam(host='127.0.0.1', port=8500)
    # server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    # greeter = Greeter()
    # pb2_grpc.add_HelloServiceServicer_to_server(greeter,server)
    # server.add_insecure_port(greeter.addr)
    # naming.register('test',greeter.addr,5)
    # server.start()
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
    try:
        while 1:
    except KeyboardInterrupt:
        service.stop()

if __name__=='__main__':
    main()