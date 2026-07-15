class Solution:
    def intToRoman(self, num: int) -> str:

        roman = ""

        intRoman = num

        M = intRoman / 1000 

        roman = roman + "M" * int(M)

        intRoman = intRoman - (10**3)*int(M)


        C = intRoman / 100

        if int(C) == 4:
            roman = roman + "CD"
            intRoman = intRoman - (10**2)*int(C)
        elif int(C) == 9:
            roman = roman + "CM"
            intRoman = intRoman - (10**2)*int(C)    
        elif int(C) > 0:
            D = intRoman / 500
            roman = roman + "D" * int(D)
            intRoman = intRoman - (5*(10**2))*int(D)
            if int(D) == 1:
                C = C-5
            roman = roman + "C" * int(C)
            intRoman = intRoman - (10**2)*int(C)    


        X = intRoman / 10

        if int(X) == 4:
            roman = roman + "XL"
            intRoman = intRoman - (10**1)*int(X)
        elif int(X) == 9:
            roman = roman + "XC"
            intRoman = intRoman - (10**1)*int(X)
        elif int(X) > 0:
            L = intRoman / 50
            roman = roman + "L" * int(L)
            intRoman = intRoman - (5*(10**1))*int(L)
            if int(L) == 1:
                X = X-5
            roman = roman + "X" * int(X)
            intRoman = intRoman - (10**1)*int(X)               

        I = intRoman

        if I == 4:
            roman = roman + "IV"
        elif I == 9:
            roman = roman + "IX"
        elif I > 0:
            V = intRoman / 5
            roman = roman + "V" * int(V)
            if int(V) == 1:
                I = I-5
            roman = roman + "I" * int(I)
            intRoman = intRoman - (10**0)*int(V)     

                   


        

        return roman