#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        nums = candidates[:]
        for num in candidates:
            if num == target:
                result.append([num])
                continue
            if num < target:
                nums.remove(num)
                subs = self.combinationSum2(nums, target-num)
                if subs != []:
                    for sub in subs:
                        sub.append(num)
                        result.append(sub)
                # nums.remove(num)
        return result

