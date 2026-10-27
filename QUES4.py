

n = int(input("Enter a positive integer: "))

original = n

if n == 0:
    octal = "0"
else:
    octal = ""

    while n > 0:
        remainder = n % 8
        octal = str(remainder) + octal
        n = n // 8

print("Octal Equivalent =", octal)