

__all__ = [
    "FoodJournal",
]



def isLogEntry(entrydate):

    parts = entrydate.split("-")

    if int(parts[0]) - 2020 < 1:
        return False

    elif int(parts[1]) not in list(range(1,13)):
        return False

    elif int(parts[2]) not in list(range(1,31)):
        return False

    return True



class FoodJournal:

    def __init__(self, logentries):

        for entrydate in list(logentries):
            assert isLogEntry(entrydate)

        self._logentries = logentries


    def get_log_entry(self, date):

        return self._logentries.get(date, None)



