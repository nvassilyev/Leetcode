mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
                '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

def letterCombinations(digits): #DFS approach
    """
    :type digits: str
    :rtype: List[str]
    """
    
    solutions = []
    
    def backtrack(i, curr):
        if len(curr) == len(digits):
            solutions.append(curr)
            return
        
        for c in mapping[digits[i]]:
            backtrack(i+1, curr + c)
            
    if digits: 
        backtrack(0, "")
        
    return solutions

# def bfs_approach(digits):
#     for digits    

print(letterCombinations("23"))