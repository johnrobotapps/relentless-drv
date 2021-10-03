

"""These definitions from example are the true description
of correct database entries. Schema enforcement is made to
match what is manually entered and inspected from here.

Comments are used to clarify important points and TODOs.

Fields can always be added, but (fingers crossed) the
global structure will remain static after a new data field
is defined.
"""



__all__ = [
    "minimalTemplate",
#    "template_by_document",
]



from uuid import UUID, uuid4
from pprint import pformat

from .._logger import get_logger


logger = get_logger(__name__)



#def _gen_addresses(key, datadict, _routes, _root):
#    """Generate the set of valid addresses for
#    data entry from a (presumably template)
#    collection.
#
#    `_routes` must be given as `[""]`
#    `_root` must be given as `""`
#
#    Arguments
#    ---------
#    key: `str` that marks routes through the data
#    datadict: `dict` with embedded dicts/lists
#
#    Returns
#    -------
#    `list` of addresses
#
#    Address format:
#     - a set of dict key tuples leading to
#       data entry points
#
#    Addresses include:
#     - [dbname, colname]
#
#    """


# THIS ONE is closest, givese duplicates
# TODO FIXME try to reduce _routes to single
#            or use the 'pop's to always
#            give one copy of each address
#def _gen_addresses(key, datadict, _routes, _root, q=1):
#    print((
#        f"{q} 1-                                 "
#        f"given fields {list(datadict)}"
#    ))
#    if hasattr(datadict, 'items'):
#        print("\n\n========================")
#        print(f"{q} 2-     {pformat(_routes)}")
#        for k,v in filter(
#            # skips all fields (ie _id) that
#            # are not iterable or strings
#            lambda i: hasattr(i[1], "__iter__") and \
#                type(i[1]) is not str,
#            datadict.items()
#        ):
#            print(f"{q} 3-                      AT>>> {k}")
#            # NOTE assumes length 1 outer dict
#            #      corresponding to a MongoDB
#            #      with name stored in _root
#            if not _root: _root += k
#            if not _routes[-1]: _routes[-1] += _root
#            #
#            u=1
#            if isinstance(v, dict):
#                print(f"{q} 4-     DICT DIVE")
#                print(f"          Now routes: {pformat(_routes)}")
#                for result in _gen_addresses(key, v, _routes, _root, q+1):
#                    print(f"{q} {u} 5-     HERE IS DDD {result}")
#                    print(f"            Now routes: {pformat(_routes)}")
#                    u+=1
#                    yield result
#                    print(f"{q} {u} 5-          RRRRroutes: {pformat(_routes)}")
#            elif isinstance(v, list):
#                print(f"{q} 6-     LIST DIVE")
#                for d in filter(
#                    lambda i: type(i) is dict,
#                    v[:1]
#                ):
#                    print(f"          Now routes: {pformat(_routes)}")
#                    if key in d:
#                        print(f"{q}           {pformat(_routes)}")
#                        print(f"{q} 7-    -->>> extending _route with {k}")
#                        _routes[-1] += f".{k}"
#                        if _routes[-1] != _root:
#                            print(f"{q} 7..-      YIELDING {_routes[-1]}")
#                            yield _routes[-1]
#                            print(f"{q} 7.-      afteryeld routes: {pformat(_routes)}")
#                    for result in _gen_addresses(key, d, _routes, _root+f".{k}", q+1):
#                        print(f"{q} {u} 8.-     HERE IS LLL {result}")
#                        print(f"            Now routes: {pformat(_routes)}")
#                        u+=1
#                        yield result
#                        print(f"{q} {u} 8-          RRRRroutes: {pformat(_routes)}")
#            else:
#                # `yield v` gives raw data
#                # from outermost call
#                #yield v
#                #print(f"{q}-     BB    bottom data: {v}")
#                pass
#        else:
#            print(f"{q} 9-     IN THE ELSERY")
#            # this yields valid addresses
#            # for data in a MongoDB
#            # string with "." separator
#            #  dbname.collname[.embedding]
#            if _routes[-1]:
#                #yield _routes[-1]
#                print(f"{q} 10..-      YIELDING {_routes[-1]}")
#                yield _routes.pop()
#                print(f"{q} 10.-      YELDed ")
#                _routes.append("")
#            print(f"{q} 10-     {pformat(_routes)}")






