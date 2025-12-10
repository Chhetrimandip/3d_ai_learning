import numpy as np
import math

# --- 1. Define Vectors ---
# Vectors are just lists of [x, y, z]
# Think of 'a' as "Looking Forward"
vector_a = [1, 0, 0] 

# Think of 'b' as "Looking 45 degrees to the Left"
vector_b = [1, 1, 0]
def manual_dot_product (a,b):
    answer = 0
    for i in range(0,2):
        answer += a[i]*b[i]
    return answer
def manual_cross_product (a,b):
    answer = []
    ast = a[1]*b[2]-a[2]*b[1]
    bst = a[2]*b[0]-a[0]*b[2]
    cst = a[0]*b[1]-a[1]*b[0]
    answer.append(ast)
    answer.append(bst)
    answer.append(cst)
    return answer

# 1. Dot Product
my_dot = manual_dot_product(vector_a, vector_b)
np_dot = np.dot(vector_a, vector_b)
print(f"Dot Product (My Code): {my_dot}")
print(f"Dot Product (Numpy):   {np_dot}")

# 2. Cross Product
my_cross = manual_cross_product(vector_a, vector_b)
np_cross = np.cross(vector_a, vector_b)
print(f"\nCross Product (My Code): {my_cross}")
print(f"Cross Product (Numpy):   {np_cross}")

# Check
if my_dot == np_dot and np.array_equal(my_cross, np_cross):
    print("\nSUCCESS: You understand the physics of 3D space.")
else:
    print("\nFAILURE: Check your math formulas.")