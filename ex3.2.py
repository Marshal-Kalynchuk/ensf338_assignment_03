import json
import time
import matplotlib.pyplot as plt

with open("ex2data.json", "r") as f:
    data = json.load(f)

with open("ex2tasks.json", "r") as f:
    tasks = json.load(f)

def binary_search(arr, target, start, end, mid):
    if start > end:
        return False
    if target == arr[mid]:
        return True
    elif target < arr[mid]:
        return binary_search(arr, target, start, mid-1, (start+mid-1)//2)
    else:
        return binary_search(arr, target, mid+1, end, (mid+1+end)//2)
    
results = []

for task in tasks:
    start = 0
    end = len(data) - 1
    target = task
    best_mid = (start+end)//2
    min_time = float('inf')
    
    for mid in range(start, end+1):
        start_time = time.time()
        found = binary_search(data, target, start, end, mid)
        end_time = time.time()
        elapsed_time = end_time - start_time
        if elapsed_time < min_time:
            min_time = elapsed_time
            best_mid = mid
    
    print((target, best_mid))
    results.append((target, best_mid))


plt.scatter([x[0] for x in results], [x[1] for x in results])
plt.title("Initial Midpoints for Binary Search")
plt.xlabel("Search Task")
plt.ylabel("Initial Midpoint")
plt.show()