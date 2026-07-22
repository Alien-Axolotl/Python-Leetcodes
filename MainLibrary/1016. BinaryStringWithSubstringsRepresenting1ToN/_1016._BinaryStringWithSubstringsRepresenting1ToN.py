class Solution:
    def queryString(self, s: str, n: int) -> bool:


        def to_binary(n: int) -> str:
            if n == 0:
                return "0"
            if n < 0:
                return "-" + to_binary(abs(n))

            bit_len =n.bit_length()
            result = []

            for i in range(bit_len - 1 , -1 , -1):
                temp = 1 << i

                if (n & temp) != 0:
                    result.append("1")
                else:
                    result.append("0")
            return "".join(result)


       

        for i in range(1 , n+1):
            if to_binary(i) in s:
                continue
            else:
                return False
        return True            


            
            

        
