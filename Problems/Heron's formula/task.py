import math

# S=# sqrt(p(p−a)(p−b)(p−c))

def heron_formula(a, b, c):
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))


input_a = int(input())
input_b = int(input())
input_c = int(input())
print(heron_formula(input_a, input_b, input_c))