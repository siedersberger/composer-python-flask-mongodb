from stackapi import StackAPI
from datetime import date
from mongoDAO import ConnectionDAO, QuestionDAO

if __name__ == '__main__':

    my_db = ConnectionDAO(hostname='mongodb')
    my_collection = QuestionDAO(my_db.questions_collection)

    SITE = StackAPI('stackoverflow')
    SITE.page_size=100
    SITE.max_pages=50

    q = SITE.fetch('questions', fromdate=date(2019,4,1), todate=date(2019,4,30))

    for item in q["items"]:
        my_collection.add_question(item)
        # print(item["tags"])
