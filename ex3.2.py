import json
from urllib.request import urlopen
import timeit
import matplotlib.pyplot as plt

with urlopen('https://raw.githubusercontent.com/ldklab/ensf338w23/main/assignments/assignment3/ex2data.json') as inUrl:
    data = json.load(inUrl)

with urlopen('https://raw.githubusercontent.com/ldklab/ensf338w23/main/assignments/assignment3/ex2tasks.json') as inUrl:
    tasks = json.load(inUrl)

def binary_search(array, target, start=0, end=None, initial_midpoint=None):
    """Perform binary search on array to find target.
    Assumes array is sorted.
    Returns True if target is found, False otherwise.
    """
    if end is None:
        end = len(array) - 1

    while start <= end:
        if initial_midpoint is None:
            mid = start + (end - start) // 2
        else:
            mid = initial_midpoint
            initial_midpoint = None
        
        if array[mid] == target:
            return True
        elif array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return False
    


times = []
times = [timeit.timeit(lambda: binary_search(data, task, initial_midpoint=task), number=100) for task in tasks]

# Create new figure
fig = plt.figure(figsize=(8, 6))


# Plot data
plt.subplot(1, 2, 1)
plt.scatter(range(len(tasks)), times)

# Add labels and title
plt.xlabel("Search Task")
plt.ylabel("Elapsed Time (s)")
plt.title("Elapsed binary search time per task")

plt.subplot(1, 2, 2)
plt.scatter(range(len(tasks)), tasks)
# Add labels and title
plt.xlabel("Search Task")
plt.ylabel("Chosen midpoint")
plt.title("Chosen midpoint per task")


# Show plot
plt.show()