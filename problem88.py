def divide(dividend, divisor):
    quotient = 0
    if divisor == 0: return None
    while dividend - divisor >= 0:
            dividend = dividend - divisor
            quotient += 1
    return quotient


print(divide(120, 12))
print(divide(1234, 23))
