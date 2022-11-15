def collatz(num):
    list = []
    while num != 1:
        list.append(num)
        if num % 2 == 0:
            num = int(num / 2)
        else:
            num = int(3 * num + 1)
    else:
        list.append(num)
    return list

def any_steps_rev_collatz(n, s):
    if n % 2 == 1 or s > 0:
        n = int(n)
        s = int(s)
        list = []
        for _ in range(1, s):
            k = 0
            result = 0
            while result % 6 != 1 and result % 6 != 5:
                k += 1
                result = (((2**k)*n)-1)//3
            n = result
            list.append(result)
        k = 0
        result = 0
        while result % 6 != 3:
            k += 1
            result = (((2**k)*n)-1)//3
        list.append(result)
        return list
    else:
        return []