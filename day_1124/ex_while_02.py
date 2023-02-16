# -------------------------------------
# while 반복문
# -------------------------------------

#1~50까지 숫자에 3을 곱해서 출력해 주세요.
num=1
while num<=50:
    print(num*3)
    #num=num+1
    num += 1

# 입력받은 수 만큼 Hello를 출력하세요.
count=3 #input("반복 횟수 : ").strip()

count=int(count)

# 다운(down) 카운팅 방식 -------------
while count>0:
    print('Hello', count)
    count-=1

# 업(Up) 카운팅 방식 -----------------
num=1
while num<=count:
    print('Hello')
    num+=1

# ------------------------------------------
# 반복 중단하기 => break
# 반복 중 조건에 해당하는 경우 즉시 반복을 중단
# break 가장 가까이 있는 반복문 중단 
# ------------------------------------------

# 1~30 사이의 숫자 중에서 3의 배수이면서 5의 배수인
# 숫자가 나오면 중단하세요.
num=1
while num<=30:
    if num%15==0: break
    #if not num%15: break
    print(num)
    num+=1

print('---- END ----')    

for n in range(1,31):
    if (n%3==0) and (n%5==0): break
    print(n)

print('---- END ----')     

# ------------------------------------------
# 중첩 반복문과 반복 중단하기 => break
# break 가장 가까이 있는 반복문 중단 
# 반복문 안에 반복문이 있는 경우 모든 반복 중단 X
# ------------------------------------------
#          1,2,3,..,10  
# 내부 반복문이 중단(break)되었는지 정보를 담는 변수
isBreak=False   

for num in range(1, 11):
    # 내부 반복의 중단여부 확인 후 
    # 중단되었다면 중단시켜줌
    if isBreak: break

    print(f'----{num}')
    for data in ['A', 'B', 'C', 'D']:
        # C인경우 반복 중단
        if data=='C': 
            isBreak=True
            break
        print(data)

# 사용자로부터 데이터를 입력 받아서 리스트에 저장
# 종료시 Q/q 입력시 입력 받기 종료
datas=[]    # 입력 데이터 저장 변수      
while True:
    data=input("저장 데이터 입력 (종료 : Q/q) ").strip()

    if data in ['Q','q']: 
        print('프로그램을 종료합니다.')
        break
    else:
        datas.append(data)

# --------------------------------------
# 반복문에서 코드 실행을 스킵하고 다음으로
# 진행하도록 하는 키워드 => continue
# 해당 키워드 아래 코드는 스킵        
# --------------------------------------     
# 1~30까지 숫자를 출력하는데 3의 배수는 출력하지 말고
# 나머지 숫자만 출력해 주세요.
num=1
while num<=30:
    if num%3:
        print(num)  
    num+=1 
print(f'---------------------------------------')
num=0
while num<30:
    num+=1  
    if not num%3: 
        continue
    print(num)  
          
print(f'---------------------------------------')

for n in range(1,31):
    if n%3:
        print(n)   
print(f'---------------------------------------')

for n in range(1,31):
    if not n%3: continue
    print(n)           
