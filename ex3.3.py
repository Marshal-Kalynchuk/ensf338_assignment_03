import sys

lst = []
prev_size = sys.getsizeof(lst)
for i in range(64):
    lst.append(i)
    curr_size = sys.getsizeof(lst)
    if curr_size != prev_size:
        print(f"Capacity changed from {prev_size} bytes to {curr_size} bytes at index {i}")
        prev_size = curr_size
