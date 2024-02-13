class Solution(object):
    def singleNumber(self, nums):
        result = 0
        for num in nums:
            result ^= num
        return result

nums = [7, 3, 4, 3,4]
sol = Solution()
print(sol.singleNumber(nums))
