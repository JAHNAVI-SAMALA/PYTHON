class Solution:
    def generate(self,s,ind,n,ans,open,close):
        if(open>n):
            return
        if(open+close == 2*n and open==close):
            ans.append(s)
            return
        self.generate(s+"(",ind+1,n,ans,open+1,close)
        if(open>close):
            self.generate(s+")",ind+1,n,ans,open,close+1)

    def generateParenthesis(self, n) :
        ans = []
        ind = 0
        open = 0
        close = 0
        self.generate("",ind,n,ans,open,close)
        return ans
ob = Solution()
n= int(input())
print(ob.generateParenthesis(n))
