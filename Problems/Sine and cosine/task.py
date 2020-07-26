import math

def sind_diff(inp_val):
    sine = math.sin(inp_val)
    cosine = math.cos(inp_val)
    return sine - cosine
    
    
user_input = float(input())
print(sind_diff(user_input))
