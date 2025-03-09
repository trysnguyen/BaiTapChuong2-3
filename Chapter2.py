import random
import zipfile
import os


def bai26():
    a=input('enter a letter:')
    if a=='u' or a=='e' or a=='i' or a=='o' or a=='a':
        print(a+' is a vowel')
    else:
        print(a+' is a consonant')

def bai27():
    a=int(input('enter a number:'))
    if a<=10 and a>=3:
        print('that is a', a, 'sided shape')
    else:
        print('you entered a number out of range [3;10]')

def bai28():
    a=input('enter a month number:')
    if a==1 or a==3 or a==5 or a==7 or a==8 or a==10 or a==12:
        print('that month have '+' 31 days')
    elif a==2:
        print('that month have 28 days')
    else:
        print('that month have 30 days')

def bai29():
    a=int(input('enter a first side of triangle:'))
    b=int(input('enter a second side of triangle:'))
    c=int(input('enter a third side of triangle:'))
    if a + b > c and a + c > b and b + c > a:
        if a==b and a==c:
            print('that is a equilateral triangle')
        if a==b or a==c or b==c:
            print('that is a isosceles triangle')
        if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
            print ('that is a right triangle')
        else:
            print('that is a normal triangle')
    else:
        print('that is not a triangle')

def bai30():
    a=int(input('enter a year number'))
    if a%4:
        print('that year have 366 days')
    else:
        print('that year have 365 days')

def bai31():
    a=input('enter a letter:')
    if a.isupper():
        b = chr((ord(a) + 3 - 65) % 26 + 65)
    elif a.islower():
        b = chr((ord(a) + 3 - 97) % 26 + 97)
    else:
        b = a
    print('The letter after encryption is', b)

def bai32():
    text = str(input('enter a text:'))
    shift = int(input('Enter a shift value: '))
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    print('Encrypted text:', result)

def bai33():
    a=input('enter a string:')
    for i in range(len(a)):
        if a[i] != a[len(a)-i-1]:
            print('that string is not a Palindrome')
            return
    print('that string is a Palindrome')

def bai34():
    a=input('enter a decimal number:')
    print('the binary number is', bin(int(a))[2:])

def bai35():
    n=int(input('enter a number of elements:'))
    a = []
    for i in range(n):
        x=int(input(f'Enter number at position {i+1}: '))
        a.append(x)
    for i in range(n):
        if a[i]%2==1:
            print (a[i])

def bai36():
    a=[]
    while True:
        x=int(input('enter a number:'))
        if x==0:
            break
        a.append(x)
    print('print all elements:')
    for i in a:
        print(i, end=' ')

def bai37():
    a=set()
    while True:
        x=str(input('enter a string:'))
        if x.isspace():
            break
        a.add(x)
    print("print all elements after remove duplicated:")
    for i in a:
        print(i, end=' ')

def bai38():
    a=[]
    b=[]
    c=[]
    while True:
        try:
            x=int(input('enter a number:'))
        except ValueError:
            break
        if x<0:
            a.append(x)
        if x==0:
            b.append(x)
        if x>0:
            c.append(x)
    for i in a:
        print(i, end=' ')
    for i in b:
        print(i, end=' ')
    for i in c:
        print(i, end=' ')

def bai39():
    n=int(input('enter a number:'))
    a={i: i**2 for i in range(1,n+1)}
    print(a)

def bai40():
    a=(1,2,3,4,5,6,7,8,9)
    print(a[:len(a)//2], a[len(a)//2:])

def bai41():
    a=(1,2,3,4,5,6,7,8,9)
    b=tuple(i for i in a if i%2==0)
    print(b)

def factorial(a):
    if a==1:
        return 1
    return a*factorial(a-1)

def bai42():
    a=int(input('enter a number:'))
    print(factorial(a))

def longerString(a, b):
    if len(a)==len(b):
        print(a)
        print(b)
    elif len(a)>len(b):
        print(a)
    else:
        print (b)

def bai43():
    a=input('enter the first string:')
    b=input('enter the second string:')
    longerString(a,b)

def bai44():
    a=[]
    for i in range(1,21):
        a.append(i**2)
    print(a)

def bai45():
    a = []
    for i in range(1, 21):
        a.append(i ** 2)
    print(a[0:5])

def bai46():
    a = []
    for i in range(1, 21):
        a.append(i ** 2)
    print(a[(len(a)-5):len(a)])

def bai47():
    a=[]
    for i in range(1, 21):
        a.append(i ** 2)
    print(a[5:len(a)])

def average(a, b, c):
    return (a+b+c)/3

def bai48():
    a=float(input('enter the first number:'))
    b=float(input('enter the second number:'))
    c=float(input('enter the third number:'))
    print(average(a,b,c))

def primeNumber(n):
    s=0
    for i in range (1, n+1, 1):
        if n%i==0:
            s+=1
    if s==2:
        return True
    return False

def bai49():
    a=int(input('enter a number:'))
    if primeNumber(a):
        print(a, 'is a prime number')
    else:
        print(a, 'is not a prime number')

def randomPassword():
    length=random.randint(7,10)
    password = ''.join(chr(random.randint(33, 126)) for _ in range(length))
    return password

def bai50():
    print ('generating random password:', randomPassword())

def goodPassword(password):
    if len(password)<8:
        return False
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    return has_upper and has_lower and has_digit

def bai51():
    a=input('Enter your password:')
    if (goodPassword(a)):
        print('Your password is good')
    else:
        print('Your password is not good')

def perfectNumber(n):
    s=0
    for i in range(1,n):
        if n%i==0:
            s+=i
    if s==n:
        return True
    return False

def printPerfectNumberFrom1to10000():
    for i in range(1, 10000):
        if perfectNumber(i):
            print (i)

def bai52():
    a=int(input('Enter a number:'))
    if (perfectNumber(a)):
        print (a, 'is a perfect number')
    else:
        print(a, 'is not a perfect number')
    print('print all perfect numbers from 1 to 10000:')
    printPerfectNumberFrom1to10000()

def all_sublists(lst):
    sublists = []
    n = len(lst)
    for i in range(n):
        for j in range(i + 1, n + 1):
            sublists.append(lst[i:j])
    return sublists

def bai53():
    lst=[1,2,3,4,5]
    print('all sublists:',all_sublists(lst))

def format(n):
    k=n.replace(' ', ', ')
    for i in range(len(k)-1, -1, -1):
        if k[i]==',':
            s=k[i+2:]
            k=k[:i]
            print(k, 'and', s)
            return


def bai54():
    n=input('enter a string:')
    format(n)

def compressFile(filePaths, outputZip):
    with zipfile.ZipFile(outputZip, 'w', zipfile.ZIP_DEFLATED) as zipFile:
        for file in filePaths:
            zipFile.write(file, os.path.basename(file))

def bai55():
    compressFile('test.txt', 'test.zip')

bai26()
bai27()
bai28()
bai29()
bai30()
bai31()
bai32()
bai33()
bai34()
bai35()
bai36()
bai37()
bai38()
bai39()
bai40()
bai41()
bai42()
bai43()
bai44()
bai45()
bai46()
bai47()
bai48()
bai49()
bai50()
bai51()
bai52()
bai53()
bai54()
bai55()
