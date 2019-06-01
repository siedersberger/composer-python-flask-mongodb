import requests
import json
import time
from stackapi import StackAPI
from datetime import date
from connect_mongo import questions_collection



if __name__ == '__main__':

    SITE = StackAPI('stackoverflow')
    SITE.page_size=100
    SITE.max_pages=10

    q = SITE.fetch('questions', fromdate=date(2019,4,1), todate=date(2019,4,30), tagged='python')

    for item in q["items"]:
        questions_collection.insert_one(item)
        print(item["tags"])
     
    

    
    
    # q = comments_collection.find(
    #     {
    #         "items.tags":"python"
    #     }
    # )
    # print(q)
   
