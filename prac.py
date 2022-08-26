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

def july_28_00():
    x = int(input("enter number: "))
    s = 1
    for i in range(21):
        s += (x ** 1)
    print(s)

def july_28_01():
    x = int(input("enter number: "))
    s = 1
    for i in range(21):
        s += (x ** i) / factorial(i)
    print(s)

def july_28_02(x,n):
   total = 1
   nu = 1
   for i in range(1, n+1):
    a = x ** nu
    nu += 2
    b = factorial(i)
    total += (a / b)
    print(total)


def july_28_03():
    x = int(input("enter number: "))
    s = x
    for i in range(0,21,2):
        for j in range(21):
            if j % 2 == 0:
                s += (x ** i) / factorial(i)
            else:
                s -= (x ** i) / factorial(i)
    print(f"sin({x}): {s}")

def july_28_04():
    for i in range(11):
        print(factorial(i))

def july_28_05():
    for i in range(5):
        for j in range(i):
            print(str(j) * j, end="\n")

def july_28_06():
    for i in range(5,-1):
        for j in range(i):
            print(str(j) * j, end="\n")

def july_28_07():
    for i in range(11):
        print(f"{i}: ", end="")
        for j in range(11):
            print(f"{i * j}", end=" ")
        print("\n")

def july_28_08():
    for i in range(0, 4):
        for j in range(i+1):
            print('*', end="")
        print("\r")
    for x in range(4,0,-1):
        for j in range(x):
            print('*', end="")
        print("\r")


def july_28_09():
    x = int(input("enter number: "))
    s = 1
    s -= (x ** 2) / factorial(2)
    for i in range(4,21,2):
        s += (x ** i) / factorial(i)
    print(s)

def july_29():
    choice = int(input("""
            AREA CALCULATOR
        1) Area of triangle
        2) Area of circle
        3) Area of rectangle

        enter choice from above menu: """))
    
    if choice not in range(1,3):
        print("choice not in menu\nGoodBye....")
        quit()
    con = 'y'
    while con == 'y':
        if choice == 1:
            b = int(input("enter base: "))
            h = int(input("enter height: "))
            area = 0.5 * b * h
            print(f"area of triangle: {area}")
            con = input("enter y to continue: ").lower()
            if con == 'y':
                menu()
        if choice == 2:
            r = int(input("enter radius: "))
            area = 3.14 * r ** 2
            print(f"area of circle: {area}")
            con = input("enter y to continue: ").lower()
            if con == 'y':
                menu()
        if choice == 3:
            l = int(input("enter length: "))
            b = int(input("enter breadth: "))
            area = l * b
            print(f"area of rectangle: {area}")
            con = input("enter y to continue: ").lower()
            if con == 'y':
                menu()

def AUG_4_2022_01():
    num = int(input("enter number: "))
    n = str(num)
    s = 0
    for i in n:
        s += 1
    print(f"number of digits in {num}: {s}")

def AUG_4_2022_02():
   x = int(input("What is the number?"))
   a = 0
   b = x
   while x!=0:
    digit = x%10
    x = x//10
    a = a+digit**3
    print(a)
    print(b)
    if a == b:
        print("It is an armstrong number")
    elif a!=b:
        print("It is not an armstrong number")

def AUG_4_2022_03():
    x = int(input("What is the number?"))
    a = 0
    b = x
    while x != 0:
        digit = x%10
        x = x//10
        a = a*10 + digit
    print(b)
    print(a)
    if a == b:
        print("It is a palindrome")
    elif a!=b:
        print("It is not a palindrome")

def AUG_4_2022_04():
    x = int(input("What is the number?"))
    a = 0
    b = x
    while x != 0:
        digit = x%10
        x = x//10
        a = a*10 + digit
    print(b)
    print(a)

def AUG_16_01():
    string = input("enter string: ")
    vowels = ['a', 'e', 'i', 'o', 'u']
    c = 0
    for i in string:
        if i.lower() in vowels:
            c+=1
    print(c)

def AUG_16_02():
    string = input('enter string: ')
    c_upper = 0
    c_lower = 0
    c_digit = 0
    c_space = 0
    for i in string: 
        if i.isupper():
            c_upper+=1
        elif i.islower():
            c_lower += 1
        if i.isdigit():
            c_digit += 1
        if i.isspace():
            c_space += 1
    print(f"upper: {c_upper}\nlower: {c_lower}\ndigit: {c_digit}\nspace: {c_space}")

def AUG_16_03():
    string = input('enter string: ')
    print(string[-1]+string[1:-1]+string[0])

def AUG_16_04():
    string = input('enter string: ')
    nstr = ""
    for i in string:
        nstr = i + nstr
    print(nstr)

def AUG_16_05():
    string = input('enter string: ')
    print(string[1:] + string[0])

def AUG_16_06():
    string = input("enter string: ")
    nstring = string[0] + "."
    for i in range(len(string) - 1):
        if string[i].isspace():
            nstring += string[i + 1] + "."
    print(nstring)

def AUG_16_07():
    string = input("enter string: ").lower()
    nstring = string[::-1]
    if string == nstring:
        print("it is a palindrome")
    else:
        print("not a palindrome")

def AUG_16_08():
    string = input("enter string: ")
    for i in range(len(string)):
        print(string[i:] + string[:i])

def AUG_16_09():
    x = "y"
    while x == "y":
        u = 0
        l = 0
        d = 0
        c = 0
        s = input("enter password: ")
        for i in s:
            if i.isupper():
                u += 1
            elif i.islower():
                l += 1
            elif i.isdigit():
                d += 0
            if len(s) < 8:
                print("password must contain 8 chars")
                c+= 1
            if u == 0:
                print("password must have 1 uppercase char")
                c += 1
            if l == 0:
                print("password must have 1 lowercase char")
                c += 1
            if d == 0:
                print("password must have 1 digit")
                c += 1
            if c == 0:
                x = input("to change ur password: type y")

def AUG_17_01():
    li = []
    su = 0
    for i in range(10):
        x = int(input("enter number: "))
        li.append(x)
    for y in li:
        if y % 2 == 0:
            su += y
    print(su)

def AUG_17_02():
    li = []
    for i in range(10):
        x = int(input("ENTER NUMBER: "))
        li.append(x)
    li2 = li[::-1]
    print(li2)

def AUG_17_03():
    li = []
    for i in range(10):
        x = int(input("enter number: "))
        li.append(x)
    li2 = []
    for y in li:
        if y % 2 == 0:
            li2.append(y // 2)
        else:
            li2.append(y * 2)
    print(li2)

def AUG_17_04():
    li = []
    for i in range(10):
        x = int(input("enter number: "))
        li.append(x)
    su = 0
    for i in li:
        su += i**2
    print(su)

def AUG_17_05():
    li = []
    for i in range(7):
        x = int(input("enter number"))
        li.append(x)
    nli = li[::-1]
    print(nli)

def AUG_17_06():
    li1 = []
    li2 = []
    for i in range(5):
        x = int(input("enter number: "))
        li1.append(x)
    for i in range(5):
        x = int(input("enter number: "))
        li2.append(x)
    nli = []
    for i in range(len(li1)):
        nli.append(li1[i])
        nli.append(li2[i])
    print(nli)
AUG_17_06()