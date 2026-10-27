


N = int(input("Enter N: "))

for num in range(1, N + 1):

    temp = num
    digits = 0

    # Count digits
    while temp > 0:
        digits += 1
        temp = temp // 10

    temp = num
    total = 0

    # Calculate sum of digits raised to power 'digits'
    while temp > 0:
        digit = temp % 10
        total = total + digit ** digits
        temp = temp // 10

    if total == num:
        print(num)