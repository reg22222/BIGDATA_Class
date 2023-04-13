import random
'''
import random

sunny = random.random()
time = random.randint(0,23)


if(time < 12):
    print("좋은 아침입니다. 지금 시각은 {}시 입니다.".format(time))
else:
    print("좋은 오후입니다. 지금 시각은 {}시 입니다.".format(time))
    
if(sunny == 0):
    print('현재 날씨가 화창하지 않습니다.')
else:
    print('현재 날씨가 화창합니다')
    
if(sunny == 1 and 6<=time <= 18):
    print("종달새가 노래를 합니다.")
else:
    print("종달새가 노래를 하지 않습니다.")

x = 0
while x < 3:
    print("안녕하세요")
    x += 1


st = 1
while st <= 3:
    print(st, '번 학생의 성적을 처리한다')
    st += 1


dan = int(input("원하는 단은?"))
i = 1
while i <=9:
    print("{} * {} = {}".format(dan,i,dan*i))
    i+=1


num = 1
sum = 0

while num <= 10:
    sum += num
    print("num의 값 : {} => 합계 : {}".format(num,sum))
    num+=1
    
    
num = 10
sum = 0

while num <= 20:
    sum += num
    print("num의 값 : {} => 합계 : {}".format(num,sum))
    num+=1


i = 150
sum = 0
while i <= 300:
    if i % 2 != 0:
        sum+=i
        i+=1
        
print("sum = {}".format(sum))  


s = -5

while s <= 5:
    f = s*9.0/5.0+32.0
    print("섭씨 : {} 화씨 : {}".format(s,f))
    s +=1
    

n = 10
f = 1

while n >= 1:
    f += n
    n-=1
print("10! = ".format(n)) 

num = 1
while num <= 20:
    if num % 2 == 0 #2의 배수일 떄
        print(num)
    num += 1


n = 10

while n <= 50:
    if(n % 3 != 0):
        print(n)
        n+=1
        



while True:
    p = input("암호 입력 : ")
    
    if p == "python":
        print("로그인 성공")
    else:
        continue'''
        

a = random.randint(1, 100)
count = 0

while True:
    b = int(input("1부터 100까지의 숫자를 입력하세요: "))
    if b < 1 or b > 100:
        print("다시 입력")
        continue
    count += 1
    if a == b:
        print("{}번만에 맞췄습니다!".format(count))
        break
    elif a > b:
        print("Down")
    else:
        print("Up")
        
print("끝낫당이")