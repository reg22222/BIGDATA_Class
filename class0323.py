'''
print(5+2)
print(5-2)
print(5*2)
print(5/2)
print(5**2)
print(5//2)
print(5%2)


x = 10%3
print(x)
y = 7//3
print(y)

a = 10
b = 20
c = a+b*10-5/5
print(c)

x = 2**3
print(x)
y = 10**4
print(y)

hello = '안녕' * 5
print(hello)

s1 = "대한민국"
s2="만세"
print(s1+s2)
print(s1*5)

print("korea"+str(2021))
print(10+int("22"))
print(10 + int(22.5))
print(10 + int(float(22.5)))
print("korea"+2021)

x = 10
x += 20
print(x)

a = 5
a = a+1
print(a)

a = 5
a += 1
print(a)

a -= 5
print(a)

a *= 2
print(a)

x = 3
y = 5
x *= x+y
print(x)

tdon = int(input("투입한 돈 : "))
mdon = int(input("물건 값 : "))

gdon = tdon - mdon
don5 = gdon//500

dondon = (don5%500)//100

print("거스름돈 : {}".format(gdon))
print("500원 동전의 개수 : {}".format(don5))
print("100원 동전의 개수 : {}".format(dondon))

if 3 < 5:
    print("hello World")

age = int(input("몇살입니까?"))
if age<20:
    print("학생입니다.")

print(3 == 5)
print(3 != 5)
print(3 < 5)
x = 4

print(1 < x < 5)
num = int(input("숫자입력 : "))
if num == 5:
    print("5입니다.")
if num > 5:
    print("5보다 크다.")
if num < 5:
    print("5보다 작다.")

country = input("나라입력 : ")
if country == "Korea":
    print("한국")

age = int(input('몇 살입니까?'))

if age <20:
    print("학생입니다.")
else :
    print("성인입니다.")

num = int(input("정수 입력 : "))
if num % 2 == 0:
    print("짝수")
else :
    print("홀수")


num = int(input("정수 입력 : "))
if num > 0:
    print("양수")
else :
    print("0 또는 음수")

num1 = int(input("첫 번째 숫자 : "))
num2 = int(input("두 번째 숫자 :"))
if num1 > num2:
    print(num1-num2)
else:
    print(num2-num1)

a = int(input("1(주간 근무) 또는 2(야간 근무)을 입력해주세요 : "))
b = int(input("근무시간을 입력해주세요 : "))

if a == 1: 
    print("{}시간동안 일한 주간 급여는 {}원 입니다.".format(b,9500*b))
else :
    print("{}시간동안 일한 야간 급여는 {}원 입니다.".format(b,int(9500*1.5*b)))'''

name = input("이름을 입력하세요 : ")
time = int(input("일주일간 일한 시간을 입력하세요 : "))
if time < 40:
    print("{}님의 주급은 {}입니다.".format(name,12000*time))    
else :
    print("초과시간 : {}".format(time-40))
    print("{}님의 주급은 {}입니다.".format(name,int((time-40)*1.5*12000)+(40*12000)))