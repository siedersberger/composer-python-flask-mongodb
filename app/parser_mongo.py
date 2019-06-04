from libdao.mongoDAO import ConnectionDAO, QuestionDAO
import operator

def parser_tags(selected_language):
    #identify all tags related with questions about python
    #append on a list these tags, except tags named python
    my_db = ConnectionDAO(hostname='mongodb')
    my_collection = QuestionDAO(my_db.db)

    quest = my_collection.find_tag(selected_language)
    questions_tags = []
    for item in quest:
        for tag in item["tags"]:
            if selected_language not in tag:
                questions_tags.append(tag)
    
    print("There are {} tags related with {}.".format(len(questions_tags),selected_language))
    return questions_tags

def rank_tags(selected_language):
    qtags = parser_tags(selected_language)
    tags_rank = {}
    for tag in qtags:
        if tag not in tags_rank:
            tags_rank[tag] = qtags.count(tag)

    return sorted(tags_rank.items(), key=operator.itemgetter(1), reverse=True) 


