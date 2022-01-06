class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] != 9:
            digits[-1] = digits[-1] + 1
            return digits
        a = ''
        for i in digits:
            a += str(i)
        return list(str(int(a)+1))
    