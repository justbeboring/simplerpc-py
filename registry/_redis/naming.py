# coding=utf-8
import redis
from multiprocessing import cpu_count
import _thread
import time


class naming(object):
    schema = 'simple_rpc'
    cli = None

    def __init__(self, host, port):
        self.cli = redis.Redis(host=host, port=port)

    def register(self, name, addr, ttl):
        result = self.cli.get('/' + self.schema + '/' + name + '/' + addr)
        if result == None:
            self.withAlive(name,addr, ttl)

    def withAlive(self, name, addr, ttl):
        _thread.start_new_thread(self.keepAlive,(name, addr, ttl))

    def keepAlive(self, name, addr,ttl):
        while 1:
            self.cli.publish(channel='/' + self.schema + '/' + name, message=str.encode('keep\t' + addr + '\t' + str(cpu_count()),encoding='utf-8'))
            time.sleep(ttl)

    def unregister(self, name, addr):
        self.cli.publish(channel='/' + self.schema + '/' + name,
                           message=str.encode('del' + addr + '\t' + str(cpu_count())))
