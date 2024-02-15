class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
    # Create a dictionary to store each element and its index
        num_dict = {}
        for i, num in enumerate(nums):
            num_dict[num] = i
                # Check if each element's complement (target - element) is in the dictionary
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_dict and num_dict[complement] != i:
                return [i, num_dict[complement]]
