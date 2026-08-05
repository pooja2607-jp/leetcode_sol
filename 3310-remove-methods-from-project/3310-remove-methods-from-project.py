from collections import deque

class Solution:
    def remainingMethods(self, n: int, k: int, invocations: list[list[int]]) -> list[int]:
        # Step 1: Build the adjacency list for the invocation graph
        graph = {i: [] for i in range(n)}
        for u, v in invocations:
            graph[u].append(v)
            
        # Step 2: Use BFS to find all suspicious methods reachable from k
        suspicious = {k}
        queue = deque([k])
        
        while queue:
            current = queue.popleft()
            for neighbor in graph[current]:
                if neighbor not in suspicious:
                    suspicious.add(neighbor)
                    queue.append(neighbor)
                    
        # Step 3: Verify if any external non-suspicious method invokes a suspicious method
        for u, v in invocations:
            if u not in suspicious and v in suspicious:
                # External method 'u' invokes suspicious method 'v' -> Cannot remove anything
                return list(range(n))
                
        # Step 4: If safe to remove, return only the remaining non-suspicious methods
        return [i for i in range(n) if i not in suspicious]
