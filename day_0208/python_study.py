#문제1.while문을 이용하여 다음처럼 별찍기를 하세요.

while 1:
    for i in range(1,6):
        print(i*'*')
    break


#문제2. fruits = ["사과", "귤", "수박", “딸기”, “바나나”]에서 요소를 while 반복문 사용하여 모두 출력하세요.

fruits = ["사과", "귤", "수박", "딸기", "바나나"]

while 1:
    for i in fruits:
        print(i)
    break


#문제3.두 정수 A와 B를 입력받은 다음 A+B를 출력하는 프로그램을 작성하세요.
#      A, B 모두 0이 들어올때까지 무한 반복하고 A,B 모두 0이 들어오면 멈춥니다.


while 1:
    num1=int(input("A를 입력하세요 : ").strip())
    num2=int(input("B를 입력하세요 : ").strip())
    if num1==0 and num2==0:
        print("입력받은 숫자 모두 0입니다.")
        break
    else:
        print(num1+num2)

#문제4. 1부터 100사이의 모든 3의 배수의 합을 계산하여 출력하세요.
while 1:
    a=[]
    for i in range(1,101):
        if i%3==0:
            a.append(i)
    print(sum(a))
    break

#문제5. 정수 안의 각 자리수의 합을 계산하여 출력하세요.. 예를 들어서 1234라면 (1+2+3+4) 10이 출력되어야 합니다.

while 1:
    a=int(input("정수 입력 : ").strip())
    b=int(input("정수 입력 : ").strip())
    c=int(input("정수 입력 : ").strip())
    d=int(input("정수 입력 : ").strip())

    print(f"네 수의 덧  셈 : {a+b+c+d}")
    print(f"네 수의 뺄  셈 : {a-b-c-d}")
    print(f"네 수의 곱  셈 : {a*b*c*d}")
    print(f"네 수의 나눗셈 : {a/b/c/d}")
    break
