class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #s = "zxyzxyz"
        seen = set()
        l = 0
        r = 0
        length = 0
        max_length = 0
        while r<len(s):
                if s[r] not in seen:
                    seen.add(s[r])
                    max_length = max(max_length, r-l +1)
                    r += 1
                else:
                    #duplicate found
                    #shrink
                    seen.remove(s[l])
                    l += 1
        return max_length


            