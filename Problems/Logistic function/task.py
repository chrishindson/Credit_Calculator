import math

def log_function(x):
    return round(1 / (1 + math.exp(-x)), 2)


input_x = int(input())
print(str(log_function(input_x)))