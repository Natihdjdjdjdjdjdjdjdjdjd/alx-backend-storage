#!/usr/bin/env python3
"""
Our Caching request module
"""
import redis
import requests
from functools import wraps
from typing import Callable


def our_page(fn: Callable) -> Callable:
    """ Decorator for get_page
    """
    @wraps(fn)
    def my_apper(url: str) -> str:
        """ my_apper url's data is cache
        """
        myclient = redis.Redis()
        myclient.incr(f'count:{url}')
        cached_page = myclient.get(f'{url}')
        if cached_page:
            return cached_page.decode('utf-8')
        response = fn(url)
        myclient.set(f'{url}', response, 10)
        return response
    return my_apper


@our_page
def get_page(url: str) -> str:
    """ request to a given endpoint
    """
    response = requests.get(url)
    return response.text
