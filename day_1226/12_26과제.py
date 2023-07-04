# 1. 문자열 리스트를 입력 받아서 내림차순 결과 가장 낮은 문자열과 가장 높은 문자열을
#  출력하는 함수를 구현하세요.
msg=['Good', 'child', 'Zoo', 'apple', 'Flower', 'zero']


msg.sort(reverse=True)

print(msg)
print(f'최고 : {max(msg)}, 최저 : {min(msg)}')




# 동환님 방법
N=6
A = []
for i in range(N):
   A.append(input('입력하세요: '))
A.sort(reverse=True)
print('정렬결과 : ', A)
print('가장 높은 문자열:', A[0],end=', ') # =max(A)
print('가장 낮은 문자열:', A[-1]) # =min(A)


# 호림님 방법
def 정렬(A):
    A.sort(reverse=True)
    print(f'정렬 결과: {A}\n가장 높은 문자열: {A[0]}, 가장 낮은 문자열: {A[-1]}')
msg=[]
[msg.append(input()) for i in range(6)]
정렬(msg)


#새로운 방법
msg=input(" 입력 : ")
msg1=msg.split(',')
print(f'정렬결과 : {sorted(msg1)}')
print(f'가장 높은 문자열 : {max(msg1)}, 가장 낮은 문자열 : {min(msg1)}')



#  2. 문자열을 입력하면 UTF-8로 인코딩된 값을 아래와 같이 출력된 함수를 구현해 주세요.

#방법1
data="가나다"

print((hex(ord('가')))+(hex(ord('나')))+(hex(ord('다'))))
print((bin(ord('가')))+(bin(ord('나')))+(bin(ord('다'))))


#방법2
data="가나다"
a=[]
b=[]
for i in data:
    a.append(hex(ord(i)))
    b.append(bin(ord(i)))

print(*a, sep='')
print(*b, sep='')



#  3. 숫자와 콤마로만 이루어진 문자열 data가 주어진다. 이때, data에 포함되어있는 자연
#  수의 합과 가장 작은 수, 가장 큰 수를 출력하는 함수를 구현하세요.
A=[]
data='123,42,98,18'

for i in data:
    if i.isdigit():
        A.append(int(i))

print(f'합 : {sum(A)}, 최고 : {max(A)}, 최저 : {min(A)}')


print(f'--------------------------------------------------------------------------')



data='1,234'

A=[]
data='1,234'

for i in data:
    if i.isdigit():
        A.append(int(i))

print(f'합 : {sum(A)}, 최고 : {max(A)}, 최저 : {min(A)}')




# 4.    2, 4, 8 게임은 숫자의 끝 자리가 2, 4, 8로 끝나는 숫자의 경우 다른 문자로 출력하는
#       게임으로 아래 조건을 만족하도록 구현하자.


n=int(input("게임 정수 입력 : "))

for i in range(1,n+1):
    if i%10==2 or i%10==4 or i%10==8:
        print('#', end='')
    elif i%20==0:
        print(i)
    else:
        print(i,end='')



print(f'------------------------------------')




def 게임(num):
    num=int(num)
    for i in range(1,num+1):
        if i%10 in [2,4,8]: print('#',end='')
        elif i%20==0: print(i)
        else: print(i,end='')

숫자=input('게임 정수 입력 : ')
게임(숫자)




#  5. 월(Month)을 입력 받아 해당 월(Month)의 영어와 계절을 출력하는 코드를 작성하세요.

month=int(input("좋아하는 달 입력 : ").strip())
season=''

if (month in [1]):
    season='january winter'
elif (month in [2]):
    season='feburary winter'
elif (month in [3]):
    season='march spring'
elif (month in [4]):
    season='april spring'
elif (month in [5]):
    season='may spring'
elif (month in [6]):
    season='june summer'
elif (month in [7]):
    season='july summer'
elif (month in [8]):
    season='august fall'
elif (month in [9]):
    season='september fall'
