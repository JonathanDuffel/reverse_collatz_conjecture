def gamma_function(number):
    steps = 0
    result = number
    while result % 6 != 3:
        if result % 6 == 1:
            result = ((4*result)-1)//3
        elif result % 6 == 5:
            result = ((2*result)-1)//3
        steps += 1
    return result, steps
