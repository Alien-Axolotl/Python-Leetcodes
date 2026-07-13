class Solution:
    def reverse(self, x: int) -> int:

        is_negative = 0

        if x < 0:
            is_negative = 1    
        num_str = str(abs(x))
        if is_negative == 1:
            num_str = "-" + num_str[::-1]
        else:    
             num_str = num_str[::-1] 
        if -2**31 <= int(num_str) <= 2**31 - 1:    
            return int(num_str)  
               
        return 0      


              
        
    

     
    

    
    
        


    
