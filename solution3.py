import numpy as np
from typing import List

class Node:
    def __init__(self, student_id, scores: List[int], next=None):
        self.student_id = student_id
        self.scores = scores
        self.next = next

class Solution3:
    def __init__(self):
        self.head = None

    def insert(self, student_id: int, scores: List[int]):
        new_node = Node(student_id, scores)
        new_addr = id(new_node)

        # Check if head node created(Empty LIst)
        if self.head is None:
            self.head = new_node
            return
        
        # Insert at head
        if new_addr < id(self.head):
            new_node.next = self.head
            self.head = new_node
            return
        
        # Iterate and insert
        current = self.head
        while current.next is not None and id(current.next) < new_addr:
            current = current.next

        # Find the ideal position and relink
        new_node.next = current.next
        current.next = new_node
    
    def search(self, target: int):
        current = self.head
        while current is not None:
            if current.student_id == target:
                return current.scores
            current = current.next

        return -1
        
