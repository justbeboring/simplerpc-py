# coding=utf-8
import grpc
import etcd3
import time

class resolver(object):
    cli = None

    def __init__(self,host,port):
        self.cli = etcd3.client(host=host, port=port)

    def resolve(self,name,channel_dic):
        while 1:
            values = self.cli.get_prefix(name)
            for weight, key in values:
                addr = str(key.key,encoding='utf-8').replace(name + '/','')
                if not addr in channel_dic:
                    count = int.from_bytes(weight,byteorder='big',signed=False)
                    for i in range(count):
                        channel = grpc.insecure_channel(addr)
                        channel_dic[addr] = channel
            time.sleep(1)