class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        res = []

        for s in spells:
            l = 0
            r = len(potions) - 1
            ind = len(potions)
            while l<=r:
                m = (l+r)//2
                if s*potions[m]>= success:
                    ind = m
                    r = m-1
                else:
                    l=m+1
            
            res.append(len(potions)-ind)
        return res


         