#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
from typing import List, Dict

class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0"""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = 0, page_size: int = 10) -> Dict:
        """
        Returns a dictionary with pagination information.
        Args:
            index (int): Index of the first item in the current page.
            page_size (int): Number of items per page.
        Returns:
            Dict: Dictionary containing pagination info and current page data.
        """
        dataset = self.indexed_dataset()
        data_length = len(dataset)
        
        # Validate index
        if index < 0 or index >= data_length:
            raise AssertionError("Index out of range")

        data = []
        current_index = index
        for _ in range(page_size):
            while current_index in dataset and dataset[current_index] is None:
                current_index += 1
            if current_index in dataset:
                data.append(dataset[current_index])
                current_index += 1

        response = {
            'index': index,
            'page_size': len(data),
            'data': data,
            'next_index': current_index if current_index < data_length else None
        }

        return response
