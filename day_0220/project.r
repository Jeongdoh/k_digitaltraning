# 1970년부터 2015년까지 기대수명 대 의료비 지출
# 보건 금융은 연간 1인당 보건 지출로 보고되며 국가 간 인플레이션과 물가 수준 차이에 따라 조정됩니다


# 데이터 전처리 할 것 없음

# 파일 불러와서 health_df변수에 저장
health_df<-read.csv("day_0220/healthexp.txt")

# 파일 확인
str(health_df)

# 결측치 확인
is.na(health_df)
sum(is.na(health_df))

health_df

# 컬럼확인
colnames(health_df)



# 탐색적데이터 분석 수행 및 시각화

mean(health_df$Spending_USD)
which.max(health_df$Spending_USD)






# 최대비용 지출한 나라 찾기
max_spending<-health_df[which.max(health_df$Spending_USD),"Country"]
# health_df 데이터셋에서 Spending_USD 변수에서 최대값을 가지는 행을 찾고, 해당 행의 Country 변수 값을 출력.

# which.max() 함수는 최대값을 가지는 원소의 인덱스를 반환.
# 따라서 which.max(health_df$Spending_USD)는 Spending_USD 변수에서 최대값을 가지는 행의 인덱스를 반환. 
# health_df[which.max(health_df$Spending_USD), "Country"]는 해당 행의 Country 변수 값을 반환. 


# 결과 출력
cat("가장 많은 지출을 한 나라", max_spending, "\n")
# cat() 함수는 출력할 문자열을 연결하여 출력하는 함수. print와 비슷함.


# 최고 기대수명 나라 찾기
max_long<-health_df[which.max(health_df$Life_Expectancy),"Country"]
# 결과 출력
cat("가장 높은 기대수명 국가", max_long, "\n")





# Spending_USD 에서 가장 평균값이 높은 나라 구하기
library(dplyr)

health_df %>%
  group_by(Country) %>%
  summarise(mean_spending = mean(Spending_USD, na.rm = TRUE)) %>%
  arrange(desc(mean_spending)) %>%
  head(3)

# dplyr 패키지의 group_by() 함수를 사용하여 국가별로 그룹화한 후,
# summarise() 함수를 사용하여 각 그룹의 Spending_USD의 평균값을 계산.
# 그리고 arrange() 함수를 사용하여 평균값이 큰 순으로 정렬하고,
# head() 함수를 사용하여 보고싶은 상위 n개 나라의 정보만을 출력.




#기술적 분석기법 적용

# ggplot2 패키지 불러오기
library(ggplot2)

# Spending_USD, Life_Expectancy 관계그래프 그리기
ggplot(data = health_df, aes(x = Spending_USD, y = Life_Expectancy)) + geom_point()




# 각 국의 기대수명 그래프 그리기
#ggplot 사용

ggplot(health_df, aes(x=Year, y=Life_Expectancy, color=Country)) + 
  geom_line() + 
  labs(title="Life Expectancy vs. Year by Country", x="Year", y="Life Expectancy", color="Country")

# aes(): ggplot() 함수 내에서 aesthetic mappings을 설정. x=Year, y=Life_Expectancy, color=Country는 
# 각각 x축, y축, 색상 aesthetic mapping을 설정.

# geom_line()은 선 그래프를 그리기 위한 함수. 선 그래프는 x와 y 값을 연결하여 그래프를 그리는 방식.

# labs() 함수는 그래프의 제목, x축 레이블, y축 레이블, 색상 범례 레이블을 지정.

# title: 그래프의 제목을 지정.
# x: x축 레이블을 지정.
# y: y축 레이블을 지정.
# color: 색상 범례 레이블을 지정.




# 각 나라별 그래프
#library중 하나인 gridExtra 사용
library(gridExtra)

# 그래프 그리기
ggplot(health_df, aes(x = Year, y = Life_Expectancy)) +
  geom_line() +
  facet_wrap(~Country, ncol = 3) +
  labs(title = "Life Expectancy vs. Year by Country", x = "Year", y = "Life Expectancy")


# aes(): ggplot() 함수 내에서 aesthetic mappings을 설정합니다. x=Year, y=Life_Expectancy, color=Country는 
# 각각 x축, y축, 색상 aesthetic mapping을 설정.

# geom_line()은 선 그래프를 그리기 위한 함수. 선 그래프는 x와 y 값을 연결하여 그래프를 그리는 방식.

