class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]: 
        hashmap = {}

        for i in range(len(nums)):
            n = nums[i]
            diff = target - n 
            if diff in hashmap:
                return [hashmap[diff], i]
            else:
                hashmap[n] = i

