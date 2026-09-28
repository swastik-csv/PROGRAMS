import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: list[int], capital: list[int]) -> int:
        # Combine capital and profits into a list of tuples and sort by capital required
        projects = sorted(zip(capital, profits))
        n = len(projects)
        i = 0
        max_heap = []
        
        # We can do at most k projects
        for _ in range(k):
            # Push all projects we can afford into the max heap (based on profit)
            while i < n and projects[i][0] <= w:
                # Use negative profit for max-heap behavior since heapq in Python is a min-heap
                heapq.heappush(max_heap, -projects[i][1])
                i += 1
            
            # If no projects can be afforded, break out early
            if not max_heap:
                break
            
            # Greedily pick the project with the maximum profit
            w += -heapq.heappop(max_heap)
            
        return w