# labs() 함수는 그래프의 제목, x축 레이블, y축 레이블, 색상 범례 레이블을 지정.

# title: 그래프의 제목을 지정.
# x: x축 레이블을 지정.
# y: y축 레이블을 지정.
# color: 색상 범례 레이블을 지정.






#통계적 분석기법 적용


# Spending_USD와 Life_Expectancy의 상관계수 구하기

# Pearson 상관계수 계산
result <- cor.test(health_df$Spending_USD, health_df$Life_Expectancy, method = "pearson")

# 결과 출력
cat("Pearson 상관계수:", result$estimate, "\n")
cat("p-value:", result$p.value, "\n")

#상관분석
cor(health_df$Spending_USD,health_df$Life_Expectancy)

# 결과
#상관계수: 0.5794305의 수치결과 상관관계가 있다고 보여짐



#가설 설정 및 검정 진행

# 가설 설정1 (의료비 지출이 가장 높은 나라는 미국일 것이다.(세계경제를 주도하기 때문))
ggplot(health_df, aes(x=Spending_USD, y=Life_Expectancy, color=Country)) + geom_point()
# geom_point 함수를 사용하여 Spending_USD 변수를 x축에,
# Life_Expectancy 변수를 y축에 배치한 산점도를 그리며,
# color 매개변수를 사용하여 국가별로 다른 색상으로 표시함.

# 의료비 지출은 미국이 가장 많다.





# 가설 설정2 (의료비 지출이 높은 국가는 평균 수명이 높을 것이다.)

# 미국 데이터 추출
us_health_exp <- subset(health_df, Country == "USA")
us_health_exp
# Spending_USD 평균값 계산
us_spending_mean <- mean(us_health_exp$Spending_USD)
us_spending_mean
# Life_Expectancy 평균값 계산
us_life_exp_mean <- mean(us_health_exp$Life_Expectancy)
us_life_exp_mean
# t-검정 수행
t.test(us_health_exp$Spending_USD, us_health_exp$Life_Expectancy)


#위와 결과 같음

# 값만 t검정

# 미국의 Spending_USD와 Life_Expectancy 추출
us_data <- health_df[health_df$Country == "USA", c("Spending_USD", "Life_Expectancy")]
us_data
# t-test 수행
t.test(us_data$Spending_USD, us_data$Life_Expectancy)

# 의료비 지출이 많은 국가와 평균수명과의 t검정 결과는 p-value = 3.538e-12로 없어보임





# 가설 설정3 (코로나로 인해 모든 나라는 2020년에 수명이 줄었을 것이다.)


# 그래프 결과
ggplot(health_df, aes(x=Year, y=Life_Expectancy, color=Country)) + 
  geom_line() + 
  labs(title="Life Expectancy vs. Year by Country", x="Year", y="Life Expectancy", color="Country")



# 일본 데이터 추출하기
japan_data <- health_df %>%
  filter(Country == "Japan")
japan_data
# Spending_USD 값과 Life_Expectancy 값의 t-검정 수행
t_test_result <- t.test(japan_data$Spending_USD, japan_data$Life_Expectancy)

# 결과 출력
t_test_result


# 다른 나라 모두 수명이 줄었는데 일본만 그대로...까비...
# 다른 의미로 보면 그만큼 고령화 되었다고 볼 수도 있음

# 일본의 Spending_USD 값과 Life_Expectancy 값의 t-검정 수행시 
#p-value = 1.573e-11 이 나왔기 때문에 의료비 지출과 기대수명은 연관이 없다고 생각함








#결과 도출 및 설명

# health_df의 Spending_USD와 Life_Expectancy의 상관분석시
# 상관계수: 0.5794305의 수치결과 상관관계가 있다고 보여진다.


# 의료비 지출은 미국이 가장 많지만,
# 의료비 지출이 많다고 해서 기대수명이 높은 것은 아니다.
# 다른 요인이 작용할수도 있을 것 ((예) 미국은 총기 합법화...)



# 코로나로 인해 모든 나라는 2020년에 수명이 줄었을 것이라 예상했는데
# 어느정도는 맞는 말(미국, 영국, 독일, 캐나다)이지만 안타깝게도 일본은 코로나로 인한 기대수명에 영향이 없어보임.
# 아니면 일본의 인구가 고령화 되었기 때문일 수도 있고, 거짓 통계일지도..

#끗


























