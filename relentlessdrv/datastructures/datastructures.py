

__all__ = [
    "minimal_schemas",
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
    item, muscle_groups
)


# Can be tuple of synonyms or string
muscle_groups = {
    ("shoulders", "deltoids"),
    "triceps", "biceps",
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


minimal_schemas = {
    "APP" : app_dict,
    "USER": user_dict,
}


