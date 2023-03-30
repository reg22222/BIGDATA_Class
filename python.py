import datetime
from pytz import timezone
'''a = int(input("a입력 : "))
b = int(input("b입력 : "))
if a == 3 and b == 4:
    print("OK")
if a == 3 or b == 4:
    print("Okay")

x = int(input("숫자입력 : "))
if x > 10 and x % 2 == 0:
    print("10초과 짝수")

a = int(input('필기 성적을 입력하세요 : '))
b = int(input("필기 성적을 입력하세요 : "))

if a <= 80 and b <= 80:
    print("합격!")
else :
    print("불합격!")

age = int(input("몇 살이세요? : "))

if 0 <= age < 7 or age >= 65:
    print("입장료는 무료입니다.")
else:
    print("입장료는 3000원입니다.")


age = int(input("나이 : "))
height = int(input("키 :"))

if age >= 10 and height >= 150:
    print("놀이기구를 탈 수 있다.")
else:
    print("놀이기구를 탈 수 없다.")

id = input("아이디를 입력하세요ㅕ :")
le = int(input("회원레벨을 입력해주세요 :"))

if id == "admin" or le == 1:
    print("관리자입니다.")
else:
    print("관리자가 아닙니다.")

n = int(input("정수를 입력하세요 : "))

if 1<= n <=100:
    print(n,"은 1~100사이에 있다")
else:
    print(n,"은 1~100사이에 없다")


m = 3

if 3 <= m <= 5:
    print('봄입니다.')
if 6 <= m <= 8:
    print('여름입니다.')
if 9 <= m <= 11:
    print('가을입니다.')
else:
    print('겨울입니다.')


a = int(input("구매금액:"))

if a <20000:
    print("배송불가")
elif a >= 50000:
    print("무료배송입니다.")
else :
    print('배송비 2500원이 추가됩니다/')

n = int(input('점수를 입력하세요 : '))

if n >= 90:
    print("A등급")
elif n >= 80:
    print("B등급")
elif n >= 70:
    print("C등급")
elif n < 70:
    print("F등급")

o = int(input("온도를 입력하세요 : "))

if 0 <= o < 100:
    print('액체입니다.')

eng = int(input('영어시험 점수를 입력하세요 : '))
math = int(input('수학시험 점수를 입력하세요 : '))

if eng < 80 and math < 80:
    print("재시험 기회 없음")
elif (eng < 80 and math > 80)or(eng>80 and math<80):
    print('재시험 기회 제공')
else:
    print('합격')

a = int(input("서비스가 어떠나요(1ㅡ2ㅡ3) : "))
b = int(input('음식값을 입력해주세요 : '))

if a== 1:
    print("팁 : {}".format(int(b / 20)))
elif a == 2:
    print("팁 : {}".format(int(b / 10)))
elif a == 3:
    print("팁 : {}".format(int(b / 5)))

a = int(input("물건 구매가를 입력하세요 : "))
h = 0;
print("구매가 : ",a)

if a <= 50000:
    print('할인율 : 5%')
    print('할인 금액 : {}'.format(a/5))
    print("지불 금액 : {}".format(a-(a/5)))
elif 50000 <= a <= 300000:
    print('할인율 : 7.5%')
    print('할인 금액 : {}'.format(a/7.5))
    print("지불 금액 : {}".format(a-(a/7.5)))
elif a >= 300000:
    print('할인율 : 10%')
    print('할인 금액 : {}'.format(a/10))
    print("지불 금액 : {}".format(a-(a/10)))

a = int(input("원하는 메뉴를 선택하세요 1.떡볶이 3000원, 2.김밥 2500원, 3.튀김 3500원: "))

if a == 1:
    print("떡볶이를 선택하셧군요!")
    n = int(input('떡볶이를 몇 인분 주문하시겠습니까? : '))
    print("총 가격은 {}원 입니다.".format(3000*a))
elif a == 2:
    print("김밥를 선택하셧군요!")
    n = int(input('김밥을 몇 인분 주문하시겠습니까? : '))
    print("총 가격은 {}원 입니다.".format(2500*a))
elif a== 3:
    print("튀김을 선택하셧군요")
    n = int(input('튀김를 몇 인분 주문하시겠습니까? : '))
    print("총 가격은 {}원 입니다.".format(3500*a))

a = int(input("체중을 입력하세요 : "))
b = int(input('키를 입력하세요 : '))

bmi = a/pow(b,2)

if 0 <= bmi <= 15:
    print("당신의 bmi지수는 {}이며 정상입니다.".format(bmi))
elif 15 < bmi <= 25:
    print("당신의 bmi지수는 {}이며 과체중입니다.".format(bmi))
elif bmi > 25:
    print("당신의 bmi지수는 {}이며 비만입니다.".format(bmi)

x = 17
if x > 10:
    if x % 2 == 0:
        print("10초과 짝수")
    else:
        print("10초과 홀수")
else:
    print("10이하")


id = int(input("아이디를 입력하세요 : "))
le = int(input("회원레벨 입력 : "))

if id == 'admin':
    print('모든콘텐츠 이용가능')
else :
    if 2 <= le <= 7:
        print('일부 콘텐츠 이용가능')
    else :
        print("이용 불가.")

hy  = int(input("현재년을 입력해 주세요 : "))

hm  = int(input("현재월을 입력해 주세요 : "))

hd  = int(input("현재일을 입력해 주세요 : "))

cy  = int(input("출생년을 입력해 주세요 : "))

cm  = int(input("출생월을 입력해 주세요 : "))

cd  = int(input("출생일을 입력해 주세요 : "))

if cm < hm :
    a = hy-cy
elif cm == hm:
    if cd < hd:
        a = hy-cy
    elif cd > hd:
        a = hy-cy-1
else:
    a = hy-cy-1

print("------------------------------------------")
print("오늘날짜 : {}년 {}월 {}일".format(hy,hm,hd))
print('생년 월일 : {}년 {}월 {}일 '.format(cy,cm,cd))

print("-----------------------------------------")
print("만나이 : {}".format(a)))

now  = datetime.datime.now(timezone('Asia/Seoul'))

print(now)
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)'''
