import numpy as np
from typing import List

class Solution2():
    def __init__(self):
        self.datas = np.empty(2**20, dtype=List[int])
    
    def insert(self, id: int, scores: List[int]):
        if self.datas[id] != None:
            self.datas[id].extend(scores)
        else:
            self.datas[id] = scores
    
    def search(self, target: int) -> List[int]:
        pass