# Last updated: 10.10.2025, 14:19:04
class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        
        n = len(energy)
        dp = [float('-inf')] * n
        dp = dp + [0] * k
        max_energy = float('-inf')

        for i in range(n-1, -1, -1):
            
            dp[i] = energy[i] + dp[i + k]
            max_energy = max(max_energy, dp[i])

        return max_energy

