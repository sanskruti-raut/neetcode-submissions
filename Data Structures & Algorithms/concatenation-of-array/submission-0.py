class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        #Initialize an empty array
        #Use the loop twice
        #Inside the loop, iterate through every element num in the input array nums
        #Append num to the result list or assign it to the next available index in the array
        #Return the resulting array
        ans = [] #Size = 2n
        for i in range(2):
            for num in nums:
                ans.append(num)
        return ans
