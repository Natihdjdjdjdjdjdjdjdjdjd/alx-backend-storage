#!/usr/bin/env python3
"""
Caching request module
"""
import redis
import requests
from functools import wraps
from typing import Callable


def track_get_page(fn: Callable) -> Callable:
    """ Decorator for get_page
    """
    @wraps(fn)
    def my_apper(url: str) -> str:
        """ my_apper url's data is cache
        """
        client = redis.Redis()
        client.incr(f'count:{url}')
        cached_page = client.get(f'{url}')
        if cached_page:
            return cached_page.decode('utf-8')
        response = fn(url)
        client.set(f'{url}', response, 10)
        return response
    return my_apper


@track_get_page
def get_page(url: str) -> str:
    """ request to a given endpoint
    """
    response = requests.get(url)
    return response.text
