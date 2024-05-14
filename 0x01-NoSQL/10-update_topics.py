#!/usr/bin/env python3
'''Task 10's module manggo opration'''


def update_topics(mongo_collection, name, topics):
     """ Changes all topics of a school document based on the name """
   my_ query = {"name": name}
    new_values = {"$set": {"topics": topics}}

    mongo_collection.update_many(my_query, new_values)
