class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        pair = [[p,s] for p , s in zip(position,speed)]
        stack = []

        for p,s in sorted(pair)[::-1]:

            stack.append((target-p)/s)

            if len(stack)>=2 and stack[-1]<=stack[-2]:
                stack.pop()
        return len(stack)

        # def carFleet(self, target, pos, speed):

        # time = [float(target - p) / s for p, s in sorted(zip(position, speed))]
        # res = cur = 0
        # for t in time[::-1]:
        #     if t > cur:
        #         res += 1
        #         cur = t
        # return res
          
        

