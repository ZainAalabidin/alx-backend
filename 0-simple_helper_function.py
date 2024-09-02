#!/usr/bin/env python3
'''module for helper functin
'''


def index_range(page: int, page_size: int) -> tuple:
    '''
    Returns a tuple containing a start index and an end index
    corresponding to the range of indexes to return in a list
    for the given pagination parameters.

    :param page: The page number (1-indexed).
    :param page_size: The number of items per page.
    :return: A tuple (start_index, end_index).
    '''
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return start_index, end_index
