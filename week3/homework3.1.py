from pymongo import MongoClient, ASCENDING
from collections import defaultdict

client = MongoClient()
db = client.school
collect = db.students

query = tmp = collect.aggregate(
    [
        {'$unwind':'$scores'},
        {"$match": {"scores.type": "homework"}},
        {"$sort": {"_id":ASCENDING, 'scores':ASCENDING}},
        {"$group": {"_id": "$_id", "scores": {"$push": "$scores"}}}
    ]
)

data = defaultdict(dict)
for item in query:
    collect.update_one({"_id": item['_id']},
        {"$pull": {
            "scores": {
                    "score": item['scores'][0]['score'],
                    "type": item['scores'][0]['type'],
                }
            }
        })