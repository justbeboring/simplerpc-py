# coding=utf-8
import grpc
import redis
import time

class resolver(object):
    cli = None
    def __init__(self,host,port):
        self.cli = redis.Redis(host=host, port=port)

    def resolve(self,name,channel_dic):
        cli = redis.Redis(host='127.0.0.1', port=6379)
        p = cli.pubsub()
        p.subscribe(name)
        while 1:
            msg = p.get_message()
            # print(msg)
            if msg == None:
                continue
            data = msg['data']
            if data == 1:
                continue
            cmd = str(data, 'utf-8').split('\t')
            if cmd[0] == 'keep':
                if not cmd[1] in channel_dic:
                    count = int(cmd[2])
                    for i in range(count):
                        channel = grpc.insecure_channel(cmd[1])
                        channel_dic[cmd[1]] = channel
            else:
                channel_dic.pop(cmd[1])
            time.sleep(1)