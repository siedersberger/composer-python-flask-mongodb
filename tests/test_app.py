import sys
sys.path.append('../')

from app.parser_mongo import rank_tags
from libdao.mongoDAO import ConnectionDAO, QuestionDAO
from unittest import TestCase, main

class TestApp(TestCase):

    def setUp(self):
        self.connection = ConnectionDAO()
        self.collection = QuestionDAO(self.connection.db)

    def test_evaluated_if_document_is_added_to_db(self):

        toptal_before_add = self.collection.questions_collection.count_documents({})
        item = {"question_id":12345}
        self.collection.add_question(item)
        toptal_after_add = self.collection.questions_collection.count_documents({})

        self.assertEqual(toptal_after_add,(toptal_before_add+1),"Document is not being added in data base.")

    def test_verify_if_db_isnot_empty(self):

        total = self.collection.questions_collection.count_documents({})
        self.assertNotEqual(total,0,"The collection is empty")


if __name__ == '__main__':
    main()