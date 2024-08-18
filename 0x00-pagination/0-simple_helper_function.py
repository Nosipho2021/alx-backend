#!/usr/bin/env python3
"""
Contains definition of index_range helper function
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Function that takes two integer arguments and returns a tuple of size two

    Args:
        page (int): page number to return (pages are 1-indexed)
        page_size (int): number of items per page

    Return:
        Tuple[int, int]: tuple containing the start and end index
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
