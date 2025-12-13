class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def reverse(left,right):
            while left<right:
                s[left],s[right] = s[right],s[left]
                left += 1
                right -=1
        n = len(s)
        reverse(0,n-1)  #reverse the whole array

        start = 0
        for i in range(n+1):
            if i==n or s[i]==" ":   
                reverse(start,i-1)      #reverse the words
                start = i+1

