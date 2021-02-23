# coding=utf-8
from kazoo.client import KazooClient
from multiprocessing import cpu_count


class naming(object):
    schema = "simple_rpc"
    cli = None

    def __init__(self, host, port):
        self.cli = KazooClient(hosts=host + ":" + str(port))
        self.cli.start()
    def register(self, name, addr, ttl):
        ok = self.cli.exists(path="/" + self.schema)
        if not ok:
            self.cli.create(path="/" + self.schema)
            self.cli.create(path="/" + self.schema + "/" + name)
            self.cli.create(path="/" + self.schema + "/" + name + "/" + addr,value=cpu_count().to_bytes(4, byteorder='big', signed=False),ephemeral=True)
        else:
            ok = self.cli.exists(path="/" + self.schema + "/" + name)
            if not ok:
                self.cli.create(path="/" + self.schema + "/" + name)
                self.cli.create(path="/" + self.schema + "/" + name + "/" + addr,value=cpu_count().to_bytes(4, byteorder='big', signed=False),ephemeral=True)
            else:
                ok = self.cli.exists(path="/" + self.schema + "/" + name + "/" + addr)
                if not ok:
                    self.cli.create(path="/" + self.schema + "/" + name + "/" + addr,
                                    value=cpu_count().to_bytes(4, byteorder='big', signed=False), ephemeral=True)

    def unregister(self, name, addr):
        self.cli.stop()
