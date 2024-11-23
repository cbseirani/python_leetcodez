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