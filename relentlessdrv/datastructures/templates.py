

"""These definitions from example are the true description
of correct database entries. Schema enforcement is made to
match what is manually entered and inspected from here.

Comments are used to clarify important points and TODOs.

Fields can always be added, but (fingers crossed) the
global structure will remain static after a new data field
is defined.
"""



__all__ = ["minimalTemplate"]




from uuid import UUID, uuid4
from pprint import pformat

from .._logger import get_logger


logger = get_logger(__name__)



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
    "id":     UUID,
    "name":   "Mashed Potatoes",
    "macros": [0.06, 0.13, 0.05],
}

foodItem2 = {
    "name":   "Gravy",
    "id":     UUID,
    "macros": [0.114, 0.13, 0.05],
}

foodItem3 = {
    "id":     UUID,
    "name":   "Biscuit",
    "macros": [0.19, 0.33, 0.04],
}

foodItem4 = {
    "id":     UUID,
    "name":   "Candy",
    "macros": [0.03, 0.68, 0.0],
}



# minimal FoodLogItem definition
#  - changes to FoodItem for Log
foodLogItem1 = {
    "consumed":  124.4,
    "published": 1632002979.52341,
    "fooditem": foodItem1,
}

foodLogItem2 = {
    "consumed":  37.5,
    "published": 1631916607.2169868,
    "fooditem": foodItem2,
}

foodLogItem3 = {
    "consumed":  35.1,
    "published": 1631820233.5943558,
    "fooditem": foodItem3,
}

foodLogItem4 = {
    "consumed":  34.1,
    "published": 1631820233.5943558,
    "fooditem": foodItem4,
}



# Entries for FoodJournal collection
foodjournal_example = [
    {
        "id":        UUID,
        "date":      "2021-09-16",
        "published": 1631720232.5943558,
        "fooditems": [
            foodLogItem3,
        ],
    },
    {
        "id":        UUID,
        "date":      "2021-09-17",
        "published": 1631820232.5943558,
        "fooditems": [
            foodLogItem2,
            foodLogItem1,
            foodLogItem4,
        ],
    },
    {
        "id":        UUID,
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
        "id":        UUID,
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
                "id":          UUID,
                "muscleGroup": "biceps",
                "name":        "dumbell curl",
                "video":       "dumbell-curl.mp4",
                "description": "curl dumbell upwards from dead hang to shoulder",
            },
            {
                "id":           UUID,
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
                "id":          UUID,
                "device":      333333333,
                "username":    "cooluser1",
                "name":        "Jane Doe",
                "foodJournal": foodjournal_example[:3],
            },
            {
                "id":          UUID,
                "device":      333333334,
                "username":    "cooluser",
                "name":        "John Doe",
                "foodJournal": foodjournal_example[1:],
            },
            {
                "id":          UUID,
                "device":      333333335,
                "username":    "acooluser",
                "name":        "Jill Smith",
                "foodJournal": foodjournal_example[::2],
            },
        ],
    },
}