elif (month in [10]):
    season='october fall'
elif (month in [11]):
    season='november witer'
elif (month in [12]):
    season='december winter'
else:
    season='존재하지 않는 달입니다.'

print(season)





#  6. 숫자와 화폐단위를 입력 받아 세자리 마다 쉼표(,) 찍어서 출력하는 기능을 구현하세요.

def data(num,won):
    print(format(num, ','),end='')
    print(won)

data(12345678,'$')


#  7. 입력받은 정수에 대한 약수를 출력하는 함수를 만들어 주세요.

num = int(input('약수 구하고 싶은 수 : '))

print(f'{num}의 약수 : ', end='')

for i in range(1,num+1):
    if i != num:
        if num%i==0:
            print(i, end=', ')
    else:
        print(i)



#  8. 입력 받은 메시지 중에서 중복 없이 숫자만 출력하는 함수를 만들어 주세요.

string = input()

dd= ['0','1','2','3','4','5','6','7','8','9']

A=[]

for i in range(0,len(string)):
    if string[i] in dd :
        if int(string[i]) not in A:
            A.append(int(string[i]))

print(A)






print(f'----------------------------------------------------------')


while True:
    string=input('메시지 입력:')
    if string=='X' or string=='x':
        break
    number=list(filter(str.isdigit,string))
    result=[]
    for i in number:
        if i not in result:
            result.append(i)
    print(result)



print(f'----------------------------------------------------------')

def 출력(text):
    A=set(filter(str.isdigit,text))
    print(*A,sep=', ')
출력('happy 2023')



print(f'----------------------------------------------------------')




def 출력(text):
    A=list(filter(str.isdigit,text))
    B=list(dict.fromkeys(A))
    print(*B,sep=', ')
출력('happy 2023')
출력('홍길동 010-3113-0782')



#  9. 생일을 입력 받은 후 한국 나이, 외국 나이를 알려주는 함수를 생성해 주세요. 

from datetime import datetime

birth = input('양력 생일(YYYY.MM.DD)을 입력하세요. ')
birth = datetime.strptime(birth, '%Y.%m.%d').date()
today = datetime.now().date()
year = today.year - birth.year
if today.month < birth.month:
    year -= 1
elif today.month == birth.month and today.day < birth.day:
    year -= 1

print(f'한국나이는 {year+2}살입니다.')
print(f'한국나이는 {year}살입니다.')



birth=input('(YYYY.MM.DD)생년월일 입력: ')
A=[]
for i in birth:
    if i.isdigit():
        A.append(int(i))
print('당신의 한국 나이는',end='')
print('',2022-(A[0]*1000+A[1]*100+A[2]*10+A[3])+1)
print('당신의 외국 나이는',end='')
print('',2022-(A[0]*1000+A[1]*100+A[2]*10+A[3]))




#  10. 팩토리얼(Factorial)을 while반복문으로 구현해 주세요. 팩토리얼 수를 입력 받아서 
#  팩토리얼 결과를 아래와 같이 출력하세요.
number = int(input())
num = number
answer = 1
while num:
    answer *= num
    num -= 1

print(f'{number}! => {answer}')




#  11. 입력받은 숫자 범위 안에서 소수(Prime Number)를 찾아서 반환하는 함수를 생성하세요.
# [입 력] 범위 숫자 입력 : 30
# [출 력] 1 ~ 30 범위에서 소수 : 2, 3, 5, 7, 11, 13, 17, 19, 23, 29



num=int(input("알고 싶은 숫자 입력 : ").strip())
prime_number=[]

for x in range(1, num+1):
    count=True

    for y in range(2,x):
        if x%y==0:
            count=False
            break
    if count:
        prime_number.append(x)
print(prime_number)





# print(f'-------------------------------------------------')

#  12. 아래 데이터를 저장합니다. 그리고 과목별 최고점수, 최저점수 출력하세요.

