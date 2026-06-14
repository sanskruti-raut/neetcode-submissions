class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        seen = set(nums) #{1,2,4} 
        high = max(nums) + 1
        low = 1

        miss = 1
        for i in range(low, (high+1)): #[1,2,3,4,5]
            if i not in seen:
                miss = i
                break
        return miss




