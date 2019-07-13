#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates = sorted(candidates)
        nums = candidates[:]
        for num in candidates:
            if num > target:
                break
            if num == target:
                result.append([num])
                break
            subs = self.combinationSum(nums, target-num)
            if subs != []:
                for sub in subs:
                    sub.append(num)
                    result.append(sub)
            nums.remove(num)
        return result

        

