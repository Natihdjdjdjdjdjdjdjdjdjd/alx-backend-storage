#!/usr/bin/env python3
""" the operations with Python using pymongo """


def list_all(mongo_collection):
    """ show all documents in Python """
    docu = mongo_collection.find()

    if docu.count() == 0:
        return []

    return docu
