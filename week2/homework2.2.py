from pymongo import MongoClient, ASCENDING
from collections import defaultdict

client = MongoClient()
db = client.students
collect = db.grades

query = collect.find().sort("student_id", ASCENDING)

data = defaultdict(dict)
for item in query:
    if not data[item['student_id']].get('score'):
        data[item['student_id']] = item
    elif data[item['student_id']]['score'] >= item['score']:
        data[item['student_id']] = item

for key, value in data.iteritems():
    print collect.remove({"_id": value['_id']})