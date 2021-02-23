# coding=utf-8

from registry._etcdv3.naming import naming as etcd
from registry._consul.naming import naming as consul
from registry._redis.naming import naming as redis
from registry._zk.naming import naming as zk
import grpc
from concurrent import futures

class service(object):
    name = None
    address = None
    grpc_server = None
    registries = []
    def __init__(self, name,address):
        self.name = name
        self.address = address
        self.grpc_server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    def add_registry(self,type,host, port):
        if type == 'etcd':
            self.registries.append(etcd(host, port))
        elif type == 'consul':
            self.registries.append(consul(host, port))
        elif type == 'redis':
            self.registries.append(redis(host, port))
        elif type == 'zookeeper':
            self.registries.append(zk(host, port))

    def register(self):
        for registry in self.registries:
            registry.register(self.name,self.address,1)

    def unregister(self):
        for registry in self.registries:
            registry.unregister(self.name,self.address,1)

    def run(self):
        self.grpc_server.add_insecure_port(self.address)
        self.grpc_server.start()

    def stop(self):
        self.grpc_server.stop()
        self.unregister()

