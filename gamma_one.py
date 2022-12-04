def gamma_one(number):
    k = 0
    result = number
    while result % 6 != 3 or result == number:
        k += 1
        result = (((2**k) * number) - 1) // 3
    return result, k
