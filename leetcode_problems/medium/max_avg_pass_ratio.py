import heapq

class Solution(object):
    def maxAverageRatio(self, classes, extraStudents):

        def _gain(p, t):
            return (p + 1) / (t + 1) - p / t

        # Store the gains with negative sign to use as MaxHeap
        # Store the gain, passed and total values as a tuple in the heap
        heap = [(- _gain(p, t), p, t) for p, t in classes]
        heapq.heapify(heap)

        for _ in range(extraStudents):
            g, p, t = heapq.heappop(heap)
            p, t = p + 1, t + 1
            heapq.heappush(heap, (- _gain(p, t), p, t))

        total = sum(p / t for _, p, t in heap)
        return total / len(classes)

def main():
    print(Solution().maxAverageRatio([[1,2],[3,5],[2,2]], 2))

main()