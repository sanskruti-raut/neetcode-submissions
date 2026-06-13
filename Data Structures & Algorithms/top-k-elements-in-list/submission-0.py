class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        nums.sort()
        for i in range(len(nums)):
            if nums[i] not in hashmap:
                hashmap[nums[i]] = 1
            else:
                hashmap[nums[i]] += 1
        sorted_keys = sorted(hashmap, key=hashmap.get, reverse=True)
        return sorted_keys[:k]
    
        

        