def _gen_addresses(key, datadict, _routes, _root, q=1):
    if hasattr(datadict, 'items'):
        for k,v in filter(
            lambda i: hasattr(i[1], "__iter__") and \
                type(i[1]) is not str,
            datadict.items()
        ):
            if not _root: _root += k
            if not _routes[-1]: _routes[-1] += _root
            if isinstance(v, dict):
                for result in _gen_addresses(key, v, _routes, _root, q+1):
                    yield result
            elif isinstance(v, list):
                for d in filter(
                    lambda i: type(i) is dict,
                    v[:1]
                ):
                    if key in d:
                        _routes[-1] += f".{k}"
                        if _routes[-1] != _root:
                            yield _routes[-1]
                    for result in _gen_addresses(key, d, _routes, _root+f".{k}", q+1):
                        yield result
        else:
            if _routes[-1]:
                yield _routes.pop()
                _routes.append("")



#set(_gen_addresses("_id", template, [""], ""))


#def _gen_addresses(key, datadict, _routes, _root, _route, q=1):
#    #print((
#    #    f"{q}1-                                 "
#    #    f"given {datadict}"
#    #))
#    if hasattr(datadict, 'items'):
#        #print("\n\n========================")
#        #print(f"{q}2-     {_routes}")
#        for k,v in filter(
#            lambda i: hasattr(i[1], "__iter__"),
#            datadict.items()
#        ):
#            #print(f"{q}3-     AT>>> {_routes[-1]}.{k}")
#            # NOTE assumes length 1 outer dict
#            #      corresponding to a MongoDB
#            #      with name stored in _root
#            if not _root: _root += k
#            if not _route: _route += _root
#            if not _routes[-1]: _routes[-1] += _root
#            if isinstance(v, dict):
#                #print(f"{q}4-     DICT DIVE")
#                for result in _gen_addresses(key, v, _routes, _root, _route, q+1):
#                    #print(f"{q}5-     HERE IS DDD {result}")
#                    yield result
#            elif isinstance(v, list):
#                #print(f"{q}6-     LIST DIVE")
#                for d in filter(
#                    lambda i: type(i) is dict,
#                    v[:1]
#                ):
#                    if key in d:
#                        if _routes[-1] != _root:
#                            print(f"{q}7-     yielding {_routes[-1]}=={_route}")
#                            yield _routes[-1]
#                        #print(f"{q}7-       -->>> adding data element {k}")
#                        _route += f".{k}"
#                        _routes[-1] += f".{k}"
#                    for result in _gen_addresses(key, d, _routes, _root, _route, q+1):
#                        #print(f"{q}8-     HERE IS LLL {result}")
#                        yield result
#            else:
#                # `yield v` gives raw data
#                # from outermost call
#                #yield v
#                #print(f"{q}-     BB    bottom data: {v}")
#                pass
#        else:
#            print(f"{q}9-     IN THE ELSERY")
#            # this yields valid addresses
#            # for data in a MongoDB
#            # string with "." separator
#            #  dbname.collname[.embedding]
#            if _routes[-1]:
#                print(f"{q}9-     yielding {_routes[-1]}=={_route}")
#                yield _routes[-1]
#                _route = ""
#                _routes.append("")
#            print(f"{q}10-     {_routes}, {_route}")
#
#
#template = minimalTemplate()
#list(_gen_addresses("_id", template, [""], "", ""))
#
#
#def _gen_addresses(key, datadict, _route, _root, q=1):
#    print((
#        f"{q}1-                                 "
#        f"given {datadict}"
#    ))
#    assert type(_route) is str
#    assert type(_root) is str
#    if hasattr(datadict, 'items'):
#        print("\n\n========================")
#        print(f"{q}2-     {_route}")
#        for k,v in filter(
#            lambda i: hasattr(i[1], "__iter__"),
#            datadict.items()
#        ):
#            print(f"{q}3-     AT>>> {_route}.{k}")
#            # NOTE assumes length 1 outer dict
#            #      corresponding to a MongoDB
#            #      with name stored in _root
#            if not _root: _root += k
#            if not _route: _route += _root
#            if isinstance(v, dict):
#                print(f"{q}4-     DICT DIVE")
#                for result in _gen_addresses(key, v, _route, _root, q+1):
#                    print(f"{q}5-     HERE IS DDD {result}")
#                    yield result
#            elif isinstance(v, list):
#                print(f"{q}6-     LIST DIVE")
#                for d in filter(
#                    lambda i: type(i) is dict,
#                    v[:1]
#                ):
#                    if key in d:
#                        # else we are at db level
#                        # iterating the collections
#                        if _route != _root:
#                            yield _route
#                        print(f"{q}7-       -->>> adding data element {k}")
#                        _route += f".{k}"
#                    for result in _gen_addresses(key, d, _route, _root, q+1):
#                        print(f"{q}8-     HERE IS LLL {result}")
#                        yield result
#            else:
#                # `yield v` gives raw data
#                # from outermost call
#                #yield v
#                print(f"{q}-          BB    bottom data: {v}")
#                #pass
#        else:
#            print(f"{q}9-      IN THE ELSERY")
#            print(f"{q}10-     {_route}")
#            # this yields valid addresses
#            # for data in a MongoDB
#            # string with "." separator
#            #  dbname.collname[.embedding]
#            yield _route
#            _route = ""
#
#
#
#list(_gen_addresses("_id",minimalTemplate(), "", ""))



