# TIME LIMIT EXCEEDED during submission
# Runtime becomes O(n^2) due to line if nums[i] in counter:

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        counter = []
        for i in range(n):
            if nums[i] in counter:
                return True
            else:
                counter.append(nums[i])
        return False