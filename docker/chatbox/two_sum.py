import time

start_time = time.time_ns()


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        hist = {}
        for i, n in enumerate(nums):
            if target - n in hist:
                return [hist[target - n], i]
            hist[n] = i
            print(hist)


index = Solution()
index.twoSum([3, 2, 6, 8], 10)

print("Script Execution Time: %s " % (time.time_ns() - start_time))
