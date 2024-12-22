class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
  
        # if len(s)>1:
        #     l , r = 0,1

        #     s1 = set()
        #     s1.add(s[l])
        #     # print(s1)
        #     maxl = 1
        #     while r <len(s) and l < len(s)-1:
        #         if s[r] not in s1:
        #             maxl = max(maxl,r-l+1)
        #             print(maxl)
        #             s1.add(s[r])
        #             print(s1)
        #             r = r+1
        #         else:
        #             l = l+1
        #             r = l
        #             s1.clear()
        #             s1.add(s[l])
        #         # r = r+1
            
        #     return maxl
        # else:
        #     return len(s)
        

        charset = set()

        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charset:
                charset.remove(s[l])
                l += 1
            charset.add(s[r])
            res = max(res,r-l+1)
        return res



         

        
