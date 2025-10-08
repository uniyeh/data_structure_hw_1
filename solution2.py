import numpy as np
from typing import List

class Solution2:
    def __init__(self):
        self.datas = np.full(2**20, dtype=object)
    
    def insert(self, id: int, scores: List[int]):
        if self.datas[id] is not None:
            self.datas[id].extend(scores)
        else:
            self.datas[id] = scores
    
    def search(self, target: int) -> List[int]:
        result = self.datas[target]
        if result is None:
            return -1
        return self.datas[target]

