class Solution:
    def reverse(self, x: int) -> int:
        if x >= 0:
            a = int(str(x)[::-1])
            return 0 if a > 2 ** 31  else a
        a = str(x)[1:][::-1]
        return 0 if int(a)*-1 < -2**31 else int(a)*-1