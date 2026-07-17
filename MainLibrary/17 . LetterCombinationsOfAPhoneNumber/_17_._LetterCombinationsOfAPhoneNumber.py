class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return[]

        LetterList = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }

        PossibleCombinations = [""]

        for digit in digits:
            Next = [""]
            for existing_combo in PossibleCombinations:
                for letter in LetterList[digit]:
                    Next.append(existing_combo + letter)
            PossibleCombinations = Next

            


        return PossibleCombinations          
            
        
