

__all__ = [
    "DATABASE_FORMAT",
]


from uuid import UUID


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
    item, MUSCLE_GROUPS)


MUSCLE_GROUPS = {
    ("shoulders", "deltoids"), "triceps", "biceps",
    "quads", "hamstrings", "calves",
    "glutes", "forearms", "chest",
    "abs", "lower back", "traps",
    "lats", "mid back", "obliques",
}


exercise_library_item = {
    "name": str,
    "description": str,
    "muscleGroup": isaMuscleGroup,
}


app_dict = {
    "foodJournal": None,
    "exerciseLibrary": exercise_library_item,
}


user_dict = {
    "name": str,
    "device": int,
    "_id": UUID,
}


DATABASE_FORMAT = {
    "APP" : app_dict,
    "USER": user_dict,
}


