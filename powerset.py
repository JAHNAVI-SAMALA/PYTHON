class Solution:
    def generate(self, ind, ans, current, nums, n):
        if ind == n:
            ans.append(current.copy())
            return
        current.append(nums[ind])
        self.generate(ind + 1, ans, current, nums, n)
        current.pop()
        self.generate(ind + 1, ans, current, nums, n)

    def subsets(self, nums) :
        ans = []
        current = []
        ind = 0
        n = len(nums)
        self.generate(ind, ans, current, nums, n)
        return ans
obj = Solution()
nums = list(map(int,input().split()))
print(obj.subsets(nums))


''' OUTPUTl
1 2 3 4
[[1, 2, 3, 4], [1, 2, 3], [1, 2, 4], [1, 2], [1, 3, 4], [1, 3], [1, 4], [1], [2, 3, 4], [2, 3], [2, 4], [2], [3, 4], [3], [4], []]
