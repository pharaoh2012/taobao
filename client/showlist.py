import json
import pymongo

mongo_con = pymongo.Connection("ds033067.mongolab.com", 33067)
mongo_db = mongo_con.tanktotal
mongo_db.authenticate("redhat", "3.14159")


items = mongo_db.tabaotry.find().sort([(
    "date", pymongo.DESCENDING), ("gailv", pymongo.ASCENDING)]).limit(20)
