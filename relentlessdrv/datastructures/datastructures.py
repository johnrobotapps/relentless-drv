

__all__ = [
    "minimal_schemas",
    "ADMIN_FIELDS",
]



ADMIN_FIELDS = [
    "admin", "config", "local",
]


def isLogEntryDate(entrydate):

    parts = entrydate.split("-")

    if int(parts[0]) - 2020 < 1:
        return False

    elif int(parts[1]) not in list(range(1,13)):
        return False

    elif int(parts[2]) not in list(range(1,31)):
        return False

    return True



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

isVideoDataFiletype = lambda v: any([
    v.endswith(sfx)
    for sfv in video_formats
])

isMacroData = lambda: True
isString = lambda s: type(s) is str
isInteger = lambda i: type(i) is int


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


foodjournal_entry = {
    "name": isString,
    "date": is,
    "macros": isMacroData,
}


app_dict = {
    "exerciseLibrary": exercise_library_item,
}


user_dict = {
    "name": isString,
    "device": isInteger,
    "foodJournal": foodjournal_entry,
}


minimal_schemas = {
    "APP" : app_dict,
    "USER": user_dict,
}



