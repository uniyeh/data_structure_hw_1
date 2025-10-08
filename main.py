import numpy as np
import random as rnd
from dataclasses import dataclass, field
from typing import List

@dataclass
class Student:
    id: int
    scores: List[int] = field(default_factory=list)

class Solution1():
    def __init__(self):
        self.capacity = 1
        self.datas = np.empty(self.capacity, dtype=object)
        self.current_usage = 0

    def insert(self, id: int, scores: List[int]):
        # Check if any element added
        if self.current_usage == 0:
            self._add_new(0, id, scores)
            return

        # Find the correct position to insert
        pos = _binary_search(self.datas, 0, self.current_usage - 1, id)
        
        # If student exists, add scores
        if pos < self.current_usage and self.datas[pos].id == id:
            self.datas[pos].scores.extend(scores)
            return
        
        # Otherwise, add new student at pos
        if self.current_usage + 1 > self.capacity:
            self._resize()
        self._add_new(pos, id, scores)
    
    def search(self, target: int) -> List[int]:
        # id=1 will always be at the first index => return datas[1] directly
        if target == 1:
            return self.datas[0].scores
        
        # Search for target data
        idx = _binary_search(self.datas, 0, self.current_usage - 1, target)
        if idx < self.current_usage and self.datas[idx].id == target:
            return self.datas[idx].scores

        # Return -1 is there is no score     
        return -1

    def _resize(self):
        # Expand array
        self.capacity *= 10
        new_arr = np.empty(self.capacity, dtype= object)
        
        # Copy all data to new arrary
        for i in range(len(self.datas)):
            new_arr[i] = self.datas[i]
        
        self.datas = new_arr
    
    def _add_new(self, pos: int, id: int, scores: List[int]):
        # Shift the elements to the right to make space for a new value if there is any element existed
        if self.current_usage > 0:
            for i in range(self.current_usage, pos, -1):
                self.datas[i] = self.datas[i-1]

        # Add new element
        self.datas[pos] = Student(id, scores)
        self.current_usage += 1
    
class Solution2():
    def __init__(self):
        self.datas = np.empty(2**20, dtype=List[int])
    
    def insert(self, id: int, scores: List[int]):
        if self.datas[id] != None:
            self.datas[id].extend(scores)
        else:
            self.datas[id] = scores
    
    def search(self, target: int) -> List[int]:
        

def _binary_search(arr, left, right, target):
    if right >= left:
        mid = left + (right - left) // 2

        if arr[mid].id == target:
            return mid
        elif target < arr[mid].id:
            return _binary_search(arr, left, mid - 1, target)
        else:
            return _binary_search(arr, mid + 1, right, target)
    
    else:
        return left

def _generate_random_inputs(amt: int) -> List[Student]:
    inputs = list()
    for i in range(amt):
        id = rnd.randint(1, 2**20)
        scores = list()
        scores_amt = rnd.randint(1, 3)
        for i in range(scores_amt):
            scores.append(rnd.randint(0, 100))
        
        inputs.append(Student(id, scores))

    return inputs

def main():
    print("Hello, World!")


if __name__ == "__main__":
    main()
