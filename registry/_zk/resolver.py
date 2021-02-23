# coding=utf-8
import grpc
from kazoo.client import KazooClient
import time

class resolver(object):
    cli = None

    def __init__(self,host,port):
        self.cli =KazooClient(hosts=host + ":" + str(port))
        self.cli.start()

    def resolve(self,name,channel_dic):
        while 1:
            children = self.cli.get_children(path=name)
            channel_dic.clear()
            for child in children:
                weight = self.cli.get(path=name + "/" + child)
                count = int.from_bytes(weight[0],byteorder='big',signed=False)
                for i in range(count):
                    channel_dic[child] = grpc.insecure_channel(child)
            time.sleep(1)