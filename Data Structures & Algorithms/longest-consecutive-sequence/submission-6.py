class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        longest = 0

        for num in seen:
            length = 0
            if (num-1) not in seen:
                length = 1
            while (num+length) in seen:
                length += 1
            longest = max(length, longest)
        return longest


        







    #   nums.sort()
    #   print(nums)
        # seen = set() # set has no duplicate values
        
        # for i in range(len(nums)):
        #     if nums[i] not in seen:
        #         seen.add(nums[i])
        #         #print(seen)      
        #     #convert set to array?
        #     arr = []
        #     for item in seen:
        #         arr.append(item)
        #         #print(arr)
        #     length = 0
        #     for j in range(len(nums)):
        #         if nums[j+1] - nums[j] == 1:
        #             length +=1
        #             print(length)
        #         else:
        #             break
        # return length

# For a given number x length of sequence ending at x = length of sequence ending at (x-1) + 1