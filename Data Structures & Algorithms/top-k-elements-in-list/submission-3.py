class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            if nums[i] not in hashmap:
                hashmap[nums[i]] = 1
            else:
                hashmap[nums[i]] += 1
        arr = []
        for key in hashmap:
            arr.append([hashmap[key],key])
            #print(arr)
        arr.sort()
        res = []
        for i in range(len(arr)-1, (len(arr)-1)-k, -1):
            #res.append(arr[][])
            res.append(arr[i][1])
            #print(res)
        return res
            
        


        # sorted_keys = sorted(hashmap, key=hashmap.get, reverse=True)
        # for 
        # return sorted_keys[:k]
    
        

        

