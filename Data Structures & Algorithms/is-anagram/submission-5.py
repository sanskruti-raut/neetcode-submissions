class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #SORTING
        if len(s) != len(t):
            return False
        if sorted(s) == sorted(t):
            return True
        else:
            return False

        #TIME COMPLEXITY: O(nlogn + mlogm)
        #SPACE COMPLECITY: O(1)


        