def db_data_addresses(dbdict):

    if len(dbdict) != 1:
        logger.debug("dbdict length must be 1")

    dbname = list(dbdict)[0]
    result = {dbname: dict()}
    t = dbdict[dbname]

    for colname, collection in dbdict[dbname].iteritems():

        if type(collection) is not list:
            logger.debug((
                f"Collection {colname} is "
                f"type {type(collection)}, "
                f"list is required"
            ))
            continue


        result[dbname][colname] = list(_gen_addresses(collection))

        for doc in collection:

            if type(doc) is not dict:
                logger.debug((
                    f"Document in {colname} is "
                    f"type {type(doc)}, "
                    f"dict is required"
                ))
                continue

                for k,v in doc.items():
                    r.append(k)
                    g


# lowerCamel for factory type things
def minimalTemplate():
    """Random UUIDs created for template
    """
    return _replace_type(
        _minimal_template, UUID, uuid4
    )



def _replace_type(
    template_dict,
    cls,
    factory_func=None,
    result=None
):
    """Recursive function to complete templates
    by filling instances of required types using
    some factory func, which by default is done
    by calling the class for given type.

    TODO check that factory returns correct type

     - len 1 dict with embedded dicts then
       dict/list embedded

     - scan only top level of embedded list/list

    """

    if factory_func is None:
        factory_func = cls

    if result is None:
        result = dict()

    assert type(template_dict) is dict
    assert callable(factory_func)

    logger.debug("\n\nRESULT:")
    logger.debug(pformat(result))

    for field, value in template_dict.items():

        logger.debug("current field: %s"%field)
        logger.debug("current value:")
        logger.debug(pformat(value))

        if type(value) is list:

            logger.debug("LIST was found")

            r = result[field] = list()

            for v in value:

                if type(v) is dict:
                    r.append(dict())

                    _replace_type(
                        v,
                        cls,
                        factory_func,
                        result=r[-1],
                    )

                else:
                    r.append(v)

        elif type(value) is dict:

            logger.debug("DICT was found")

            r = result[field] = dict()

            _replace_type(
                value,
                cls,
                factory_func,
                result=r,
            )

        elif value is cls:
            logger.debug("GENERATE from factory: %s"%field)
            result[field] = factory_func()

        else:
            logger.debug("COPY: %s"%field)
            result[field] = value

    return result




# minimal FoodItem definition
foodItem1 = {
    "_id":    UUID,
    "name":   "Mashed Potatoes",
    "macros": [0.06, 0.13, 0.05],
}

foodItem2 = {
    "_id":    UUID,
    "name":   "Gravy",
    "macros": [0.114, 0.13, 0.05],
}

