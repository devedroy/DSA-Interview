


class Solution:
    def majorityElement(self, nums):
        countMap = {}
        for n in nums:
            if n in countMap:
                countMap[n] += 1
            else:
                countMap[n] = 1
        res = nums[0]
        for k in countMap.keys():
            if countMap[k] >= countMap[res]:
                res = k
        return res

print(Solution().majorityElement([2,2,1,1,1,2,2]))