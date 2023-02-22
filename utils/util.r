#-----------------------------------------------------------
# 공통으로 자주 사용되는 함수들
#-----------------------------------------------------------

# 객체의 기본 정보 출력 기능 함수----------------
displayInfo<-function(data){
    print("TEST")
    str(data)
    summary(data)
}


# 결측치 체크 기능 함수------------------------------
checkNa<-function(data){
    eNum<-sum(is.na(data))
    rNum<-sum(!complete.cases(data))
    print(paste("원소 Na :",eNum,"행 NA",rNum,sep = " - "))
}

library(stringr)


# 최빈값 체크 기능 함수----------------------------------------
checkMode<-function(data){
    for(col in colnames(data))
    {
        # 컬럼별 빈도표 >> 최대값
        max(table(data[col]))           # 가장 많은 숫자
        maxIdx<-which.max(table(data[col]))     # 인덱스
        maxValue<-names(which.max(table(data[col])))     # 가장 많이 나온 값

        print(paste(col,"최빈값 : ", maxValue))
    }
}


# 이상치 체크 함수
# 여러개
# 과제


# 이상치 체크 기능 함수-------------------------------------
# 과제 => 여러개

# 전체 데이터의 상관계수 체크기능 함수------------------------
# 매개변수 => 데이터 객체, 기준 컬럼명
checkCor<-function(data){

}