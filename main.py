import matplotlib.pyplot as plt
import rev_collatz as rc

step = []
number = []
counter = 0
n = 7
s = 5

list = rc.any_steps_rev_collatz(n, s)
list.reverse()
list += rc.collatz(n)

for x, y in enumerate(list, start=1):
    step.append(x)
    number.append(y)

plt.plot(step, number)
plt.title('Collatz Conjecture', fontsize = 20)
plt.xlabel('Step', fontsize = 15)
plt.ylabel('N', fontsize = 15)
plt.show()

