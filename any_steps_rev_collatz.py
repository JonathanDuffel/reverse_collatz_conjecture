def any_steps_rev_collatz():
    number, steps = input("Type an odd positive integer and steps").split()
    if number.isdigit() and steps.isdigit():
        number, steps = map(int,(number, steps))
        list = []
        for _ in range(1, steps):
            k = 0
            result = 0
            while result % 6 != 1 and result % 6 != 5:
                k += 1
                result = (((2**k)*number)-1)/3
            number = result
            list.append((result, k))
        k = 0
        result = 0
        while result % 6 != 3:
            k += 1
            result = (((2**k)*number)-1)/3
        list.append((result, k))
        print(*list, sep="\n")
    else:
        print("Invalid Input")
        exit()

def main():
    any_steps_rev_collatz()