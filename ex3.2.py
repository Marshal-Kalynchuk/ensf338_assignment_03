import json
import timeit
import matplotlib.pyplot as plt


# Load the array and the list of search tasks
with open("ex2data.json", "r") as f:
    data = json.load(f)

with open("ex2tasks.json", "r") as f:
    tasks = json.load(f)

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
    
results = []
for task in tasks:

    t = timeit.Timer(lambda: binary_search(data, task, initial_midpoint=task))
    elapsed_time = t.timeit(number=10)
    results.append((task, elapsed_time))


# Extract task and elapsed time values from results
tasks, elapsed_times = zip(*results)

# Create new figure
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(1, 1, 1)

# Plot data
ax.scatter(tasks, elapsed_times)

# Add labels and title
ax.set_xlabel("Search Task")
ax.set_ylabel("Elapsed Time (s)")
ax.set_title("Binary Search Performance")

# Show plot
plt.show()