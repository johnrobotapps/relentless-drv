

__all__ = [
    "minimal_schemas",
    "ADMIN_FIELDS",
]



ADMIN_FIELDS = [
    "admin", "config", "local",
]



isin = lambda item, grouping: any([
    item == gritem
    if type(gritem) is not tuple
    else any([
        item==ggritem
        for ggritem in gritem
    ])
    for gritem in grouping
])


isaMuscleGroup = lambda item: isin(
    item, muscle_groups
)

isNutritionData = lambda: True
isString = lambda s: type(s) is str
isInteger = lambda i: type(i) is int

isVideoDataFiletype = lambda v: any([
    v.endswith(sfx)
    for sfv in video_formats
])


# Can be tuple of synonyms or string
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


exercise_library_item = {
    "name": isString,
    "description": isString,
    "video": isVideoDataFiletype,
    "muscleGroup": isaMuscleGroup,
}


foodjournal_item = {
    "name": isString,
    "nutrition": isNutritionData,
}


app_dict = {
    "exerciseLibrary": exercise_library_item,
}


user_dict = {
    "name": isString,
    "device": isInteger,
    "foodJournal": foodjournal_item,
}


minimal_schemas = {
    "APP" : app_dict,
    "USER": user_dict,
}


