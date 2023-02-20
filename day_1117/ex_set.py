# ----------------------------------------------
# Set 타입 : 마지막에 추가된 자료형
#          - 중복 데이터 불허 *가장 중요한 특징
#          - 인덱스 없음, 키 없음
#          - 여러 종류의 여러개의 데이터 저장 
# - 형식 : {데이터1,데이터2, ..., 데이터N}
#          set( 데이터 어려개 )
# - 중복 제거에 활용
# - 데이터 타입 끼리 데이터 비교 시에 사용
# - 합집합, 교집합, 차집합 기능 제공
# ----------------------------------------------

# set 객체 생성----------------------------------
data1=set()  # 비어 있는 set 타입
data2={1,3,5,2,1,4,2}
data3=set('Hello')

print('data1 => 타입: %s, 개수: %s' %(type(data1), len(data1)), data1)
print('data2 => 타입: %s, 개수: %s' %(type(data2), len(data2)), data2)
print('data3 => 타입: %s, 개수: %s' %(type(data3), len(data3)), data3)

# ------------------------------------------------
#집합 기능 다루기
# ------------------------------------------------
# 1 ~ 10 범위의 2의 배수로 구성된 데이터 생성
s1=set([2,4,6,8,10])
s1={2,4,6,8,10}
s1=set(range(2,11,2))

# 1 ~ 10 범위의 5의 배수로 구성된 데이터 생성
s2=set([5,10])
s2={5,10}
s2=set(range(5,11,5))

print(f's1 => {s1}, s2 =>{s2}')

# 2개 데이터에 공통된 데이터를 출력하기-------------
# 교집합 => 연산자 &
print(f'공통 데이터 : {s1 & s2}')

# 2개 데이터의 모든 데이터 단 중복 제거하고 출력-----
# 합칩합 => 연산자 |
print(f'모든 데이터 : {s1 | s2}')

# S1에만 존재하는 데이터 출력-----------------------
# 차집합 => 연산자 -
print(f'S1만의 데이터 : {s1 - s2}')

# -----------------------------------------------
# 합집한, 교집합, 차집환 관련 메서드
# -----------------------------------------------
print(f'공통 데이터 : {s1 & s2} - {s1.intersection(s2)}')
print(f'모든 데이터 : {s1 | s2} - {s1.union(s2)}')
print(f'S1만 데이터 : {s1 - s2} - {s1.difference(s2)}')
