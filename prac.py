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

def factorial():
    x = int(input("enter number: "))
    a = 1
    for i in range(1,x+1):
        a *= i
    print(a)

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




