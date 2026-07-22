class Solution:
    def hammingWeight(self, n: int) -> int:

        total = 0

        bitlength = n.bit_length()

        for i in range(bitlength-1 , -1 , -1):
            temp = 1 << i

            if (i & temp) != 0:
                total = total+1

        return total        
        
