"""
The code uses the classis dynamic programming to solve the problem
"""

class Solution:
    #allowed_symbol_set = {"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"}
    allowed_symbol_set = {i for i in range(65,91)}
    special_charset = {ord("*"),ord("?")}
    ord_star = ord("*")
    ord_query = ord("?")
    
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        
        if len(p) == 0:
            return True if len(s) == 0 else False
        elif len(p) != len(s) and "*" not in set(p):
            return False
        
        s = [ord(char) for char in s]
        p = [ord(char) for char in p]
        
        #status_arr = [[False for j in range(len(p)+1)] for i in range(len(s)+1)]
        status_arr = [[False]*(len(p)+1) for i in range(len(s)+1)]
        status_arr[0][0] = True
        for i in range(len(p)):
            if p[i] == Solution.ord_star:
                status_arr[0][i+1] = status_arr[0][i]
            
        for i in range(1,len(s)+1):
            for j in range(1,len(p)+1):
                if p[j-1] == Solution.ord_query or p[j-1] == s[i-1]:
                    status_arr[i][j] = status_arr[i-1][j-1]
                elif p[j-1] == Solution.ord_star:
                    status_arr[i][j] = status_arr[i-1][j] | status_arr[i][j-1]
                elif p[j-1] != s[i-1]:
                    status_arr[i][j] = False
                
        return status_arr[len(s)][len(p)]