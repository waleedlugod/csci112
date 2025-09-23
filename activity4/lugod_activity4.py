from pymongo import *

conn = MongoClient("mongodb://localhost:27018")

conn.drop_database("manilaRecords")

# 1
db = conn["manilaRecords"]

# 2
coll = db["lugod_edSheeranDiscography"]

# 3
coll.insert_many(
    [
        {
            "title": "The A Team",
            "year": 2011,
            "album": "plus",
            "runtime": 259,
        },
        {
            "title": "Drunk",
            "year": 2011,
            "album": "plus",
            "runtime": 201,
        },
        {
            "title": "U.N.I",
            "year": 2011,
            "album": "plus",
            "runtime": 229,
        },
        {
            "title": "Grade 8",
            "year": 2011,
            "album": "plus",
            "runtime": 180,
        },
        {
            "title": "Wake Me Up",
            "year": 2011,
            "album": "plus",
            "runtime": 230,
        },
        {
            "title": "One",
            "year": 2014,
            "album": "multiply",
            "runtime": 253,
        },
        {
            "title": "I’m a Mess",
            "year": 2014,
            "album": "multiply",
            "runtime": 245,
        },
        {
            "title": "Sing",
            "year": 2014,
            "album": "multiply",
            "runtime": 236,
        },
        {
            "title": "Don’t",
            "year": 2014,
            "album": "multiply",
            "runtime": 220,
        },
        {
            "title": "Nina",
            "year": 2014,
            "album": "multiply",
            "runtime": 226,
        },
        {
            "title": "Eraser",
            "year": 2017,
            "album": "divide",
            "runtime": 228,
        },
        {
            "title": "Castle on the Hill",
            "year": 2017,
            "album": "divide",
            "runtime": 262,
        },
        {
            "title": "Dive",
            "year": 2017,
            "album": "divide",
            "runtime": 239,
        },
        {
            "title": "Shape of You",
            "year": 2017,
            "album": "divide",
            "runtime": 234,
        },
        {
            "title": "Perfect",
            "year": 2017,
            "album": "divide",
            "runtime": 264,
        },
        {
            "title": "Tides",
            "year": 2021,
            "album": "equals",
            "runtime": 196,
        },
        {
            "title": "Shivers",
            "year": 2021,
            "album": "equals",
            "runtime": 208,
        },
        {
            "title": "First Times",
            "year": 2021,
            "album": "equals",
            "runtime": 186,
        },
        {
            "title": "Bad Habits",
            "year": 2021,
            "album": "equals",
            "runtime": 232,
        },
        {
            "title": "Overpass Graffiti",
            "year": 2021,
            "album": "equals",
            "runtime": 237,
        },
        {
            "title": "Boat",
            "year": 2023,
            "album": "subtract",
            "runtime": 186,
        },
        {
            "title": "Salt Water",
            "year": 2023,
            "album": "subtract",
            "runtime": 240,
        },
        {
            "title": "Eyes Closed",
            "year": 2023,
            "album": "subtract",
            "runtime": 195,
        },
        {
            "title": "Life Goes On",
            "year": 2023,
            "album": "subtract",
            "runtime": 211,
        },
        {
            "title": "Dusty",
            "year": 2023,
            "album": "subtract",
            "runtime": 223,
        },
    ]
)

# 4
coll.insert_many(
    [
        {
            "title": "Magical",
            "year": 2023,
            "album": "autumn variations",
            "runtime": 195,
        },
        {
            "title": "England",
            "year": 2023,
            "album": "autumn variations",
            "runtime": 227,
        },
    ]
)

# 5
for song in coll.find({"$or": [{"year": 2019}, {"year": 2020}]}):
    print(song)

# 6
coll.update_many(
    {"album": "plus"},
    {
        "$set": {
            "credits": {
                "producers": [
                    "Jake Gosling",
                    "Steve Robson",
                    "Example",
                    "Chris Leonard",
                    "Paul Golder",
                ]
            }
        }
    },
)
coll.update_many(
    {"album": "multiply"},
    {
        "$set": {
            "credits": {
                "producers": [
                    "Ed Sheeran",
                    "Steve Robson",
                    "Jake Gosling",
                    "Benny Blanco",
                    "Rick Rubin",
                    "Mike Elizondo",
                    "Jimmy Napes",
                ]
            }
        }
    },
)
coll.update_many(
    {"album": "divide"},
    {
        "$set": {
            "credits": {
                "producers": [
                    "Ed Sheeran",
                    "Steve Robson",
                    "Benjamin Levin (Benny Blanco)",
                    "Mike Elizondo",
                    "Foy Vance",
                    "Ryan Tedder",
                ]
            }
        }
    },
)
coll.update_many(
    {"album": "equals"},
    {
        "$set": {
            "credits": {
                "producers": [
                    "Ed Sheeran",
                    "Steve Robson",
                    "Aaron Dessner",
                    "Jacknife Lee",
                    "Max Martin",
                    "FRED",
                    "Ben Kohn",
                ]
            }
        }
    },
)
coll.update_many(
    {"album": "subtract"}, {"$set": {"credits": {"producers": ["Dessner"]}}}
)
coll.update_many(
    {"album": {"$ne": "autumn variations"}},
    {"$set": {"credits.writer": "Ed Sheeran"}},
)

# 7
coll.update_many({}, {"$rename": {"runtime": "duration"}})

# 8
for song in coll.find({"album": "multiply", "duration": {"$gt": 240}}):
    print(song)

# 9
coll.delete_many({"album": "autumn variations"})

conn.close()
