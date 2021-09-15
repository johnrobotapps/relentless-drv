#!/usr/bin/env python


import pymongo

import sys


from .datastructures import DATABASE_FORMAT



REQUIRED_FIELDS = list(DATABASE_FORMAT)


# SECOND ARGUMENT is always dburl if given
nargs = 2
nargv = len(sys.argv[1:])

args = list()

assert 1 == nargv <= nargs

# SECOND ARGUMENT is always dburl if given
if nargv:
    args = sys.argv[1:]
    dbname = sys.argv[1]
    dburl = args[2]


client = MongoClient(dburl)

newdb = client[dbname]


for field in REQUIRED_FIELDS:
    newdb.create_collection(field)



