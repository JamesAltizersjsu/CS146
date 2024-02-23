from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = []
        n = len(nums)
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # Skip duplicates
            j, k = i + 1, n - 1
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                if sum == 0:
                    triplets.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1  # Skip duplicates
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1  # Skip duplicates
                    j += 1
                    k -= 1
                elif sum < 0:
                    j += 1
                else:
                    k -= 1
        return triplets

# Test the function
solution = Solution()
nums = [-5, 0, 5, 10, -10, 0]
res = solution.threeSum(nums)
print(res)
