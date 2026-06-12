class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]: 
        #BRUTE FORCE
        # for i in range(len(nums)):
        #     for j in range(1,len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]
       
        # TIME COMPLEXITY: O(N^2)
        # SPACE COMPLEXITY: O(1)

        #Hashmap 
        hashmap = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hashmap:
                return [hashmap[diff], i]
            hashmap[nums[i]] = i

        

