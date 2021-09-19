

MINIMAL_TEMPLATE = {
    "APP": {
        "exerciseLibrary": {
            "description": "a description of exercise string",
            "muscleGroup": "a muscle group name string",
            "name": "name of the exercise",
            "video": "video file name",
        }
    },
    "USER": {
        "device": 9999999,
        "name": "the users name",
        "foodJournal": {
            "name": "this field wont exist for too long",
            "nutrition": "nutrition data",
        },
    }
}

fakelogs = [
    {
        "id": 0,
        "date": "2021-09-18",
        "data": {
            "fooditems": [
                {
                    "name": "Mashed Potatoes",
                    "id": 0,
                    "macros": [0.06, 0.13, 0.05],
                    "consumed": 124.4,
                },
            ],
        },
        "published": 1632002978.872485
    },

    {
        "id": 1,
        "date": "2021-09-17",
        "data": {
            "fooditems": [
                {
                    "name": "Gravy",
                    "id": 1,
                    "macros": [0.114, 0.13, 0.05],
                    "consumed": 37.5,
                },
            ],
        },
        "published": 1631916603.2869868
    },

    {"id": 2,
     "date": "2021-09-16",
        "data": {
            "fooditems": [
                {
                    "name": "Biscuit",
                    "id": 2,
                    "macros": [0.19, 0.33, 0.04],
                    "consumed": 35.1,
                },
            ],
        },
     "published": 1631820232.5943558}
]
