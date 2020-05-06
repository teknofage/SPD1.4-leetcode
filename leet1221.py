class Solution:
    def balancedStringSplit(self, s: str) -> int:
  

        # example_3
        # "LLLRRR"
        # example output: "LLLRRR" OR "LR"

        # loop from left to right, maintaining balance of R and L 
        # if R>0 and L=R:
        # substring is valid.
        
        count = 0
        num_rs = 0
        num_ls = 0
        for i in list(s):
            if i == "R":
                num_rs += 1
            
                if num_rs == num_ls:
                    num_rs = 0
                    num_ls = 0 
                    count += 1
            elif i == "L":
                num_ls += 1
                if num_rs == num_ls:
                    num_rs = 0
                    num_ls = 0 
                    count += 1
                    
        return count
        