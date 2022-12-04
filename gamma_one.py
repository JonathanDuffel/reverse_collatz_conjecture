def gamma_one(number):
    k = 1
    result = number
    while result % 6 != 1 or result % 6 != 5 or result == number:
        result = ((2**k) * number) - 1) // 3
        k += 1
    return result
