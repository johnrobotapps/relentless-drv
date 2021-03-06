
"""Schema for validating datastructures

  --> schema embedded dict layers

top -    Mongo Database
second-  Mongo Collection

lower-   App Datastructure

"""

__all__ = [
    "minimal_schema",
    "ADMIN_FIELDS",
]



from uuid import UUID
from .validators import *



ADMIN_FIELDS = [
    "admin", "config", "local",
]



# Can be tuple of synonyms or string
#  - first in tuple used for display
muscle_groups = {
    ("shoulders", "deltoids"),
    "triceps", "biceps",
    "quads", "hamstrings", "calves",
    "glutes", "forearms", "chest",
    "abs", "lower back", "traps",
    "lats", "mid back", "obliques",
}


video_formats = [
    ".gif", ".mp4",
]


exercise_item = {
    "_id":         isType(UUID),
    "name":        isString,
    "description": isString,
    "filename":    isVideoDataFiletype,
    "muscleGroup": isaMuscleGroup,
}


food_item = {
    "_id":    isType(UUID),
    "name":   isString,
    "macros": isMacroData,
}


food_journal_entry = {
    "consumed":  isType(float),
    "published": isType(float),
}

food_journal_entry.update(food_item)


food_journal = {
    "_id":       isType(UUID),
    "date":      isDate,
    "published": isType(float),
    "foodItems": food_journal_entry,
}

weight_entry = {
    "_id":       isType(UUID),
    "date":      isDate,
    "published": isType(float),
    "weight":    isType(float),
}


user_profile = {
    "_id":         isType(UUID),
    "name":        isString,
    "device":      isInteger,
    "username":    isUserName,
    "foodJournal": food_journal,
    "weight":      weight_entry,
}


minimal_schema = {

    # DATABASE
    "relentless-storage" : {

        # COLLECTIONs
        "exerciseLibrary": exercise_item,
        "foodItemLibrary": food_item,
        "users":           user_profile,
    }
}


