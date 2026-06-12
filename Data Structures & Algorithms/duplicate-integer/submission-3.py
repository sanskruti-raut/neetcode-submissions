# # BRUTE FORCE

# class Solution:
#     def hasDuplicate(self, nums: List[int]) -> bool:
#         for i in range(len(nums)):
#             for j in range(i,len(nums))
#                 if nums[i] == nums[i+1]
#                     return true
#         else:
#             return false      

# # SORT

# class Solution:
#     def hasDuplicate(self, nums: List[int]) -> bool:
#         x = nums.sort()
#         for i in range(len(nums)):
#                 if nums[i] == nums[i+1]
#                     return true
#         else:
#             return false   
# HASHMAP 


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for i in nums:
            if  i in hashset:
                 return True
            hashset.add(i)
        return False  

