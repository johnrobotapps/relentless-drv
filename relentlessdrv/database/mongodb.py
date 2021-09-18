

__all__ = [
    "MongoDB",
]

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


    @property
    def connected(self):
        return bool(
            self._client.server_info()
        ) if self._client else False


    @staticmethod
    def __validate(document, target):

        validated = False

        assert bool(target)

        m = minimal_schemas
        while target:
            m = m[target.pop()]

        for k,checking_func in m:
            assert checking_func(doc[k])

        return validated


    def _validate_document(self, document):
        validated = False
        if len(document) == 1:
            target = list(document)
            doc = document[target]
            while len(doc) == 1:
                t = list(doc)[0]
                target.append(t)
                doc = doc[t]
            else:
                validated = self.__validate(
                    doc, target
                )
        
        return validated


    def add_document(self, document):

        if self.connected:
            if self._validate_document(document):
                target, doc = self.__validate(doc)
                self._client.insert_one(
                    doc
                )


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


