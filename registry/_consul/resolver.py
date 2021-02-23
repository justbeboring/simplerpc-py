# coding=utf-8
import grpc
import consul
import time

class resolver(object):
    cli = None
    def __init__(self, host, port):
        self.cli = consul.Consul(host=host, port=port)
    def resolve(self,name,channel_dic):
        cli = consul.Consul()
        while 1:
            services = cli.agent.services()
            for s in services:
                if name in s:
                    items = s.split('/')
                    addr = items[len(items) - 1]
                    if not addr in channel_dic:
                        channel = grpc.insecure_channel(addr)
                        channel_dic[addr] = channel
            time.sleep(1)