# 이름 국어 수학 윤리 국사
# 베트맨 90 89 98 99
# 마징가 82 71 80 91
# 슈퍼맨 77 100 92 90
# 슈렉 94 82 93 71
# 피오나 78 99 91 83


kor=[90,82,77,94,78]
math=[89,71,100,82,99]
eth=[98,80,92,93,91]
his=[99,91,90,71,83]

kor_sum=sum(kor)/len(kor)
math_sum=sum(math)/len(math)
eth_sum=sum(eth)/len(eth)
his_sum=sum(his)/len(his)

print(f'최고점수 : {max(kor)}, 최저점수 : {min(kor)}, 평균 : {kor_sum}')
print(f'최고점수 : {max(math)}, 최저점수 : {min(math)}, 평균 : {math_sum}')
print(f'최고점수 : {max(eth)}, 최저점수 : {min(eth)}, 평균 : {eth_sum}')
print(f'최고점수 : {max(his)}, 최저점수 : {min(his)}, 평균 : {his_sum}')





#  13. 구구단 n단부터 m단까지를 반복문 1개로 구현하는 함수를 생성하세요.

def gugudan(num): # 몇단까지 출력할 것인가
    for b in range(1,10): # a X b = c 에서 b 부분
        for a in range(2, num+1): # a X b = c 에서 a 부분
            print(a, 'X', b, '=', a*b, end  ='\t')
        print()
gugudan(5)



print(f'--------------------------------------------------------------------------------------')



def gugudan(start_n,end_n):
    n = start_n
    k = 1
    switch = True
    
    while k != 10:
        if switch:
            print(f"--[{n}단]--",end='     ')
            n +=1
            if n==end_n+1: switch = False; n = start_n; print()

        if not switch:
            print(f"{n}*{k}= {n*k:2}",end='       ')
            n +=1
            if n==end_n+1: n = start_n; k +=1; print()


gugudan(2,4)




print(f'--------------------------------------------------------------------------------------')









#  14. 입력받은 숫자에서 천자리, 백자리, 십자리, 일자리를 출력하세요.
N=5
list1 = []

for i in range(N):
    list1.append(input('입력하세요: '))

def numbers():
    print("숫자: ", list1[0]+list1[1]+list1[2]+list1[3]+list1[4])
    print("만의 자리: ", list1[0])
    print("천의 자리: ", list1[1])
    print("백의 자리: ", list1[2])
    print("십의 자리: ", list1[3])
    print("일의 자리: ", list1[4])

numbers()




# 숫자를 문자로 변환해서 리스트에 담아 리스트 인덱스로 출력하는 방식으로...




#  15. 정수, 실수, 논리, 문자열 등 데이터 입력 시 모두 덧셈한 결과 출력하는 함수를 생성하세요.
# [호 출] 

# addData()) 
# addData(1,3,5)) 
# addData(True, True, False, False, True)) 
# addData('A')) 
# addData('A','BC','Good'))

# [출 력] 
# None
#  9
#  3
#  A
#  ABCGood

def addData(*datas):
    if len(datas)>0:  
        if isinstance(datas[0], str): 
            total= ''    
        else:
            total= 0

        for data in datas:
            total +=data

        return total

print(addData())
print(addData(1,3,5))
print(addData(True, True, False, False, True))
print(addData('A'))
print(addData('A','BC','Good'))







#  16. 아래 출력결과가 나오도록 코드를 작성하세요.
for h in range(10,0,-1):
  print(f'{" "*int(h)}{"*"*(2*(10-int(h))+1)}',end="\n")    
print("         ***\n         ***\n         ***")



#호림씨 방법
n=-1
while n<15:
    n=n+2
    print(('*'*n).center(15))
print(('****').center(15))
print(('****').center(15))
print(('Merry Christmas').center(15))
print(('2023').center(15))

