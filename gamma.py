def gamma(n, s):
    reverseCollatz = [n]
    
    def gamma_one(n, mod):
        k = 1
        result = n
        while result % 6 not in mod or k == 1:
            result = (((2**k)*n)-1)//3
            k += 1
        return result
    
    def gamma_any(n, s):
        threemod = False
        while not threemod:
            if s == 1:
                n = gamma_one(n, [3])
                threemod = True
            else:
                n = gamma_one(n, [1, 5])
            s -= 1
            reverseCollatz.append(n)
        return reverseCollatz
        
    return gamma_any(n, s)
    
number, steps = list(map(int, input("Type a odd natural number and steps: ").split()))
print(gamma(number, steps))
