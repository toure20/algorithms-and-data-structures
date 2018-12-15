# 22. Generate Parentheses
class Solution:
    # my recursive solution
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """ 
        ans = []
        self.helper(ans, [], n-1, n-1, 0, n)
        return ans
        
    def helper(self, ans, brackets, left, right, cur, n):
        if cur == 2*n-2:
            ans.append('(' + ''.join(brackets) + ')')
        if left > 0:
            brackets.append('(')
            self.helper(ans, brackets, left-1, right, cur+1, n)
            brackets.pop()
        if right > 0 and right >= left:
            brackets.append(')')
            self.helper(ans, brackets, left, right-1, cur+1, n)
            brackets.pop()

sol = Solution()
print(sol.generateParenthesis(2))