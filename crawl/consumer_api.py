from stackapi import StackAPI
from datetime import date
from connect_mongo import Mongo_connection

if __name__ == '__main__':

    my_db = Mongo_connection(hostname='mongodb')

    SITE = StackAPI('stackoverflow')
    SITE.page_size=100
    SITE.max_pages=5

    q = SITE.fetch('questions', fromdate=date(2019,4,1), todate=date(2019,4,30))

    for item in q["items"]:
        my_db.questions_collection.insert_one(item)
        # print(item["tags"])
