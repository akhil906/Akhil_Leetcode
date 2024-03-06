class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        l = 0

        curr_sum = sum(nums[:k])
        avg_sum=curr_sum/k
        for i in range(k,len(nums)):
            curr_sum = curr_sum - nums[l]+nums[i]
            avg_sum = max(avg_sum,curr_sum/k)
            l = l+1
        return avg_sum


        