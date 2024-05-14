#!/usr/bin/env python3
""" let we  Operationsby mongodb with Python using pymongo """


def insert_school(mongo_collection, **kwargs):
    '''adds a new document in a collection.
    '''
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
