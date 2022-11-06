def single_step_rev_collatz(n):
    k = 0
    result = 0
    while result % 6 != 3:
        k += 1
        result = (((2**k)*n)-1)/3
    return result, k

def find_next_whole_number(n):
    k = 0
    result = 0
    while result % 6 != 1 and result % 6 != 5:
        k += 1
        result = (((2**k)*n)-1)/3
    return result, k

def any_steps_rev_collatz():
    number, steps = input("Type an odd positive integer and steps").split()
    if number.isdigit() and steps.isdigit():
        number, steps = map(int,(number, steps))
        list = []
        for s in range(1, steps):
            number, k = find_next_whole_number(number)
            list.append((number, k))
        list.append(single_step_rev_collatz(number))
        print(*list, sep = "\n")
    else:
        print("Invalid Input 1")
        exit()

def main():
    any_steps_rev_collatz()

main()