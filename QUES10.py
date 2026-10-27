


N = int(input("Enter an odd number: "))

mid = N // 2

# Upper half (including middle row)
for i in range(mid + 1):
    
    for j in range(mid - i):
        print(" ", end="")
        
    for j in range(2 * i + 1):
        print("*", end="")
        
    print()

# Lower half
for i in range(mid - 1, -1, -1):
    
    for j in range(mid - i):
        print(" ", end="")
        
    for j in range(2 * i + 1):
        print("*", end="")
        
    print()