class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

                
        s1 = defaultdict(int)
        t1 = defaultdict(int)

        if len(s)!=len(t):
            return False
        
        for i in range(len(s)):
            s1[s[i]]+=1
            t1[t[i]]+=1

        if s1==t1:
            return True
        else:
            return False
        