import numpy as np
from typing import List

class Solution2:
    # Direct addressing: use student ID as array index for O(1) access
    def __init__(self):
        # Create array with 2^20 slots, all initialized to None
        self.datas = np.full(2**20, None, dtype=object)

    def insert(self, id: int, scores: List[int]):
        # Check if student already exists
        if self.datas[id] is not None:
            # Append new scores to existing list
            self.datas[id].extend(scores)
        else:
            # Create new scores list for this student
            self.datas[id] = scores

    def search(self, target: int) -> List[int]:
        # Direct access using ID as index
        result = self.datas[target]
        if result is None:
            return -1
        return self.datas[target]

    def add_all_score(self):
        total = 0
        # Iterate through all slots in the array
        for data in self.datas:
            if data is not None:
                # Sum all scores for this student
                for score in data:
                    total += score
        return total

    def clean_up(self):
        # Reset array to all None values
        self.datas = np.full(2**20, None, dtype=object)