# 1. for 문을 이용하여 구구단 1단부터 9단까지 출력하는 코드를 작성하시오.
for (i in 1:9)
    for (j in 1:9){
    cat(i,'*',j,'=',i*j,'\n')
}


# 2. 1번의 구구단 출력을 아래와 같이 진행하여 보시오 (탭이 안되시면 띄어쓰기로)
for (i in 1:9)
    for (j in 1:9){
    cat(i,'*',j,'=',i*j,'\n')
}




# 3. while 문과 조건문을 이용하여 아래와 같이 출력하는 코드를 작성하시 오

a=1

while (a<=5){
     if(a%%2==0){
        cat(rep('*',3),rep(' ',4),rep('*',3),end='\n')
    }else if(a%%3==0){
        cat(rep('*',10),end='\n')
    }else if (a%%2==1){
        cat(rep('*',1),rep(' ',8),rep('*',1),end='\n')
    
}
a=a+1
}


# 4. 1에서 부터 100까지 차례로 더해 나갈 때, 처음으로 합이 1000을 넘게 만드는 수는 무엇인지 for문과 if문 그리고
# break 문을 이용하여 구하여라. 또한 처음으로 1000을 넘었을 때, 누적합은 얼마인지 구하여라. 
s=0
for (i in seq(1,100)){
    s=s+i
    if (s>=1000){
        break
    }
}
s


# 5. 반복문을 이용하여 50에서 100까지의 합을 계산할 때, 짝수의 합을 계 산하는 코드를 작성하시오. 
# (단, next 함수를 써서 작성 하시오.) 
s=0
for (i in seq(50,100)){
    if (i%%2==1){
        next
    }
    s=s+i
    }
s



# 6. 하나의 벡터를 입력 받아 벡터의 길이, 원소의 합, 최솟값, 최댓값, 평균, 분산을 반환하는 함수를
# 작성하고 x = 1:10에 대한 결과 를 확인하시오.
vvv <- function(x) {
return(list(length_x=length(x),sum_x=sum(x),min_x=min(x),max_x=max(x),mean_x=mean(x),var_x=var(x)))
}


x=1:10
vvv(x)

# 7. 6에서 작성한 함수에 새로운 인수를 추가하여 1인 경우 벡터의 길이, 2 인 경우 원소의 합과 같이 특정 값을
# 선택할 수 있도록 함수를 수정하 시오. x=1:10의 값을 이용하여 각각의 경우에 대해서 결과를 확인하시오.

# 여러 값에 대하여 각각 다른 처리를 하고자 할 때 사용
# switch(변수,1에 해당 표현식, 2에 해당 표현식, ...)
vvv <- function(x,another) {
return(switch(another,length_x=length(x),sum_x=sum(x),min_x=min(x),max_x=max(x),mean_x=mean(x),var_x=var(x)))
}


x=1:10
vvv(x,5)


# 8. 7에서 작성한 함수에서 새로운 인수를 생략 시 원소의 합이 출력하도록 default 설정을 적용하시오.

vvv <- function(x,another) {
return(switch(another,length_x=length(x),sum_x=sum(x),min_x=min(x),max_x=max(x),mean_x=mean(x),var_x=var(x)))
}


x=1:10
vvv(x,5)



# 9. 1 – 9 사이의 숫자 2개를 입력 받아 작은 수 부터 큰 수까지의 구구단을 출력하는 함수를 작성하시오. 
# (ex, 3과 4를 입력 시)






