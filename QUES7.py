

import math

print("N\tN^2\tN^3\tSquare Root")

for n in range(1, 16):
    square = n * n
    cube = n * n * n
    root = math.sqrt(n)

    print(n, "\t", square, "\t", cube, "\t", f"{root:.4f}")