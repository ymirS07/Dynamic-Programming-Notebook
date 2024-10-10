class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        total = sum(nums)
        if total % 2 == 0:
            sub_total = total // 2
            if max(nums) > sub_total:
                return False
        else:
            return False
        
        dp = [0] * (sub_total + 1)
        for i in range(n):
            for j in range(sub_total, -1, -1):
                if nums[i] <= j:
                    dp[j] = max(dp[j], dp[j - nums[i]] + nums[i])
                else:
                    dp[j] = dp[j]
        
        if dp[sub_total] == sub_total:
            return True
        return False