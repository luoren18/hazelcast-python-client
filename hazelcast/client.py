from connection import ConnectionManager
from cluster import ClusterManager

class HazelcastClient(object):
    _config = None

    def __init__(self, config=None):
        self._config = config
        self._connection_manager = ConnectionManager()
        self._cluster = ClusterManager(config, self._connection_manager)

    def get_map(self, name):
        pass

class Config:
    def __init__(self):
        self._username = ""
        self._password = ""
        self._addresses = []

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        self._username = value

    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, value):
        self._password = value

    def add_address(self, address):
        self._addresses.append(address)

    def get_addresses(self):
        return self._addresses