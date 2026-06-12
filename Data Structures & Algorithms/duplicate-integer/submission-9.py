class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Iterate through array using 2 nested loops to check all pairs of distinct indices 
        # If any pair of elements has the same value, return True
        # If all pairs are checked and no duplicates are found return false
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False



          





                     













        