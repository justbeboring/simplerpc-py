# coding=utf-8
import grpc
import consul
from multiprocessing import cpu_count
import _thread
import time
import socket
import _thread


class naming(object):
    schema = 'simple_rpc'
    cli = None

    def __init__(self, host, port):
        self.cli = consul.Consul(host=host, port=port)

    def register(self, name, addr, ttl):
        service_info = addr.split(':')
        self.cli.agent.service.register(
            name='/' + self.schema + '/' + name + '/' + addr,
            service_id='/' + self.schema + '/' + name + '/' + addr,
            address=service_info[0],
            port=int(service_info[1]),
            check=consul.Check().tcp(service_info[0],int(service_info[1])+1,'3s','5s','10s')
        )
        _thread.start_new_thread(self.consul_check,(service_info[0],int(service_info[1])+1))
    def withAlive(self, name, addr, ttl):
        _thread.start_new_thread(self.keepAlive,(name, addr, ttl))

    def keepAlive(self, name, addr,ttl):
        while 1:
            # self.cli.publish(channel='/' + self.schema + '/' + name, message=str.encode('keep\t' + addr + '\t' + str(cpu_count()),encoding='utf-8'))
            time.sleep(ttl)

    def unregister(self, name, addr):
        self.cli.agent.service.deregister(server_id='/' + self.schema + '/' + name + '/' + addr)

    def consul_check(self,host,port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((host, port))
        s.listen(5)
        while 1:
            s.accept()