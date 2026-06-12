class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for i in strs:
            sort_str = ''.join(sorted(i))
            if sort_str not in res:
                res[sort_str] = [i]
            else:
                res[sort_str].append(i)
        return list(res.values())
            
