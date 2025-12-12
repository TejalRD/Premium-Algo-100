class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        n=len(s)
        net = 0

        for direction, amount in shift:
            if direction == 0:  #left
                net -= amount
            else:               # 1 = right
                net += amount
        k = net%n
        if k==0:
            return s
        return s[-k:]+s[:-k]
