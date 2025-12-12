class Solution:
    def confusingNumber(self, n: int) -> bool:
        map = {0:0, 1:1, 6:9, 9:6, 8:8}
        original = n
        rotated = 0

        while n>0:
            d = n%10
            if d not in map:
                return False
            rotated = rotated *10 + map[d]
            n //=10
        
        return rotated != original

        