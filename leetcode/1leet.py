# https://leetcode.cn/problems/two-sum/description/

from typing import List


class Solution:
    # 方法一
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        for i in range(length - 1):
            for j in range(i + 1, length):
                if nums[i] + nums[j] == target:
                    return [i, j]

    # 方法二
    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        target_dict = {}
        for i in range(len(nums)):
            if (target - nums[i]) in target_dict:
                return [i, target_dict.get(target - nums[i])]
            target_dict[nums[i]] = i
        return []


if __name__ == '__main__':
    s = Solution()
    s.twoSum2([2, 7, 11, 15], 9)
