
from pymongo import MongoClient

from ..datastructures import ADMIN_FIELDS, minimal_schemas


#class __MongoDB_Protected:
#    _add_db_method_name = HARDBRACKETS MAGIC METHOD
#    def block:
#        setattr(getattr(
#            _add_db_method_name), lambda: None)
#        

#class MongoDB(__MongoDB_Protected):


class MongoDB:
    """Interface to the Mongo Database
    simple wrapper for `pymongo.MongoClient`
    """

    def __init__(self, host="localhost", port=27017):

        super(MongoDB, self).__init__()

        assert type(host) is str
        assert type(port) is int

        self.port = port
        self.host = host

        self._client = None


    def connect(self):

        if self._client is None:
            self._client = MongoClient(
                port=self.port, host=self.host,)


    def _assert_is_empty(self):

        return bool(self)


    def __bool__(self):

        return bool(len(self.__list_myself))


    def __list_myself(self):

        return self._client.list_database_names()


    def create(self):
        raise Exception("NOPE")


