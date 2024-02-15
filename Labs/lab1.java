class Solution {
    public int[] twoSum(int[] nums, int target) {
        // Iterate over the numbers in the array.
        for (int i = 0; i < nums.length; i++) {
            // For each number, iterate over the rest of the numbers in the array.
            for (int j = i + 1; j < nums.length; j++) {
                // Check if the current two numbers add up to the target.
                if (nums[i] + nums[j] == target) {
                    // If they do, return their indices.
                    return new int[]{i, j};
                }
            }
        }
        // If no two numbers sum up to the target, return null.
        return null;
    }
}
