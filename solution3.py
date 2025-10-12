import numpy as np
from typing import List

class Node:
    def __init__(self, student_id, scores: List[int], next=None):
        self.student_id = student_id
        self.scores = scores
        self.next = next

class Solution3:
    # Linked list sorted by memory address
    def __init__(self):
        # Initialize empty linked list
        self.head = None

    def insert(self, student_id: int, scores: List[int]):
        # Create new node
        new_node = Node(student_id, scores)
        new_addr = id(new_node)

        # Case 1: Empty list - set as head
        if self.head is None:
            self.head = new_node
            return

        # Case 2: Insert at head (smaller address than current head)
        if new_addr < id(self.head):
            new_node.next = self.head
            self.head = new_node
            return

        # Case 3: Find correct position in the list
        current = self.head
        # Traverse until we find insertion point
        while current.next is not None and id(current.next) < new_addr:
            current = current.next

        # Insert new node at correct position
        new_node.next = current.next
        current.next = new_node

    def search(self, target: int):
        # Linear search through linked list
        current = self.head
        while current is not None:
            # Check if current node matches target ID
            if current.student_id == target:
                return current.scores
            current = current.next

        # Student not found
        return -1

    def add_all_score(self):
        total = 0
        current = self.head
        # Traverse entire list
        while current is not None:
            if len(current.scores) >= 1:
                # Sum all scores for current student
                for score in current.scores:
                    total += score
            current = current.next
        return total

    def clean_up(self):
        # Clear linked list
        self.head = None