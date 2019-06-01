from connect_mongo import questions_collection
import operator

def parser_tags():
    #identify all tags related with questions about python
    #append on a list these tags, except tags named python
    quest = questions_collection.find({},{"tags": 1, "_id": 0})
    questions_tags = []
    for item in quest:
        for tag in item["tags"]:
            if 'python' not in tag:
                questions_tags.append(tag)
    
    #print("There are {} tags related with python.".format(len(questions_tags)))
    return questions_tags

def rank_tags():
    qtags = parser_tags()
    tags_rank = {}
    for tag in qtags:
        # print(tag)
        if tag not in tags_rank:
            tags_rank[tag] = qtags.count(tag)

    return sorted(tags_rank.items(), key=operator.itemgetter(1), reverse=True) 


