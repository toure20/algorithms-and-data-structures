# 91. Decode Ways
class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0' or '00' in s: return 0
        
        dp = [1, 1]
        for i in range(len(s)-1):
            if s[i] == '0' or s[i+1] == '0':
                if int(s[i]) >= 3:
                    return 0
                dp.pop()
                dp.append(dp[-1])
            elif int(s[i:i+2]) > 26:
                dp.append(dp[-1])
            else:
                dp.append(dp[-2]+dp[-1])
                
        return dp[-1]

    def numDecodings(self, s: str) -> int:
        if s[0] == '0': return 0
        
        dp1 = dp2 = 1
        for i in range(1, len(s)):
            if s[i] == '0' and (s[i-1] == '0' or s[i-1] >= '3'): return 0
            
            if s[i] == '0':
                dp1, dp2 = dp2, dp1
            elif '10' <= s[i-1:i+1] <= '26':
                dp1, dp2 = dp2, dp1+dp2
            else:
                dp1, dp2 = dp2, dp2
        
        return dp2
            
                
            