#내가한거
print(' '*7+'*')
print(' '*6+'*'*3)
print(' '*5+'*'*5)
print(' '*4+'*'*7)
print(' '*3+'*'*9)
print(' '*2+'*'*11)
print(' '*1+'*'*13)
print('*'*15)
print(' '*6+'*'*4)
print(' '*6+'*'*4)
print(' '*1+'Merry Christmas'.upper())
print(' '*6+'2023')



#  17. 문자열 ‘Merry Christmas HaPPy New YEaR’에서 대문자는 소문자로, 소문자는 대문자로 
#  변환하여 출력하는 코드를 구현하세요.
# msg='Merry Christmas HaPPy New YEaR'
# msg1=list(msg)
# empty=[]

# for s in msg:
#     if s.isupper():
#         empty.append(s.lower())
#     elif s.islower():
#         empty.append(s.upper())
# print(empty)

#리스트 컴프리핸션
stc =  'Merry Christmas HaPPy New YEaR'
result=''.join([i.upper() if i.islower() else i.lower() for i in stc])

print(result)


# 호림님
text='Merry Christmas HaPPy New YEaR'
A=[i.swapcase() for i in text]
print(text)
print('=>',*A)




#  18. 6가지 연산 결과를 한꺼번에 반환하는 함수를 생성 후 호출하여 결과를 아래와 같이
#  출력해 주세요.
nums=input("숫자 입력 : (예. 3,4)")

num1, num2=nums.split(',')
num1, num2=int(num1), int(num2)
print(f'덧셈결과 : {num1+num2}')
print(f'뺄셈결과 : {num1-num2}')
print(f'곱셈결과 : {num1*num2}')
print(f'나눗셈결과 : {num1/num2}')
print(f'몫결과 : {num1//num2}')
print(f'나머지결과 : {num1%num2}')







#  19. 다양한 사람들로부터 개인정보를 입력받는 함수를 구현하세요.


# day1125이론2


def info(**data):
    for key,value in data.items():
        print(f'{key:6} => {value}')
info(age=12,phone='010-1111-2222',job='학생',loc='대구')




#  20. [나의 계산기] 프로그램을 구현하세요.



while True:
    print('------------------------------------------------------')
    print('<나의계산기>')
    print('------------------------------------------------------')
    print('1.입 력 2.덧 셈 3.뺄 셈')
    print('4.곱 셈 5.나 눗 셈 6.종 료')
    print('------------------------------------------------------')

    a = int(input('메뉴 선택(1~6): '))
    if a == 1:
        print('숫자 2개 입력 :(예: 1, 7)')
        num = input()
        b = int(num[0])
        c = int(num[3])
    elif a == 2:
        print(f'{b}+{c}={b+c}')
    elif a == 3:
        print(f'{b}-{c}={b-c}')
    elif a == 4:
        print(f'{b}*{c}={b*c}')
    elif a == 5:
        print(f'{b}/{c}={b/c}')
    elif a == 6:
        print(f'나의계산기 프로그램을 종료합니다.')
        break









# # 어떤 농장에서는 수박이 10kg이 넘으면 1등급, 그렇지 않고 7kg이 넘으면 2등급,
# # 그렇지 않고 4kg이 넘으면 3등급, 나머지는 4등급을 준다고 합니다.
# # 수학된 수박 무게를 입력 받아서 등급을 기준으로 수박 무게와 등급을 저장하세요.


# # 수박이 10kg이 넘으면 1등급, 그렇지 않고 7kg이 넘으면 2등급,그렇지 않고 4kg이 넘으면 3등급, 나머지는 4등급을 준다고 합니다.
# # 수학된 수박 무게를 입력 받아서 , 
# # 등급을 기준으로 수박 무게와 등급을 저장하세요.

# # fruit=int(input("수박의 무게를 입력하세요").strip())

# # if fruit>=10:
# #     print("1등급입니다.")
# # elif fruit>=7:
# #     print("2등급입니다.")
# # elif fruit>=4:
# #     print("3등급입니다.")
# # else:
# #     print("4등급입니다.")




