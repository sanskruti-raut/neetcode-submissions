class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # while val in nums:
        #     nums.remove(val)
        # return len(nums)
        # TIME COMPLEXITY: O(N) + O(N) = O(N^2)
        # counter = 0
        # length = len(nums)
        # for i in range(length):
        #     if val == nums[i]:
        #         counter = counter + 1
        #         nums
        # return length - counter
        stack = []
        for i in range(len(nums)):
            if nums[i] != val:
                stack.append(nums[i])
        while len(nums) != 0:
            nums.pop()
        while len(stack) != 0:
            nums.append(stack.pop())
        return len(nums)

                            


