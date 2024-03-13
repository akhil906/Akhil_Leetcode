class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # c = 0
        # l = 0
        # t = 0
        # maxc = 0
        # for i in range(len(nums)):
        #     if nums[i]==1:
        #         c+=1
        #     elif nums[i]==0 and t<k:
        #         c=c+1
        #         t=t+1
        #     elif nums[i]==0 and t>=k:
        #         t=0
        #         l = l+1
        #         c=c-1
        #     maxc = max(maxc,c)
        # return maxc
        # l = 0
        # r = 0
        # c = 0
        # t = 0
        # maxc = 0

        # while l<r and r<len(nums):
        #     if nums[r]==1:
        #         c+=1
        #     elif nums[r]==0 and t<k:
        #         c=c+1
        #         t=t+1
        #     elif nums[r]==0 and t>=k:
        #         t=0
        #         while nums[l]!=0:
        #             if nums[l]=


        #         l = l+1
        #         c=c-1 
        #     maxc = max(maxc,c)

        l = 0
        r = 0
        count = 0
        maxc = 0
        for r in range(len(nums)):
            if nums[r]==1:
                count+=1
            while (r-l+1)-count > k:
                if nums[l]==1:
                    count -= 1
                l+=1

            maxc = max(maxc,r-l+1)
        return maxc





            

            