class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #CLARIFICATION QUESTIONS: 

        #BRUTE FORCE
        # Iterate through array using 2 nested loops to check all pairs of distinct indices 
        # If any pair of elements has the same value, return True
        # If all pairs are checked and no duplicates are found return false
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] == nums[j]:
        #             return True
        # return False
        # Time Complexity = O(n^2)
        # Space Complexity = O(1)

        #SORTING
        # Sort the array
        # Iterate through the array starting from index 1
        # Compare the current element with previous element
        # If both elements are equal, duplicate found - TRUE
        # If the loop finishes without detecting equal neighbors - FALSE

        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False
        # TIME COMPLEXITY = O(nlogn)
        # SPACE COMPLEXITY = O(1)





          





                     













        