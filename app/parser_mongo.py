import operator
from libdao.mongoDAO import QuestionDAO

class ParserTags:

    def __init__(self):
        self.__question_dao = QuestionDAO()

    def get_related_tags(self, selected_tag):
        '''
            Identify all tags related with a input tag.
            After that, the tags found are appended on a list.
        '''
        quest = self.__question_dao.find_tag(selected_tag)
        questions_tags = []
        for item in quest:
            for tag in item["tags"]:
                if selected_tag not in tag:
                    questions_tags.append(tag)
        
        print("There are {} tags related with {}.".format(len(questions_tags),selected_tag))
        return questions_tags

    def rank_tags(self, selected_tag):
        '''
            From a list of tags related with a input tag, 
            it counts how many times the tag was related and append this information in another list.
            Finally, it returns this list sorted by number of relations found.
        '''
        qtags = self.get_related_tags(selected_tag)
        tags_rank = {}
        for tag in qtags:
            if tag not in tags_rank:
                tags_rank[tag] = qtags.count(tag)

        return sorted(tags_rank.items(), key=operator.itemgetter(1), reverse=True) 

    def count_tags(self):
        tags_counted = {}
        all_documents = self.__question_dao.find_all_documents()
        for document in all_documents:
            for tag in document["tags"]:
                if tag not in tags_counted:
                    tags_counted[tag] = self.__question_dao.find_tag(tag).count()

        return sorted(tags_counted.items(), key=operator.itemgetter(1), reverse=True) 
