
from pymongo import MongoClient


#class __MongoDB_Protected:
#    _add_db_method_name = HARDBRACKETS MAGIC METHOD
#    def block:
#        setattr(getattr(
#            _add_db_method_name), lambda: None)
#        

#class MongoDB(__MongoDB_Protected):


class MongoDB:


    def __init__(self, db_url=None):

        super(MongoDB, self).__init__()

        assert (db_url is None) or (type(db_url) is str)

        self._client = None

        if db_url is None:
            db_url = "mongodb://localhost:27017/"

        self._db_url = db_url


    def connect(self):

        if self._client is None:
            self._client = MongoClient(self.db_url)


    def _assert_is_empty(self):

        return bool(self)


    def __bool__(self):

        return bool(len(self.__list_myself))


    def __list_myself(self):

        return self._client.list_database_names()


    def create(self):
        raise Exception("NOPE")


