class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed = [0]+flowerbed+[0]
        stack = []
        i = 0
        zc = 0
        while n>0 and i<len(flowerbed):
                
            if flowerbed[i]==0:
                zc = zc + 1
            else:
                zc = 0     
            if zc == 3:
                n = n-1
                zc = zc-2
            i = i+1
        if n == 0:
            return True
        else:
            return False 




         
        