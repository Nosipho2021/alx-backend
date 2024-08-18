#!/usr/bin/env python3
"""
Defines the Server class that paginates a database of popular baby names.
"""
import csv
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate the start and end index for a page of data.

    Args:
        page (int): The page no (1-indexed).
        page_size (int): The no of items per page.

    Returns:
        Tuple[int, int]: containing the start index and end index.
    """
    start = (page - 1) * page_size
    end = start + page_size
    return start, end


class Server:
    """Server class to paginate database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset

        Returns:
            List[List]: The dataset loaded from the CSV file.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Skip header row

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Retrieve a page of data from the dataset.

        Args:
            page (int): The page number (1-indexed). Must be a positive integer.
            page_size (int): The number of items per page. Must be a positive integer.

        Returns:
            List[List]: The lists containing the requested page of data.
                        Returns an empty list if the page is out of range.
        """
        assert isinstance(page, int) and page > 0, "page must be a positive integer"
        assert isinstance(page_size, int) and page_size > 0, "page_size must be a positive integer"

        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()

        # Handle out-of-range page
        if start_index >= len(dataset):
            return []

        return dataset[start_index:end_index]
