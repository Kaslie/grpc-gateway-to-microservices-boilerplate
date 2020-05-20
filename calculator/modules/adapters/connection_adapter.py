class ConnectionAdapter(object):
    def __init__(self, connection_type):
        self.connection_type = connection_type

    def run(self):
        self.connection_type.run()
