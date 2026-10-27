

N = int(input())

i = N

while i <= 1000:

    if i % 4 == 0:
        i += N
        continue

    print(i, end=" ")

    i += N