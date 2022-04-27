class Solution:
    def reverse(self, x: int) -> int:
        if x >= 0:
            revPos = int(str(x)[::-1])
            return revPos if revPos <= ((2**31)-1) else 0
        revNeg = int((str(x)[1:])[::-1])*-1
        return revNeg if revNeg >= -2**31 else 0