from dataclasses import dataclass, field
from typing import List
import random as rnd
import solution1 as s1
import solution2 as s2
import solution3 as s3
import time
import tracemalloc

@dataclass
class Student:
    id: int
    scores: List[int] = field(default_factory=list)

def _generate_random_inputs(amt: int) -> List[Student]:
    inputs = list()
    for i in range(2**amt):
        id = rnd.randint(1, 2**20 - 1)
        scores = list()
        scores_amt = rnd.randint(1, 3)
        for i in range(scores_amt):
            scores.append(rnd.randint(0, 100))
        
        inputs.append(Student(id, scores))

    return inputs

def _generate_random_requests() -> List[int]:
    requests = list()
    for i in range(1000000):
        requests.append(rnd.randint(1, 2**20 - 1))
    return requests

# Single process for testing
def _solution_routine(solution_class, count, inputs, requests):
    TIME_OUT = 600 # Time out after 10 minutes

    print(f"**Round {count} start**")

    # Get memory before creating solution and inserting
    current_before, peak_before = tracemalloc.get_traced_memory()

    # Create solution instance (this is where Solution2 allocates its big array)
    solution = solution_class()

    # Performance insert
    print("Insert start...")
    start_time = time.time()
    for i in inputs:
        solution.insert(i.id, i.scores)
        # Time out check
        if time.time() - start_time >= TIME_OUT:
              print(f"Insert timeout: over 10 minutes")
              return False
    end_time = time.time()
    print(f"Insert inputs: {end_time - start_time} seconds ")

    # Get memory after insert
    current_after, peak_after = tracemalloc.get_traced_memory()
    memory_diff = (current_after - current_before) / 1024 / 1024
    print(f"Memory used: {memory_diff:.2f} MB", flush=True)
    
    # Performance search
    # print("Search start...")  
    # start_time = time.time()
    # for request in requests:
    #     solution.search(request)
    #     # Time out check
    #     if time.time() - start_time >= TIME_OUT:
    #           print(f"Insert timeout: over 10 minutes")
    #           return True
    # end_time = time.time()
    # print(f"Search inputs: {end_time - start_time} seconds ")  
    
    # Add all scores
    # print("Add scores start...")
    # start_time = time.time()
    # total = solution.add_all_score()
    # # Time out check
    # end_time = time.time()
    # print(f"Add scores: {end_time - start_time} seconds - {total} ")
    # if end_time - start_time >= TIME_OUT:
    #     print(f"Add scores timeout: over 10 minutes")
    #     return False
    # Clean up current test data
    # solution.clean_up()
    print(f"**Round {count} end**")
    return True


def main():
    # Start memory tracking
    tracemalloc.start()

    print("Start generating random input...")
    inputList = list()
    for i in range(11, 26):
        inputList.append(_generate_random_inputs(i))
    print("Random input generated.")
    # print("Start generating random request...")
    # requests = _generate_random_requests()
    # print("Random requests generated.")
    requests = [0]
    print("Solution 1 ---------------------------------------")
    count = 11
    for inputs in inputList:
        success = _solution_routine(s1.Solution1, count, inputs, requests)
        if not success:
            break
        count += 1
    print("Solution 1 completed ---------------------------------------")
    print("Solution 2 ---------------------------------------")
    count = 11
    for inputs in inputList:
        success = _solution_routine(s2.Solution2, count, inputs, requests)
        if not success:
            break
        count += 1
    print("Solution 2 completed ---------------------------------------")
    print("Solution 3 ---------------------------------------")
    count = 11
    for inputs in inputList:
        success = _solution_routine(s3.Solution3, count, inputs, requests)
        if not success:
            break
        count += 1
    print("Solution 3 completed ---------------------------------------")
    
    # Stop memory tracking
    tracemalloc.stop()

if __name__ == "__main__":
    main()