# # 입력 받은 나이의 연령대를 출력하세요.
# # ( 영‧유아(0~5세), 아동(6~12세), 청소년(13~18세), 청년(19~29세), 중년(30~49세),
# # 장년(50~64세), 노년(65세 이상) )

# a=int(input("나이를 입력하세요 : "))

# if a>=65:
#     print("노년입니다.")
# elif a>=50:
#     print("장년입니다.")
# elif a>=30:
#     print("중년입니다.")
# elif a>=19:
#     print("청년입니다.")
# elif a>=13:
#     print("청소년입니다.")
# elif a>=6:
#     print("아동입니다.")
# else :
#     print("영유아입니다.")

#1번 
# 구구단 리스트컴프리핸션

i=5
a=[f'{i}*{j}={i*j}'for j in range(1,10)]
print(*a,sep='')






# 2번 코딩테스트

def addData(*datas):
    if len(datas)>0:  
        if isinstance(datas[0], str): 
            total= ''    
        else:
            total= 0

        for data in datas:
            total +=data

        return total

print(addData())
print(addData(1,3,5))
print(addData(True, True, False, False, True))
print(addData('A'))
print(addData('A','BC','Good'))




# 코딩 테스트 3번


배트맨={'국어':90,'수학':89,'윤리':98,'국사':99}
마징가={'국어':82,'수학':73,'윤리':71,'국사':91}
피오나={'국어':78,'수학':99,'윤리':91,'국사':83}

name = [배트맨,마징가,피오나]
name1 = ['배트맨','마징가','피오나']

for i in range(0,3):
    score = list(name[i].values())

    Mn = max(score)
    mn = min(score)

    indexM = score.index(Mn)
    indexm = score.index(mn)

    Ms = list(배트맨.keys())[indexM]
    ms = list(배트맨.keys())[indexm]

    print(f'[{name1[i]}] 최고 점수 : {Mn} {Ms} 최저 점수 : {mn} {ms}')





    print(f'--------------------------------------------------------------------')






베트맨={90:'국어',89:'수학',98:'윤리',99:'국사'}
마징가={82:'국어',73:'수학',71:'윤리',91:'국사'}
피오나={78:'국어',99:'수학',91:'윤리',83:'국사'}


print(f'[베트맨] 최고 점수 : {sorted(베트맨.items(), reverse=True)[0][0]} {sorted(베트맨.items(), reverse=True)[0][-1]}      \
    최저 점수 : {sorted(베트맨.items(), reverse=True)[-1][0]} {sorted(베트맨.items(), reverse=True)[-1][-1]}')

print(f'[베트맨] 최고 점수 : {sorted(마징가.items(), reverse=True)[0][0]} {sorted(마징가.items(), reverse=True)[0][-1]}      \
    최저 점수 : {sorted(마징가.items(), reverse=True)[-1][0]} {sorted(마징가.items(), reverse=True)[-1][-1]}')

print(f'[베트맨] 최고 점수 : {sorted(피오나.items(), reverse=True)[0][0]} {sorted(피오나.items(), reverse=True)[0][-1]}      \
    최저 점수 : {sorted(피오나.items(), reverse=True)[-1][0]} {sorted(피오나.items(), reverse=True)[-1][-1]}')





#동환님 방법
배트맨={90:'국어',89:'수학',98:'윤리',99:'국사'}
마징가={82:'국어',73:'수학',71:'윤리',91:'국사'}
피오나={78:'국어',99:'수학',91:'윤리',83:'국사'}
이름=[배트맨,마징가,피오나]
이름2=['배트맨','마징가','피오나']
for i in range(0,len(이름)):
    print('[',이름2[i],'] ',end='')
    print('최고 점수:',max(이름[i].keys()),이름[i].get(max(이름[i].keys())),\
         '  최저 점수:',min(이름[i].keys()),이름[i].get(min(이름[i].keys())))




