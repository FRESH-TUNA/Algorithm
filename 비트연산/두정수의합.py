class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF
        INT_MAX = 0x7FFFFFFF
        
        a_bin = bin(a & MASK)[2:].zfill(32)
        b_bin = bin(b & MASK)[2:].zfill(32)
        
        result = []
        carry, _sum = 0, 0
        
        for i in range(32):
            A = int(a_bin[31 - i])
            B = int(b_bin[31 - i])
            
            # add 로 인해 발생한 carry
            Q1 = A & B
            
            # add로 인한 결과
            Q2 = A ^ B
            
            # 최종 자릿수 = add로 인한 결과 ^ 전자리수에서 발생한 carry
            _sum = carry ^ Q2
            
            # carry 발생조건 
            # 더해서 캐리가 발생 or 더한 결과값+전자릿수캐리에의해 캐리 발생
            Q3 = Q2 & carry 
            carry = Q1 | Q3
        
            result.append(str(_sum))
        if carry == 1: result.append('1')
            
        # 초과 자릿수 처리
        result = int(''.join(result[::-1]), 2) & MASK
        
        # 음수처리
        if result > INT_MAX: result = ~(result ^ MASK)
            
        return result
