class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        result = []
        cur_pos = 0
        
        for i in range(len(num1)-1, -1, -1):
            carry = 0
            temp_res = 0
            pos = 1
            
            for j in range(len(num2)-1, -1, -1):
                prod = int(num1[i]) * int(num2[j])
                temp_res += (((prod % 10) + carry) * pos)
                carry = prod // 10
                pos *= 10
            
            temp_res += (carry*pos)
            result.append(temp_res* (10**cur_pos))
            cur_pos += 1
            
        print(result)
            
        return str(sum(result))
        