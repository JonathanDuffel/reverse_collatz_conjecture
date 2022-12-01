def gamma_one(number, desired_mod):                             # Returns reverse collatz result
    k = 1
    result = number                                             # Keep n unchanged
    while result % 6 not in desired_mod or result == number:    # Gamma class must not have repeating elements
        result = (((2**k) * number) - 1) // 3                   # Reverse collatz equation
        k += 1                                                  # Incriment k until the result is a desired mod6
    return result
        
def gamma_any(number, steps):                                   # Returns gamma class beggining at n with s steps
    gamma_sequence = [number]
    threemodsix = False
    while not threemodsix:                                      # Runs repeatedly until n is 3mod6
        if steps == 1:
            number = gamma_one(number, [3])                     # Finds final gamma step with n % 6 = 3
            threemodsix = True
        else:
            number = gamma_one(number, [1,5])                   # Finds next gamma step with n % 6 = 1 or 5
        steps -= 1
        gamma_sequence.append(number)                           # Add n to gamma class
    return gamma_sequence
    
number, steps = list(map(int, input("Type a odd natural number and steps: ").split()))
print(gamma_any(number, steps))
