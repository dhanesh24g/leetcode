myMap = {"Dhanesh": 32}
print(myMap)

myMap["Parveen"] = 30
print(myMap)

# Tuples - Similar to Arrays but immutable
tup = (1,2,4)
print(tup[-1])

# Cannot modify a tuple
#tup[0] = 11

# Heap implementation
import heapq

heap = []
heapq.heappush(heap,22)
heapq.heappush(heap,31)
heapq.heappush(heap,67)
heapq.heappush(heap,21)
heapq.heappush(heap,3)
print(f"Heap: ", heap)

# The minimum value is always at index 0
heapq.heappop(heap)
print(f"Heap: ", heap)



# ln = len(nums)
# if target > nums[ln / 2]:
#     searchInsert(ln / 2 + 1, ln)
# elif target < nums[ln / 2]:
#     searchInsert(0, ln / 2 - 1)
# else:
#     return ln / 2
# return