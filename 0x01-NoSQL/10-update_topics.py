#!/usr/bin/env python3
'''Task 10's module manggo opration'''


def update_topics(mongo_collection, name, topics):
    '''Changes all topics of a collection's document based on the name.
    '''
      my_query = {'name': name},
      add = {'$set': {'topics': topics}}

       mongo_collection.update_many(my_query, add)
