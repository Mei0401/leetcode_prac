#
# @lc app=leetcode id=18 lang=python3
#
# [18] 4Sum
#
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4: return []
        nums = sorted(nums)
        result = []
        checked_1 = []
        for first in range(len(nums)-3):
            checked_2 = []
            if nums[first] in checked_1:
                continue
            checked_1.append(nums[first])
            for second in range(first+1, len(nums)-2):
                if nums[second] in checked_2:
                    continue
                checked_2.append(nums[second])
                third = second + 1
                forth = len(nums)-1
                need = target - nums[first] - nums[second]
                while third < forth:
                    if need == nums[third] + nums[forth]:
                        result.append([nums[first], nums[second], nums[third], nums[forth]])
                        while third < forth and nums[third] == nums[third+1]:
                            third += 1
                        while third < forth and nums[forth] == nums[forth-1]:
                            forth -= 1
                        if forth - third == 1:
                            break
                        third, forth = third+1, forth-1
                    elif need > nums[third] + nums[forth]:
                        third += 1
                    else:
                        forth -= 1
        return result


        

        

