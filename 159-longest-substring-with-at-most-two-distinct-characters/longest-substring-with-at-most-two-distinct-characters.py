class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        freq = {}
        l = 0
        best = 0

        for r,ch in enumerate(s):
            freq[ch] = freq.get(ch,0)+1

            while len(freq) > 2:
                left_ch = s[l]
                freq[left_ch] -= 1
                if freq[left_ch] ==0:
                    del freq[left_ch]
                l += 1
            best = max(best,r-l+1)
        return best
        