# 베트맨={90:'국어',89:'수학',98:'윤리',99:'국사'}
# 마징가={82:'국어',73:'수학',71:'윤리',91:'국사'}
# 피오나={78:'국어',99:'수학',91:'윤리',83:'국사'}
# print(f'[베트맨] 최고점수:{max(베트맨.items())}       최저점수:{min(베트맨.items())}')
# print(f'[마징가] 최고점수:{max(마징가.items())}       최저점수:{min(마징가.items())}')
# print(f'[피오나] 최고점수:{max(피오나.items())}       최저점수:{min(피오나.items())}')






#4번
#코딩테스트 4번
id='930303-1234567' #input('주민번호 입력(000000-0000000): ')
A=[]
if int(id[7])==1 or int(id[7])==2:
    A.append(1)
    A.append(9)
else:
    A.append(2)
    A.append(0)
for i in id:
    if i.isdigit():
        A.append(int(i))
#나이
B=A[0]*1000+A[1]*100+A[2]*10+A[3]
print(f'{2022-B+1}세',end=', ')
#성별
if A[8]==1 or A[8]==3:print('남자',end=', ')
else: print('여자',end=', ')
#생년월일
print(f'{B}년{A[4]*10+A[5]}월{A[6]*10+A[7]}일',end=' ')
#띠
띠=['원숭이띠','닭띠','개띠','돼지띠','쥐띠','소띠','호랑이띠','토끼띠','용띠','뱀띠','말띠','양띠']
if B%12 ==0: print(띠[0],end=' ')
if B%12 ==1: print(띠[1],end=' ')
if B%12 ==2: print(띠[2],end=' ')
if B%12 ==3: print(띠[3],end=' ')
if B%12 ==4: print(띠[4],end=' ')
if B%12 ==5: print(띠[5],end=' ')
if B%12 ==6: print(띠[6],end=' ')
if B%12 ==7: print(띠[7],end=' ')
if B%12 ==8: print(띠[8],end=' ')
if B%12 ==9: print(띠[9],end=' ')
if B%12 ==10: print(띠[10],end=' ')
if B%12 ==11: print(띠[11],end=' ')
#별자리
C=A[4]*1000+A[5]*100+A[6]*10+A[7]
별자리=['물병자리','물고기자리','양자리','황소자리','쌍둥이자리','게자리','사자자리','처녀자리','천칭자리','전갈자리','궁수자리','염소자리']
if 120 <= C <=218: print(별자리[0])
if 219 <= C <=320: print(별자리[1])
if 321 <= C <=419: print(별자리[2])
if 420 <= C <=520: print(별자리[3])
if 521 <= C <=621: print(별자리[4])
if 622 <= C <=722: print(별자리[5])
if 723 <= C <=822: print(별자리[6])
if 823 <= C <=923: print(별자리[7])
if 924 <= C <=1022: print(별자리[8])
if 1023 <= C <=1122: print(별자리[9])
if 1123 <= C <=1224: print(별자리[10])
if 1225 <= C or C <=119: print(별자리[11])





#5번


def printMenu():
    print('-'*14)   
    print(' <영어변환기>')
    print('-'*14)
    print(' 1.입    력')
    print(' 2.대 문 자')
    print(' 3.소 문 자')
    print(' 4.코 드 화')
    print(' 5.종    료')
    print('-'*14)



isCheck=False
while True:
    #메뉴 출력
    printMenu()

    choice=input("메뉴 선택(1~5): ").strip()
    if choice=='5': 
        print('영어변환기 프로그램을 종료합니다.')
        break
    elif choice=='1':
        nums=input("숫자 2개 입력 :(예: 1, 7) ").strip()
        isCheck = True
    elif choice=='2': # 대문자
        if isCheck:
            print(nums.upper())
    elif choice=='3': # 소문자
        if isCheck:
            print(nums.lower())       
    elif choice=='4': # 코드화
        if isCheck:
            for s in nums:
                print(f'{hex(ord(s))}', end='')
            print()
        else:
            print("입력된 데이터가 없습니다.")      