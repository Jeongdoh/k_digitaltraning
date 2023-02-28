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





cor(cancer_20_df$X2, cancer_20_df$X3)
cor(cancer_30_df$X2, cancer_30_df$X3)
cor(cancer_40_df$X2, cancer_40_df$X3)
cor(cancer_50_df$X2, cancer_50_df$X3)
cor(cancer_60_df$X2, cancer_60_df$X3)
cor(cancer_70_df$X2, cancer_70_df$X3)


# 위 코드는 각 연령대별 데이터프레임에서 X2와 X3의 상관관계를 계산하고 있습니다.

# cancer_20_df: 0.4988936 (약한 양의 상관관계)
# cancer_30_df: -0.2306078 (약한 음의 상관관계)
# cancer_40_df: -0.6835816 (뚜렷한 음의 상관관계)
# cancer_50_df: -0.7394686 (뚜렷한 음의 상관관계)
# cancer_60_df: -0.1702963 (약한 음의 상관관계)
# cancer_70_df: 0.7803566 (뚜렷한 양의 상관관계)
# 20대에서는 X2와 X3 사이에 약한 양의 상관관계가 있으며, 
# 30대부터는 음의 상관관계가 나타납니다. 
# 특히 40대부터는 뚜렷한 음의 상관관계가 나타나며, 
# 70대에서는 뚜렷한 양의 상관관계가 나타납니다. 
# 이러한 결과는 각 연령대별로 X2와 X3 간의 관련성이 다르게 나타날 수 있음을 시사합니다.







cor(cancer_20_df)
cor(cancer_30_df)
cor(cancer_40_df)
cor(cancer_50_df)
cor(cancer_60_df)
cor(cancer_70_df)

















library(ggplot2)

ggplot(cancer_20_df, aes(x=X2, y=X3, size=X1, color=X1)) + 
  geom_point() + 
  scale_size(range = c(2,6)) +
  labs(title="췌장암과 당뇨병 간의 상관관계 그래프", 
       x="췌장암", y="당뇨병") +
  theme(plot.title = element_text(hjust = 0.5))






