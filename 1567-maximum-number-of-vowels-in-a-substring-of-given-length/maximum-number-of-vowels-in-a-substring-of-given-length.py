class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        l = 0
        count = 0
        

        for i in s[:k]:

            if i == 'a' or i=='e' or i == 'i' or i=='o' or i=='u':
                count+=1
        print(f'{count}-{s[:k]}')
        maxcount = count
        for i in range(k,len(s)):
            print(s[i])
            if s[i] == 'a'or s[i] == 'e'or s[i] =='i'or s[i] =='o'or s[i] =='u':
                count+=1     
            if s[l] == 'a'or s[l] == 'e' or s[l] =='i'or s[l] =='o'or s[l] =='u':
                count = count-1
            
            maxcount = max(maxcount,count)
            l = l+1
        
        return maxcount
            






        

        
