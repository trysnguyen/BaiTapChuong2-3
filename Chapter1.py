import math

def bai6():
    r=float(input('enter radius of cylinder:'))
    h=float(input('enter height of cylinder:'))
    print ('Volume of cylinder:', r*r*h*math.pi)

def bai7():
    a=float(input('enter the first length of triangle:'))
    b=float(input('enter the second length of triangle:'))
    c=float(input('enter the third length of triangle:'))
    p=(a+b+c)/2
    print ('Area of the triangle:', math.sqrt(p*(p-a)*(p-b)*(p-c)))

def bai8():
    a=float(input('enter the length of equilateral triangle:'))
    print('Area of the equilateral triangle:', a*a*math.sqrt(3)/4)

def bai7_1(a,b,c):
    p = (a + b + c) / 2
    print('Area of the triangle:', math.sqrt(p * (p - a) * (p - b) * (p - c)))

def bai8_1(a,b,c):
    print('Area of the equilateral triangle:', a * a * math.sqrt(3) / 4)

def bai9():
    a = float(input('enter the first length of triangle:'))
    b = float(input('enter the second length of triangle:'))
    c = float(input('enter the third length of triangle:'))
    if a==b and b==c:
        bai8(a,b,c)
    else:
        bai7(a,b,c)

def bai10():
    a=float(input('enter the first dimension of the room:'))
    b=float(input('enter the second dimension of the room:'))
    print('the area of the room is', a*b)

def bai11():
    a=float(input('nhap kich thuoc thu nhat cua canh dong (do dai met):'))
    b=float(input('nhap kich thuoc thu 2 cua canh cong (do dai met):'))
    print('dien tich cua canh dong la', a*b/43560, 'Mau Anh')

def bai12():
    a=float(input('Enter the price of the meal:'))
    print('Total money after tax and tips:', a*123/100)

def bai13():
    n=int(input('Enter n to calculate sum from 1 to n:'))
    print('sum =', (n*(n+1))/2)

def bai14():
    a=int(input('Enter number a:'))
    b=int(input('Enter number b:'))
    print ('a+b =', a+b)
    print ('a-b =', a-b)
    print ('a*b =', a*b)
    try:
        result = a/b
    except ZeroDivisionError as e:
        print(f"Error: {e}")
    else:
        print('a/b =', a/b)
    print('a//b = ', a//b)
    print('log10(a) = ', math.log10(a))
    print('a^b = ', a**b)

def bai15():
    a=float(input('Enter volume of water:'))
    b=float(input('Enter delta temperature:'))
    q=a*b*4.168
    print('sum of energy:',q)
    print('cost:', (q*2.777*math.e**(-7))*8.9, 'cent')

def bai16():
    a=float(input('Enter the height of the object:'))
    print('speed =', math.sqrt(0**2 + 9.8*a))

def bai17():
    a=float('Enter temperature of air:')
    b=float('Enter speed of wind:')
    print('cold air index:', 13.12+0.6215*a-11.37*b+0.3965*a*b)

bai6()
bai7()
bai8()
bai9()
bai10()
bai11()
bai12()
bai13()
bai14()
bai15()
bai16()
bai17()



