from libdao.mongoDAO import ConnectionDAO, QuestionDAO
import operator

def parser_tags(selected_tag):
    '''
        Identify all tags related with a input tag.
        After that, the tags found are appended on a list.
    '''
    my_db = ConnectionDAO(hostname='mongodb')
    my_collection = QuestionDAO(my_db.db)

    quest = my_collection.find_tag(selected_tag)
    questions_tags = []
    for item in quest:
        for tag in item["tags"]:
            if selected_tag not in tag:
                questions_tags.append(tag)
    
    print("There are {} tags related with {}.".format(len(questions_tags),selected_tag))
    return questions_tags

def rank_tags(selected_tag):
    '''
        From a list of tags related with a input tag, 
        it counts how many times the tag was related and append this information in another list.
        Finally, it returns this list sorted by number of relations found.
    '''
    qtags = parser_tags(selected_tag)
    tags_rank = {}
    for tag in qtags:
        if tag not in tags_rank:
            tags_rank[tag] = qtags.count(tag)

    return sorted(tags_rank.items(), key=operator.itemgetter(1), reverse=True) 


