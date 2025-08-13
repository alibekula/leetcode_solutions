# Last updated: 13.08.2025, 16:56:19
class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        
        n = len(asteroids)
        min_asteroid, max_asteroid = min(asteroids), max(asteroids)
        buckets = [[] for _ in range(n)]

        if mass < min_asteroid:
            return False

        for asteroid in asteroids:

            if asteroid == max_asteroid:
                idx = n-1
            else:
                idx = ((asteroid - min_asteroid) * (n-1)) // (max_asteroid - min_asteroid)
            
            buckets[idx].append(asteroid)
        
        for bucket in buckets:
            min_val = min(bucket) if bucket else float('inf')
            for aster in bucket:
                if mass < min_val:
                    return False 
 
                mass += aster

        return True

        