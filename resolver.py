# coding=utf-8

from registry._etcdv3.resolver import resolver as etcd
from registry._consul.resolver import resolver as consul
from registry._redis.resolver import resolver as redis
from registry._zk.resolver import resolver as zk
import _thread

class resolver(object):
    name = None
    channel_dic = {}
    registries = []
    addr_index = 0
    def __init__(self, name):
        self.name = name

    def add_registry(self,type,host, port):
        if type == 'etcd':
            self.registries.append(etcd(host, port))
        elif type == 'consul':
            self.registries.append(consul(host, port))
        elif type == 'redis':
            self.registries.append(redis(host, port))
        elif type == 'zookeeper':
            self.registries.append(zk(host, port))

    def resolving(self):
        for registry in self.registries:
            _thread.start_new_thread(registry.resolve,(self.name,self.channel_dic))

    def get_channel(self):
        count = len(self.channel_dic)
        if count == 0:
            return None
        channel = list(self.channel_dic.values())[self.addr_index]

        self.addr_index += 1
        if self.addr_index == count:
            self.addr_index = 0
        return channel