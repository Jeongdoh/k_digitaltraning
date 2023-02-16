# ------------------------------------------------
# 복잡한 함수 => 활용도 높고 많이 사용됨
# ------------------------------------------------
# 숫자 2개 더하는 함수 ----------------------------
def addTwo(n1, n2):
    return n1+n2

# 숫자 5개 더하는 함수 ----------------------------
def addFivw(n1, n2, n3, n4, n5):
    return n1+n2+n3+n4+n5

# 숫자 4개 더하는 함수 ----------------------------
def addFour(n1, n2, n3, n4):
    return n1+n2+n3+n4 


# ------------------------------------------------
# 매개변수의 수가 인자의 수를 유동적으로 처리하는 함수
# => 가변인자 함수 
# => 매개변수의 형태 :  *변수명
# => 매개변수에 전달되는 인자 갯수 : 0개 ~ n개
# -------------------------------------------------
print()
print(10)
print(1,4,2,7,3,9)

# -------------------------------------------------
# 기    능 : 입력된 데이터를 모두 더하는 기능
# 함 수 명 :  addData
# 매개 변수 : *datas
# 반 환 값 :  덧셈 결과
# -------------------------------------------------
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
# print(addData(1,3,5))
# print(addData(1,'a',5))
# print(addData(True, True, False, False, True))
# print(addData('A'))
# print(addData('A','BC','Good'))
print(f'------------------------------------')
# -------------------------------------------------
# 기    능 : 입력된 숫자를 게산해주는 기능
# 함 수 명 :  calcNum
# 매개 변수:  *nums, -- 가변인자 숫자 
#             how   -- 계산방법 +, -, *
# 반 환 값 :  계산 결과
# -------------------------------------------------
def calcNum(how, *nums):
    if how=='+':
        print("덧셈")
    elif how=='-':
        print("뺄셈")
    elif how=='*':
        print('곱셈')
    else:
        print('지원하지 않는 계산입니다.')
        

# 함수 호출 ----------------------------------------
calcNum('+',10,20)
calcNum('-',10,20)
calcNum('-')
#calcNum()

print(f'------------------------------------')

# -------------------------------------------------
# 기    능 :  입력된 숫자를 게산해주는 기능
# 함 수 명 :  calc
# 매개 변수:  *nums, -- 가변인자 숫자 
#             how   -- 계산방법 
#                      기본계산 : + 
# 반 환 값 :  계산 결과
# -------------------------------------------------
def calc(*nums,how='+'):
    print(f'how : {how}, nums :{nums}')


calc()
calc(1,2,3,4, how='-')
calc(11,22,33)

print(1,2,'***')
print("----------------")

# --------------------------------------------
# 기본값 매개변수 
# 의미 : 함수 호출 시 인자를 주지 않을 경우 사용할 
#        값을 미리 정해둔 매내변수
# 형식 : 매개변수명=값
# 기본값 매개변수가 여러개 있는 경우는
# 함수 호출 시 매개변수명=값 지정 
# --------------------------------------------
def add(a, b=0, c=0):
    print(a, b, c)
    print("결과 :", a+b+c)

#add()    # 매개변수 a는 미입력시 사용할 값이 없음. 받드시 값 지정
add(5)     # a=5, b=0, c=0
add(5,3)   # a=5, b=3, c=0 
add(5,c=3) # a=5, b=0, c=3
add(5,3,7)

sorted([1,2,4], reverse=False)

print("----------------")

# --------------------------------------------
# 키워드 매개변수
# 의미 : 매개변수 데이터의 의미와 값을 함께 전달
#        호출 시 전달되는 인자의 갯수는 유동적 0~N개
# 형식 : **변수명
# -------------------------------------------
# 기    능 : 개인정보를 입력받아 저장하는 함수
# 함 수 명 : saveInfo
# 매개 변수: 사람마다 다름 => 데이터 종류 다름, 갯수 다름
#           가변, 데이터의미=값 **infos
# 반 환 값 : 저장된 데이터
# -------------------------------------------
print("----------------")

def saveInfo(**infos):
    print(type(infos), len(infos), infos)
    for k,v in infos.items():
        print(f'{k}-{v}')

    for key in infos.keys():
        print(f'{key} => {infos.get(key)}')

print("----------------")

# 키워드 파라미터 함수 호출 방법 ---------------
# 함수명(변수명1=값, ..., 변수명N=값)
print("----------------")

saveInfo(name='Hong')
saveInfo()
saveInfo(age=12, phone='010-2222-1111',job='학생', loc='대구')

print("----------------")

# --------------------------------------------
# 기본값 매개변수 
# 의미 : 함수 호출 시 인자를 주지 않을 경우 사용할 
#        값을 미리 정해둔 매내변수
# 형식 : 매개변수명=값
# 기본값 매개변수가 여러개 있는 경우는
# 함수 호출 시 매개변수명=값 지정 
# --------------------------------------------
def add(a, b=0, c=0):
    print(a, b, c)
    print("결과 :", a+b+c)

#add()    # 매개변수 a는 미입력시 사용할 값이 없음. 받드시 값 지정
add(5)     # a=5, b=0, c=0
add(5,3)   # a=5, b=3, c=0 
add(5,c=3) # a=5, b=0, c=3
add(5,3,7)

sorted([1,2,4], reverse=False)

# --------------------------------------------
# 반환값을 여러개 돌려주는 함수
# -------------------------------------------
# 기    능 : 4칙연산 수행 후 결과를 반환하는 함수
# 함 수 명 : fourCalc
# 매개 변수: num1, num2
# 반 환 값 : 뎃셈, 뺄셈, 곲셈, 나눗셈
# -------------------------------------------
def fourCalc(num1, num2):
    addValue=num1+num2
    subValue=num1-num2
    mulValue=num1*num2
    divValue=num1/num2 if num2>0 else 0

    return addValue, subValue, mulValue, divValue
print( type(fourCalc))

print("----------------")
