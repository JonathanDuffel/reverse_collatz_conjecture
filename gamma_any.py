def gamma_one(number, desired_mod):                             # Returns next gamma element of given mod6
    k = 1
    result = number
    while result % 6 not in desired_mod or result == number:    # Gamma sequence must not have repeating elements
        result = (((2**k) * number) - 1) // 3                   # Reverse collatz equation
        k += 1                                                  # Incriment k until the result is a desired mod6
    return result
        
def gamma_any(number, steps):                                   # Returns gamma sequence after a given number in given steps
    gamma_sequence = [number]
    threemodsix = False
    while not threemodsix:                                      # Runs repeatedly until number is 3mod6
        if steps == 1:
            number = gamma_one(number, [3])                     # Finds final gamma step with number % 6 = 3
            threemodsix = True
        else:
            number = gamma_one(number, [1,5])                   # Finds next gamma element with number % 6 = 1 or 5
        steps -= 1
        gamma_sequence.append(number)                           # Adds number to gamma class
    return gamma_sequence
    
number, steps = list(map(int, input("Type an odd natural number and steps: ").split()))
print(gamma_any(number, steps))
