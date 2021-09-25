

def isType(cls):
    return lambda item: type(item) is cls



def isDate(entrydate):

    parts = entrydate.split("-")

    if type(entrydate) is not str:
        return False

    elif int(parts[0]) - 2020 < 1:
        return False

    elif int(parts[1]) not in list(range(1,13)):
        return False

    elif int(parts[2]) not in list(range(1,31)):
        return False

    return True



isSomewhereIn = lambda item, grouping: any([
    item == gritem
    if type(gritem) is not tuple
    else any([
        item==ggritem
        for ggritem in gritem
    ])
    for gritem in grouping
])



isaMuscleGroup = lambda item: isSomewhereIn(
    item, muscle_groups
)


isVideoDataFiletype = lambda v: any([
    v.endswith(sfx)
    for sfv in video_formats
])



isMacroData = lambda: True

isString = lambda s: type(s) is str

isInteger = lambda i: type(i) is int

isUserName = lambda s: isString(s) and (len(s.split()) == 1)


