class Solution:
    def generate(self, ind, ans, current, nums, n):
        ans.append(current.copy())
        for i in range(ind, n):
            if i > ind and nums[i] == nums[i - 1]:
                continue
            current.append(nums[i])
            self.generate(i + 1, ans, current, nums, n)
            current.pop()
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  
        ans = []
        self.generate(0, ans, [], nums, len(nums))
        return ans
