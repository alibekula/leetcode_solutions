# Last updated: 12.09.2025, 03:07:00
from collections import defaultdict

class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        lan_map = {i+1: set(languages[i]) for i in range(len(languages))}

        troubled_users = set()
        for f1, f2 in friendships:
            if lan_map[f1].isdisjoint(lan_map[f2]):  
                troubled_users.add(f1)
                troubled_users.add(f2)

        if not troubled_users:
            return 0

        lans_count = [0] * (n+1)
        for user in troubled_users:
            for lan in lan_map[user]:
                lans_count[lan] += 1

        max_cover = max(lans_count)

        return len(troubled_users) - max_cover
