

__all__ = [
    "MongoDB",
]



from pymongo import MongoClient
from pprint import pformat

from ..datastructures import ADMIN_FIELDS
from .._logger import get_logger

logger = get_logger(__name__)



class MongoDB:
    """Interface to the Mongo Database
    simple wrapper for `pymongo.MongoClient`
    """


    @property
    def connected(self):
        """Check if instance is connected to DB

        """

        return bool(
            self._client.server_info()
        ) if self._client else False


    def __validate(self, document, target):
        """Validity check of doc against schema

        """

        assert bool(target)

        m = self._schema
        validated = False

        while target:
            m = m[target.pop()]

        # Every field in schema must
        # exist in the doc
        for k,checking_func in m:
            try: checking_func(doc[k])
            except: break

        else:
            validated = True

        return validated


    def _validate_document(self, document):
        """Validate a document for a MongoDB
        collection against existing schema.
        The document must be a dict embedded
        in length 1 dicts to navigate to the
        correct collection.

        """

        validated = False

        if len(document) == 1:

            target = list(document)
            doc = document[target[0]]

            logger.info(f"length is 1? {len(doc)}")

            # TODO need to make sure doc is
            #      still dict-like
            while len(doc) == 1 and type(doc) is dict:

                logger.debug(pformat(target))
                logger.debug(pformat(doc))

                t = list(doc)[0]
                target.append(t)
                doc = doc[t]

            else:
                validated = self.__validate(
                    doc, target
                )
        
        return validated


    def add_document(self, document):
        """Documents are added with the full address
        dict address via length 1 embedded dicts

        ie {"database": {"collection": datadict}}

        """

        if self.connected:

            if self._validate_document(document):

                self._client.insert_one(
                    doc
                )

                logger.info((
                    "Added:\n -Target: {}"
                    "\n -Doc: {}\n".format(
                    target, doc)
                ))

        else:
            pass


    def __init__(self, host="localhost", port=27017):

        super(MongoDB, self).__init__()

        assert type(host) is str
        assert type(port) is int

        self.port = port
        self.host = host

        self._client = None
        self._schema = None


    @property
    def schema(self):
        return self._schema


    @schema.setter
    def schema(self, schema):
        """Embedded dicts with some boolean
        function for every bottom-level field.
        Function later used to check entries

        """

        # TODO schema should be validated
        #      that is has correct setup
        assert type(schema) is dict

        if self._schema is None:
            self._schema = schema


    def connect(self):

        if self._client is None:
            self._client = MongoClient(
                port=self.port, host=self.host,)


    def is_empty(self):

        return bool(self)


    def __bool__(self):

        return bool(len(self.__list_myself()))


    def __list_myself(self):

        return [
            nm for nm in 
            self._client.list_database_names()
            if nm not in ADMIN_FIELDS 
        ]


    def __iter__(self):
        if self.connected:
            yield iter(self.__list_myself())


    def create(self):
        raise Exception("NOPE")


