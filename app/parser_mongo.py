from main import my_db
import operator

def parser_tags(selected_language):
    #identify all tags related with questions about python
    #append on a list these tags, except tags named python
    quest = my_db.questions_collection.find({"tags":selected_language},{"tags": 1, "_id": 0})
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
        # print(tag)
        if tag not in tags_rank:
            tags_rank[tag] = qtags.count(tag)

    return sorted(tags_rank.items(), key=operator.itemgetter(1), reverse=True) 