foodItem3 = {
    "_id":    UUID,
    "name":   "Biscuit",
    "macros": [0.19, 0.33, 0.04],
}

foodItem4 = {
    "_id":    UUID,
    "name":   "Candy",
    "macros": [0.03, 0.68, 0.0],
}



# minimal FoodLogItem definition
#  - changes to FoodItem for Log
foodLogItem1 = {
    "consumed":  124.4,
    "published": 1632002979.52341,
}

foodLogItem2 = {
    "consumed":  37.5,
    "published": 1631916607.2169868,
}

foodLogItem3 = {
    "consumed":  35.1,
    "published": 1631820233.5943558,
}

foodLogItem4 = {
    "consumed":  34.1,
    "published": 1631820233.5943558,
}

foodLogItem1.update(foodItem1)
foodLogItem2.update(foodItem2)
foodLogItem3.update(foodItem3)
foodLogItem4.update(foodItem4)



# Entries for FoodJournal collection
foodjournal_example = [
    {
        "_id":       UUID,
        "date":      "2021-09-16",
        "published": 1631720232.5943558,
        "fooditems": [
            foodLogItem3,
        ],
    },
    {
        "_id":       UUID,
        "date":      "2021-09-17",
        "published": 1631820232.5943558,
        "fooditems": [
            foodLogItem2,
            foodLogItem1,
            foodLogItem4,
        ],
    },
    {
        "_id":       UUID,
        "date":      "2021-09-18",
        "published": 1631916603.2869868,
        "fooditems": [
            foodLogItem1,
            foodLogItem2,
            foodLogItem3,
            foodLogItem4,
        ],
    },
    {
        "_id":       UUID,
        "date":      "2021-09-19",
        "published": 1632002978.872485,
        "fooditems": [
            foodLogItem1,
            foodLogItem2,
        ],
    },
]



_minimal_template = {
    # Database Name
    "relentless-storage": {
        # Collection Name
        "exerciseLibrary": [
            {
                "_id":         UUID,
                "muscleGroup": "biceps",
                "name":        "dumbell curl",
                "video":       "dumbell-curl.mp4",
                "description": "curl dumbell upwards from dead hang to shoulder",
            },
            {
                "_id":         UUID,
                "muscleGroup": "triceps",
                "name":        "tricep extension-rope",
                "video":       "tricep-extension-rope.mp4",
                "description": "extend rope downwards from shoulder to hanging position",
            },
        ],
        # Collection Name
        "foodItemLibrary": [
            foodItem1,
            foodItem2,
            foodItem3,
            foodItem4,
        ],
        # Collection Name
        "users": [
            {
                "_id":         UUID,
                "device":      333333333,
                "username":    "cooluser1",
                "name":        "Jane Doe",
                "birthday":    "1980-12-21",
                "foodJournal": foodjournal_example[:3],
                "weight": [
                    {
                        "_id":       UUID,
                        "published": 1631820233.594355,
                        "weight":    185,
                    },
                    {
                        "_id":       UUID,
                        "published": 1631840233.594355,
                        "weight":    186,
                    },
                    {
                        "_id":       UUID,
                        "published": 1631860233.594355,
                        "weight":    185,
                    },
                ],
            },
            {
                "_id":         UUID,
                "device":      333333334,
                "username":    "cooluser",
                "name":        "John Doe",
                "birthday":    "1984-2-16",
                "foodJournal": foodjournal_example[1:],
                "weight": [
                    {
                        "_id":       UUID,
                        "published": 1631843233.594355,
                        "weight":    201,
                    },
                    {
                        "_id":       UUID,
                        "published": 1631865233.594355,
                        "weight":    206,
                    },
                ],
            },
            {
                "_id":         UUID,
                "device":      333333335,
                "username":    "acooluser",
                "birthday":    "2001-5-3",
                "name":        "Jill Smith",
                "foodJournal": foodjournal_example[::2],
                "weight": [
                    {
                        "_id":       UUID,
                        "published": 1631843233.594355,
                        "weight":    123,
                    },
                    {
                        "_id":       UUID,
                        "published": 1631865233.594355,
                        "weight":    122,
                    },
                ],
            },
        ],
    },
}

