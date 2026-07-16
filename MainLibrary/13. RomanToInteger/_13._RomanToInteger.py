class Solution:
    def romanToInt(self, s: str) -> int:

        roman_to_int = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        
        intRoman = 0

        used = False

        for i in range(len(s)):
            if used:
                used = False
                continue
            else:
                if i + 1 < len(s) and roman_to_int[s[i]] < roman_to_int[s[i+1]]:
                    intRoman = intRoman + roman_to_int[s[i+1]] - roman_to_int[s[i]]
                    used = True
                else:
                    intRoman = intRoman + roman_to_int[s[i]]


        return intRoman            






                

            




