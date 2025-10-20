from pymongo import *
import datetime

conn = MongoClient("mongodb://localhost:27018")

dbLocation = conn["location"]
collLocation = dbLocation["locationDetectionLog"]

dbPromo = conn["promo"]
collPromo = dbPromo["promoAvailments"]


f = open("yup.txt", "w")
pipelineYuppies = [
    {
        "$match": {
            "subsProfile.age": {"$gte": 22, "$lte": 50},
            "subsProfile.sex": "Female",
            "subsProfile.cityAddress": "Busan",
            "latitude": {"$gte": 37.4, "$lte": 37.6},
            "longitude": {"$gte": 126, "$lte": 127},
            "timestamp": {
                "$gte": datetime.datetime(2024, 9, 1),
                "$lte": datetime.datetime(2024, 9, 30),
            },
        },
    },
    {
        "$group": {
            "_id": "$msisdn",
            "id": {"$first": "$_id"},
        }
    },
    {
        "$project": {
            "_id": "$id",
            "msisdn": "$_id",
        }
    },
    {
        "$out": {"db": "marketing", "coll": "lugod_yuppiesPromo"},
    },
]
for _ in collLocation.aggregate(pipelineYuppies):
    f.write(f"{_}\n")

f = open("go.txt", "w")
pipelineGoData = [
    {
        "$match": {
            "promo": "GODATA",
            "availmentDate": {
                "$gte": datetime.datetime(2024, 6, 1),
                "$lte": datetime.datetime(2024, 9, 30),
            },
            "denom": {"$eq": 1000},
        }
    },
    {
        "$group": {
            "_id": "$msisdn",
            "id": {"$first": "$_id"},
            "totalSpending": {"$sum": "$denom"},
        }
    },
    {"$match": {"totalSpending": {"$gte": 7000}}},
    {
        "$project": {
            "_id": "$id",
            "msisdn": "$_id",
        }
    },
    {
        "$out": {"db": "marketing", "coll": "lugod_goDataPromo"},
    },
]
for _ in collPromo.aggregate(pipelineGoData):
    f.write(f"{_}\n")
