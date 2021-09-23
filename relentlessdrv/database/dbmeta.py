

from .mongodb import MongoDB, MongoClient



class DBMeta(type):


    def __init__(cls, *args, **kwargs):

        cls._database = None


    @property
    def database(cls):

        return cls._database


    @database.setter
    def database(cls, mongodb):

        if cls._database is None:
            if type(mongodb) is MongoClient:
                cls._database = mongodb


