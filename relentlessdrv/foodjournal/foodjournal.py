

__all__ = [
    "FoodJournal",
]


from ..database import DBMeta

from ..datastructures import foodjournal_entry
from ..datastructures.datastructures import isLogEntryData



class FoodJournal(metaclass=DBMeta):

    def __init__(self, logentries):

        for entrydate in list(logentries):
            assert isLogEntryDate(entrydate)

        self._logentries = logentries


    def get_log_entry(self, date):

        return self._logentries.get(date, None)



