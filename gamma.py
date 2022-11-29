def gamma(n, s):
    gamma_class = [n]
    
    def gamma_one(n, desired_mod):                          # Returns reverse collatz result
        k = 1
        result = n                                          # Keep n unchanged
        while result % 6 not in desired_mod or result == n: # Gamma class must not have repeating elements
            result = (((2**k)*n)-1)//3                      # Reverse collatz equation
            k += 1                                          # Incriment k until the result is a desired mod6
        return result
    
    def gamma_any(n, s):                                    # Returns gamma class beggining at n with s steps
        threemodsix = False
        while not threemodsix:                              # Runs repeatedly until n is 3mod6
            if s == 1:
                n = gamma_one(n, [3])                       # Finds final gamma step with n % 6 = 3
                threemodsix = True
            else:
                n = gamma_one(n, [1,5])                     # Finds next gamma step with n % 6 = 1 or 5
            s -= 1
            gamma_class.append(n)                           # Add n to gamma class
        return gamma_class
        
    return gamma_any(n, s)
    
number, steps = list(map(int, input("Type a odd natural number and steps: ").split()))
print(gamma(number, steps))
