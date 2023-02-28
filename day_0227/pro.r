library("ggplot2")


con_df <- read.csv("day_0227\\ex_shiny\\app_lay\\cancer.csv")
head(con_df)


dang_df<-read.csv("day_0227\\ex_shiny\\app_lay\\dang.csv")
dang_df



apply(con_df[,7:8],1,sum)
con_df["19~29세"]=apply(con_df[,7:8],1,sum)
con_df["30~39세"]=apply(con_df[,9:10],1,sum)
con_df["40~49세"]=apply(con_df[,11:12],1,sum)
con_df["50~59세"]=apply(con_df[,13:14],1,sum)
con_df["60~69세"]=apply(con_df[,15:16],1,sum)
con_df["70세이상"]=apply(con_df[,17:21],1,sum)

con_df<-con_df[,c(1,2,22:27)]
con_df
dang_df
colnames(con_df)
colnames(dang_df)

df<-




# 데이터프레임 합치기
merged_df <- merge(con_df, dang_df, by = c("성별", "시점"))

# 회귀분석 실행
lm_result <- lm(성별 ~ ., data = merged_df)

# 회귀분석 결과 출력
summary(lm_result)




cancer_20_df <- data.frame(cbind(con_df$"성별",con_df$"19~29세",dang_df$"X19.29세"))
cancer_20_df

cancer_30_df <- data.frame(cbind(con_df$"성별",con_df$"30~39세",dang_df$"X30.39세"))
cancer_30_df

cancer_40_df <- data.frame(cbind(con_df$"성별",con_df$"40~49세",dang_df$"X40.49세"))
cancer_40_df

cancer_50_df <- data.frame(cbind(con_df$"성별",con_df$"50~59세",dang_df$"X50.59세"))
cancer_50_df

cancer_60_df <- data.frame(cbind(con_df$"성별",con_df$"60~69세",dang_df$"X60.69세"))
cancer_60_df

cancer_70_df <- data.frame(cbind(con_df$"성별",con_df$"70세이상",dang_df$"X70세이상"))
cancer_70_df



cancer_20_df$X1<-as.integer(cancer_20_df$X1)
cancer_20_df$X2<-as.integer(cancer_20_df$X2)
cancer_20_df$X3<-as.integer(cancer_20_df$X3)


cancer_30_df$X1<-as.integer(cancer_30_df$X1)
cancer_30_df$X2<-as.integer(cancer_30_df$X2)
cancer_30_df$X3<-as.integer(cancer_30_df$X3)

cancer_40_df$X1<-as.integer(cancer_40_df$X1)
cancer_40_df$X2<-as.integer(cancer_40_df$X2)
cancer_40_df$X3<-as.integer(cancer_40_df$X3)

cancer_50_df$X1<-as.integer(cancer_50_df$X1)
cancer_50_df$X2<-as.integer(cancer_50_df$X2)
cancer_50_df$X3<-as.integer(cancer_50_df$X3)

cancer_60_df$X1<-as.integer(cancer_60_df$X1)
cancer_60_df$X2<-as.integer(cancer_60_df$X2)
cancer_60_df$X3<-as.integer(cancer_60_df$X3)

cancer_70_df$X1<-as.integer(cancer_70_df$X1)
cancer_70_df$X2<-as.integer(cancer_70_df$X2)
cancer_70_df$X3<-as.integer(cancer_70_df$X3)


str(cancer_20_df)




cancer_20_df
cancer_30_df
cancer_40_df
cancer_50_df
cancer_60_df
cancer_70_df





cancer_20_man<-cancer_20_df[1:10,]
cancer_20_woman<-cancer_20_df[11:20,]
cancer_20_man

cancer_30_man<-cancer_30_df[1:10,]
cancer_30_woman<-cancer_30_df[11:20,]


cancer_40_man<-cancer_40_df[1:10,]
cancer_40_woman<-cancer_40_df[11:20,]


cancer_50_man<-cancer_50_df[1:10,]
cancer_50_woman<-cancer_50_df[11:20,]


cancer_60_man<-cancer_60_df[1:10,]
cancer_60_woman<-cancer_60_df[11:20,]


cancer_70_man<-cancer_70_df[1:10,]
cancer_70_woman<-cancer_70_df[11:20,]

cancer_man<-c(cancer_20_man,cancer_30_man,cancer_40_man,cancer_50_man,cancer_60_man,cancer_70_man)
cancer_man<-data.frame(cancer_man)
cancer_man

cancer_woman<-c(cancer_20_woman,cancer_30_woman,cancer_40_woman,cancer_50_woman,cancer_60_woman,cancer_70_woman)
cancer_woman<-data.frame(cancer_woman)
cancer_woman





cor(cancer_man$X2,cancer_man$X3)
cor(cancer_woman$X2,cancer_woman$X3)

cor(cancer_man$X2.1,cancer_man$X3.1)
cor(cancer_woman$X2.1,cancer_woman$X3.1)

cor(cancer_man$X2.2,cancer_man$X3.2)
cor(cancer_woman$X2.2,cancer_woman$X3.2)

cor(cancer_man$X2.3,cancer_man$X3.3)
cor(cancer_woman$X2.3,cancer_woman$X3.3)

cor(cancer_man$X2.4,cancer_man$X3.4)
cor(cancer_woman$X2.4,cancer_woman$X3.4)

cor(cancer_man$X2.5,cancer_man$X3.5)
cor(cancer_woman$X2.5,cancer_woman$X3.5)



# 20대 남 회귀분석
model2 <- lm(cancer_man$X2 ~ cancer_man$X3, data = cancer_man)
# 회귀분석 결과 출력
summary(model2)

# 20대 여 회귀분석
model22 <- lm(cancer_woman$X2 ~ cancer_woman$X3)
# 회귀분석 결과 출력
summary(model22)



# 30대 남 회귀분석
model3 <- lm(cancer_man$X2.1~cancer_man$X3.1)
# 회귀분석 결과 출력
summary(model3)

# 30대 여 회귀분석
model33 <- lm(cancer_woman$X2.1~cancer_woman$X3.1)
# 회귀분석 결과 출력
summary(model33)



# 40대 남 회귀분석
model4 <- lm(cancer_man$X2.2~cancer_man$X3.2)
# 회귀분석 결과 출력
summary(model4)

# 40대 여 회귀분석
model44 <- lm(cancer_woman$X2.2~cancer_woman$X3.2)
# 회귀분석 결과 출력
summary(model44)



# 50대 남 회귀분석
model5 <- lm(cancer_man$X2.3~cancer_man$X3.3)
# 회귀분석 결과 출력
summary(model5)

# 50대 여 회귀분석
model55 <- lm(cancer_woman$X2.3~cancer_woman$X3.3)
# 회귀분석 결과 출력
summary(model55)



# 60대 남 회귀분석
model6 <- lm(cancer_man$X2.4~cancer_man$X3.4)
# 회귀분석 결과 출력
summary(model6)

# 60대 여 회귀분석
model66 <- lm(cancer_woman$X2.4~cancer_woman$X3.4)
# 회귀분석 결과 출력
summary(model66)



# 70대 남 회귀분석
model7 <- lm(cancer_man$X2.5~cancer_man$X3.5)
# 회귀분석 결과 출력
summary(model7)

# 70대 여 회귀분석
model77 <- lm(cancer_woman$X2.5~cancer_woman$X3.5)
# 회귀분석 결과 출력
summary(model77)

