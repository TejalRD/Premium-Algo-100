class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        m,n= len(s), len(t)
        if m>n:
            return self.isOneEditDistance(t,s)
        if n-m >1:
            return False
        
        if m==n:
            diff = 0
            for i in range(m):
                if s[i] != t[i]:
                    diff +=1
                    if diff >1:
                        return False
            return diff == 1
        i=0
        while i<m and s[i] == t[i]:
            i+=1
        
        return s[i:] == t[i+1:]
        