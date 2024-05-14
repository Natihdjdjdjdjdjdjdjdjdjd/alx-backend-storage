#!/usr/bin/env python3
'''Task 11's module.
'''


def schools_by_topic(mongo_collection, topic):
    """ returns the list of school having a specific topic """
    top_doc = mongo_collection.find({"topics": topic})
    return list(top_doc)
