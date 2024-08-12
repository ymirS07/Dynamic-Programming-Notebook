class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp_list = [1] * len(nums)
        for i, num in enumerate(nums):
            for j in range (i):
                    if nums[j] < nums[i]:
                        dp_list[i] = max(dp_list[i], dp_list[j]+1)
            
        return max(dp_list)
