class Solution:
    def maximum69Number (self, num: int) -> int:
        # convert num into a list of strings
        # iterate over the num list
        # if num[i] is 6, replace it with 9
        # convert the list to int and return
        
        num_list = list(str(num))
        
        for i in range(len(num_list)):
            if num_list[i] != '9':
                num_list[i] = '9'
                break
        
        return int("".join(num_list))
