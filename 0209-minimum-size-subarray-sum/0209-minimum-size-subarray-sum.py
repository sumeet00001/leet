class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left=0
        ans= float('inf')
        curr=0
        for i in range(len(nums)):
            curr+=nums[i]
            while curr>=target:
                ans=min(ans,i-left+1)
                curr-=nums[left]
                left+=1
        return 0 if ans == float('inf') else ans