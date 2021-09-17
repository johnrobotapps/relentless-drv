

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


isVideoDataFiletype = lambda v: any([
    v.endswith(sfx)
    for sfv in video_formats
])


exercise_library_item = {
    "name": str,
    "description": str,
    "video": isVideoDataFiletype,
    "muscleGroup": isaMuscleGroup,
}


foodjournal_item = {
    "name": str,
    "nutrition": isNutritionData,
}


app_dict = {
    "exerciseLibrary": exercise_library_item,
}


user_dict = {
    "name": str,
    "device": int,
    "foodJournal": foodjournal_item,
}


minimal_schemas = {
    "APP" : app_dict,
    "USER": user_dict,
}


