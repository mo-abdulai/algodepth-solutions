class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        minHeap = []

        for x, y in points:
            
            distance = (x ** 2) + (y ** 2)

            heapq.heappush(minHeap, (-distance, x, y))

            if len(minHeap) > k:
                heapq.heappop(minHeap)
        

        result = []

        for _, x, y in minHeap:
            result.append([x, y])
        
        return result

        