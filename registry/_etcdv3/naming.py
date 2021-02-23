# coding=utf-8
import etcd3
from multiprocessing import cpu_count
import _thread
import time


class naming(object):
    schema = 'simple_rpc'
    cli = None

    def __init__(self, host, port):
        self.cli = etcd3.client(host=host, port=port)

    def register(self, name, addr, ttl):
        result = self.cli.get('/' + self.schema + '/' + name + '/' + addr)
        if result[0] == None:
            self.withAlive(name,addr, ttl)

    def withAlive(self, name, addr, ttl):
        lease = self.cli.lease(ttl=ttl)
        self.cli.put(key='/' + self.schema + '/' + name + '/' + addr, value=str.encode(str(cpu_count())), lease=lease)
        _thread.start_new_thread(self.keepAlive,(lease,))

    def keepAlive(self, lease):
        while 1:
            lease.refresh()
            time.sleep(3)

    def unregister(self, name, addr):
        self.cli.delete('/' + self.schema + '/' + name + '/' + addr)
