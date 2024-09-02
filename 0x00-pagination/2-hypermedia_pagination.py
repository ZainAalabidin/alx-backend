#!/usr/bin/env python3
""" Pagination module
"""
import csv
import math
from typing import Dict, List, Tuple


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ Retrieves dataset for specific page
            - Args:
                - page: search page
                - page_size: size of each page
            - Return:
                - list of dataset for specified page
        """
        assert type(page) is int and type(page_size) is int
        assert page > 0 and page_size > 0
        start, end = index_range(page, page_size)
        dataset = self.dataset()
        return dataset[start: end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """ Returns page data plus info to next and prev pages
            - Args:
                - page: page to look for information
                - page_size: size of each page
            - Return:
                - dictionary of page_size, page, data, next page,
                  previous page and total_pages
        """
        dataset = self.dataset()
        total_pages = math.ceil(len(dataset) / page_size)
        prev_page, next_page = None, None
        if page < total_pages:
            next_page = page + 1
        if page > 1:
            prev_page = page - 1
        page_data = self.get_page(page, page_size)
        response = {'page_size': len(page_data),
                    'page': page,
                    'data': page_data,
                    'next_page': next_page,
                    'prev_page': prev_page,
                    'total_pages': total_pages}
        return response


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ Gets start and end indices of dataset
        - Args:
            - page: page to look for information
            - page_size: size of each page
        - Return:
            - tuple of start index and end index of each page
    """
    start_idx = (page - 1) * page_size
    end_idx = page * page_size
    return start_idx, end_idx
