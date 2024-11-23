'''
 * 1. Two Sum
 * 
 * Given an array of integers nums and an integer target, return
 *  indices of the two numbers such that they add up to target.
 *
 * You may assume that each input would have exactly one solution,
 *  and you may not use the same element twice.
 *
 * You can return the answer in any order.
 *
 * Example 1:
 * Input: nums = [2,7,11,15], target = 9
 * Output: [0,1]
 * Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
 *
 * Example 2:
 * Input: nums = [3,2,4], target = 6
 * Output: [1,2]
 *
 * Example 3:
 * Input: nums = [3,3], target = 6
 * Output: [0,1]
 *
 * Constraints:
 * 2 <= nums.length <= 104
 * -109 <= nums[i] <= 109
 * -109 <= target <= 109
 *
 * Only one valid answer exists.
 *
 * Follow-up: Can you come up with an algorithm that is less than O(n^2) time complexity?
'''
class TwoSum:
    @staticmethod
    def run():
        nums = [2, 7, 11, 15]
        target = 9
        result = TwoSum.two_sums(nums, target)
        print(f"TwoSum result {result}")
        result = TwoSum.two_sums_optimized(nums, target)
        print(f"TwoSum optimized result: {result}")

    @staticmethod
    def two_sums(nums, target):
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue

                if nums[i] + nums[j] == target:
                    return [i, j]

        raise Exception("Did not find result!")

    @staticmethod
    def two_sums_optimized(nums, target): 
        indicies = {}
        for i, num in enumerate(nums):
            needed = target - num
            if needed in indicies:
                return [indicies[needed], i]
            
            indicies[num] = i

        raise Exception("Did not find result!")