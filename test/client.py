# coding=utf-8
import proto.hello_pb2 as pb2
import proto.hello_pb2_grpc as pb2_grpc
import time
import resolver
from registry.registry_type import regisrty_type

def main():
    resv = resolver.resolver(name='/simple_rpc/test')
    resv.add_registry(type='etcd',host='127.0.0.1',port=2379)
    # resv.add_registry(type='consul', host='127.0.0.1', port=8500)
    # resv.add_registry(type='zookeeper', host='127.0.0.1', port=2181)
    # resv.add_registry(type='redis', host='127.0.0.1', port=6379)
    resv.resolving()
    while 1:
        try:
            channel = resv.get_channel()
            if channel != None:
                stub = pb2_grpc.HelloServiceStub(channel)
                response = stub.Echo(pb2.Payload(data='hello'))
                print(response)
                time.sleep(1)
        except:
            continue

if __name__ == '__main__':
    main()