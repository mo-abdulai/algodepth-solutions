class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        maxHeap = []

        for x, y in points:
            distance = (x ** 2) + (y ** 2)

            heapq.heappush(maxHeap, (-distance, x, y))

            if len(maxHeap) > k:
                heapq.heappop(maxHeap)
            
        result = []
        for _, x, y in maxHeap:
            result.append([x, y])
    
        return result