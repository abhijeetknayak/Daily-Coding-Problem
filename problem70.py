def get_digits(a):
    digits = 0
    while a > 0:
        digits = digits + a % 10
        a = a // 10
    return digits

def return_perfect_number(a):
    digits = 10 - get_digits(a) # The digits should sum up to 10
    return (a * 10 + digits)

print(return_perfect_number(19))
print(return_perfect_number(23))
print(return_perfect_number(230))
print(return_perfect_number(3))

