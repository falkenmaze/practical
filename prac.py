#helper function
def factorial(x):
    a = 1
    for i in range(1,x+1):
        a *= i
    return a
#question functions
def average():
    numbers = []
    i = 0
    while i <= 20:
        num = int(input(f"enter {i} number: "))
        numbers.append(num)
        i += 1
    even = []
    odd = []
    for x in numbers:
        if x % 2 == 0:
            even.append(x)
        else:
            odd.append(x)

    toteve = 0
    totodd = 0
    for y in even:
        toteve += y
    if len(even) != 0:
        average_even = toteve / len(even)
    else:
        average_even = 0
    for z in odd:
        totodd += z
    if len(odd) != 0:
        average_odd = totodd / len(odd)
    else:
        average_even = 0
    print(f"average of even number: {average_even}\naverage of odd numbers: {average_odd}")

def cube():
    i = 0
    while i <= 10:
        x = int(input(f"enter {i} number: "))
        cube_of_x = x ** 3
        print(cube_of_x)
        i += 1 

def factorial_q():
    x = int(input("enter number: "))
    a = 1
    for i in range(1,x+1):
        a *= i
    print(a)

def series():
    y = int(input("enter number of elements: "))
    j = 2
    s = 0
    x = int(input(f"enter numerator: "))
    for i in range(y):
        a = x / j
        s += a
        j += 2
    print(s)


def multiply():
    x = int(input("enter number: "))
    for i in range(10+1):
        print(f"{x} X {i} = {x * i}")

def sumofdigits():
    a = input("enter number: ")
    s = 0
    for i in a:
        s += int(i)
    print(s)

def sum_of_series():
    x = int(input("enter number: "))
    s = 1
    for i in range(21):
        s += (x ** 1)
    print(s)

def ss2():
    x = int(input("enter number: "))
    s = 1
    for i in range(21):
        s += (x ** i) / factorial(i)
    print(s)

def ss3():
    x = int(input("enter number: "))
    s = 1
    for i in range(1,21,2):
        for j in range(1,21):
            s += (x ** i) / factorial(j)
    print(s)

def ss5():
    x = int(input("enter number: "))
    s = x
    for i in range(0,21,2):
        for j in range(21):
            if j % 2 == 0:
                s += (x ** i) / factorial(i)
            else:
                s -= (x ** i) / factorial(i)
    print(f"sin({x}): {s}")

def ss6():
    for i in range(11):
        print(factorial(i))

def ss7():
    for i in range(5):
        for j in range(i):
            print(str(j) * j, end="\n")

def ss8():
    for i in range(5,-1):
        for j in range(i):
            print(str(j) * j, end="\n")

def ss9():
    for i in range(11):
        print(f"{i}: ", end="")
        for j in range(11):
            print(f"{i * j}", end=" ")
        print("\n")

def ss10():
    for i in range(0, 4):
        for j in range(i+1):
            print('*', end="")
        print("\r")
    for x in range(4,0,-1):
        for j in range(x):
            print('*', end="")
        print("\r")


def ss11():
    x = int(input("enter number: "))
    s = 1
    s -= (x ** 2) / factorial(2)
    for i in range(4,21,2):
        s += (x ** i) / factorial(i)
    print(s)