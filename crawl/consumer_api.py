import sys
sys.path.append('../')

from stackapi import StackAPI
from datetime import date
from libdao.mongoDAO import ConnectionDAO, QuestionDAO
from calendar import monthrange

def set_questions(year, month):
    ''' get a set of questions from StackAPI and store in data base (MongoDB)
    '''
    my_collection = QuestionDAO()

    SITE = StackAPI('stackoverflow')
    SITE.page_size=100
    SITE.max_pages=15

    first_day = 1
    last_day = monthrange(year, month)[1]

    q = SITE.fetch('questions', fromdate=date(year,month,first_day), todate=date(year,month,last_day))

    for item in q["items"]:
        my_collection.add_question(item)


if __name__ == '__main__':

    if len(sys.argv) > 1:
        month = int(sys.argv[1])
        year = int(sys.argv[2])
    else:
        month = 1
        year = 2019

    print("Data period setted: {}/{}".format(month,year))
    set_questions(year, month)
    
