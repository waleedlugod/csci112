from pymongo import *

conn = MongoClient("mongodb://localhost:27018")

conn.drop_database("manilaRecords")

db = conn["manilaRecords"]

db["lugod_edSheeranDiscography"].insert_many(
    [
        {
            "title": "The A Team",
            "year": "2011",
            "album": "plus",
            "runtime": "259",
        },
        {
            "title": "Drunk",
            "year": "2011",
            "album": "plus",
            "runtime": "201",
        },
        {
            "title": "U.N.I",
            "year": "2011",
            "album": "plus",
            "runtime": "229",
        },
        {
            "title": "Grade 8",
            "year": "2011",
            "album": "plus",
            "runtime": "180",
        },
    ]
)

conn.close()
