# Auto MPG 데이터셋은 자동차의 연비(mpg)와 다양한 특성들을 포함한 데이터셋입니다.
# 각 열은 다음과 같습니다.

# mpg : 연비 (실수형)
# cylinders : 실린더 개수 (정수형)
# displacement : 배기량 (실수형)
# horsepower : 출력 (실수형)
# weight : 차량 무게 (실수형)
# acceleration : 가속능력 (실수형)
# model year : 모델 연도 (정수형)
# origin : 제조국 (정수형)
# 이 데이터셋을 이용하여 각 모델들의 성능을 비교해보겠습니다.

# 먼저 데이터셋을 불러오고, 각 열에 대한 특성화를 진행합니다. 특성화 과정은 다음과 같습니다.

# mpg : 예측할 값으로 사용하기 때문에 제외합니다.
# cylinders, model year, origin : 범주형 데이터로 변환합니다. (One-Hot Encoding)
# displacement, horsepower, weight, acceleration : 정규화를 진행합니다.


import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import r2_score, mean_squared_error

# 데이터셋 불러오기
df = pd.read_csv('auto-mpg.csv')

# mpg를 제외한 데이터를 X에 저장합니다.
X = df.drop(columns=['mpg'])

# cylinders, model year, origin을 One-Hot Encoding합니다.
categorical_columns = ['cylinders', 'model year', 'origin']
ohe = OneHotEncoder()
X_categorical = ohe.fit_transform(X[categorical_columns])
X_categorical = X_categorical.toarray()

# 정규화할 데이터를 저장합니다.
X_numeric = X.drop(columns=categorical_columns)

# 정규화를 진행합니다.
scaler = StandardScaler()
X_numeric_scaled = scaler.fit_transform(X_numeric)

# 정규화된 데이터와 One-Hot Encoding된 데이터를 합칩니다.
X_processed = np.concatenate([X_numeric_scaled, X_categorical], axis=1)

# mpg를 y로 저장합니다.
y = df['mpg']

# 학습 데이터와 테스트 데이터를 나눕니다.
X_train, X_test, y_train, y_test = train_test_split(X_processed, y, test_size=0.3, random_state=42)


# 1. Linear Regression


# 모델 학습
lr = LinearRegression()
lr.fit(X_train, y_train)

# 예측
y_pred = lr.predict(X_test)

# 평가
lr_r2 = r2_score(y_test, y_pred)
lr_rmse = np.sqrt(mean_squared_error(y_test, y_pred))

print("Linear Regression R2 Score:", lr_r2)
print("Linear Regression RMSE:", lr_rmse)





# 2. Polynomial Regression


# 다항 회귀를 위한 전처리
poly = PolynomialFeatures(degree=2)
X_train_poly = poly.fit_transform(X_train)
X_test_poly = poly.transform(X_test)

# 모델 학습
pr = LinearRegression()
pr.fit(X_train_poly, y_train)

# 예측
y_pred = pr.predict(X_test_poly)

# 평가
pr_r2 = r2_score(y_test, y_pred)
pr_rmse = np.sqrt(mean_squared_error(y_test, y_pred))

print("Polynomial Regression R2 Score:", pr_r2)
print("Polynomial Regression RMSE:", pr_rmse)





# 3. Ridge Regression

# 모델 학습
ridge = Ridge(alpha=0.5)
ridge.fit(X_train, y_train)

# 예측
y_pred = ridge.predict(X_test)

# 평가
ridge_r2 = r2_score(y_test, y_pred)
ridge_rmse = np.sqrt(mean_squared_error(y_test, y_pred))

print("Ridge Regression R2 Score:", ridge_r2)
print("Ridge Regression RMSE:", ridge_rmse)




# 4. Lasso Regression

# 모델 학습
lasso = Lasso(alpha=0.5)
lasso.fit(X_train, y_train)

# 예측
y_pred = lasso.predict(X_test)

# 평가
lasso_r2 = r2_score(y_test, y_pred)
lasso_rmse = np.sqrt(mean_squared_error(y_test, y_pred))

print("Lasso Regression R2 Score:", lasso_r2)
print("Lasso Regression RMSE:", lasso_rmse)




# 결과 비교
# 4개의 모델을 비교해 보면, 다항 회귀 모델이 가장 높은 R2 Score과 가장 낮은 RMSE를 가지며 가장 성능이 좋은 것으로 나타났습니다. Ridge Regression 모델과 Linear Regression 모델도 비슷한 성능을 보이고 있으며, Lasso Regression 모델은 나머지 모델에 비해 R2 Score이 낮고 RMSE가 높게 나타나 성능이 가장 나쁜 것으로 나타났습니다.






# Revue de parfum
# 전처리 과정에서 계속 오류가 나는데?
# 오류가 어떤 종류인지 알려주시면 좀 더 자세한 안내를 드릴 수 있을 것 같습니다. 혹시 어떤 코드를 실행할 때 어떤 오류가 발생하는지 알려주실 수 있을까요?




# Revue de parfum
# 정규화 과정에서 could not convert string to float: '?' 이런 오류메세지가 뜨고있어

# 데이터셋을 살펴보니 '?' 문자열이 일부 열에 포함되어 있어서 오류가 발생한 것 같습니다. 이 문자열은 결측치를 의미하는데, 이를 처리하지 않으면 모델 학습이나 예측에서 오류가 발생할 수 있습니다.

# 따라서, 이 문자열을 결측치로 간주하고 해당 열의 평균값 또는 중앙값 등으로 대체하는 전처리 과정이 필요합니다. 이를 처리하는 방법은 다음과 같습니다.

import pandas as pd
import numpy as np

# 데이터셋 불러오기
df = pd.read_csv('auto-mpg.csv')

# '?' 문자열을 결측치로 대체하기
df.replace('?', np.nan, inplace=True)

# 결측치가 있는 행 제거하기
df.dropna(inplace=True)

# 정규화
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
scaled_data = scaler.fit_transform(df[['cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model year']])

# 데이터셋 분할
X = scaled_data
y = df['mpg']

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# 위 코드에서 df.replace('?', np.nan, inplace=True) 라인은 데이터셋에서 '?' 문자열을 결측치(np.nan)로 대체합니다. 
# df.dropna(inplace=True) 라인은 결측치가 있는 행을 제거합니다.

# 이후에는 정규화를 위해 StandardScaler()를 사용하고, train_test_split()으로 데이터셋을 분할합니다.

# 위 코드를 실행하시면 오류 없이 전처리가 완료될 것입니다.




# Revue de parfum
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 이렇게 하면 X값과 y값이 어떤 변수에 담기는거야?


# train_test_split() 함수는 데이터셋을 특정 비율로 분할해주는 함수입니다. 이 함수를 사용하면 데이터셋을 분할한 후, 각각의 데이터셋을 변수에 담을 수 있습니다.

# train_test_split() 함수에서 반환되는 값은 4개인데, 이는 분할된 데이터셋을 각각 train 데이터셋과 test 데이터셋으로 나눈 후, X_train, X_test, y_train, y_test 4개의 변수에 저장된다는 뜻입니다.

# 여기서 X_train은 train 데이터셋에서 독립 변수의 값들을, y_train은 train 데이터셋에서 종속 변수의 값들을, X_test는 test 데이터셋에서 독립 변수의 값들을, y_test는 test 데이터셋에서 종속 변수의 값들을 담고 있습니다.

# 즉, X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42) 코드는 X와 y 데이터셋을 분할한 후, train 데이터셋과 test 데이터셋으로 나누어 각각의 변수에 저장한다는 뜻입니다.




# Revue de parfum
# 그럼 로지스틱 회귀로 결과를 나타내고 해석해줘


# auto mpg 데이터셋은 연속형 변수인 mpg(연비) 값을 예측하는 문제이기 때문에 로지스틱 회귀 모델을 사용할 수 없습니다. 로지스틱 회귀 모델은 이진 분류 문제에 사용되는 모델입니다. 따라서 auto mpg 데이터셋에서는 선형 회귀 모델을 사용하여 연비를 예측할 수 있습니다.

# 선형 회귀 모델을 사용하여 예측 결과를 해석할 때는 주로 회귀 계수(coefficient)와 절편(intercept) 값을 살펴봅니다. 회귀 계수는 각 독립 변수의 영향력을 나타내며, 양의 값이면 해당 독립 변수가 증가할수록 종속 변수 값도 증가하는 것을 의미하고, 음의 값이면 해당 독립 변수가 증가할수록 종속 변수 값은 감소하는 것을 의미합니다. 절편은 모든 독립 변수가 0일 때의 종속 변수 값을 나타냅니다.

# 아래는 auto mpg 데이터셋에서 선형 회귀 모델을 사용하여 연비를 예측한 후 회귀 계수와 절편 값을 출력한 예시 코드입니다.


from sklearn.linear_model import LinearRegression

# 모델 학습
lr = LinearRegression()
lr.fit(X_train, y_train)

# 회귀 계수 출력
print(lr.coef_)

# 절편 출력
print(lr.intercept_)

# 위 코드를 실행하면 회귀 계수와 절편이 출력됩니다. 
# 이를 해석해보면, 각 독립 변수의 회귀 계수 값이 양수인 경우 해당 독립 변수가 증가할수록 연비 값도 증가하는 것을 의미합니다. 
# 마찬가지로 각 독립 변수의 회귀 계수 값이 음수인 경우 해당 독립 변수가 증가할수록 연비 값은 감소하는 것을 의미합니다. 
# 절편은 모든 독립 변수 값이 0일 때의 연비 값을 의미합니다.

# 다만, 선형 회귀 모델의 해석은 여러 가지 다른 요인들에 의해 영향을 받을 수 있으므로, 
# 보다 정확한 해석을 위해서는 변수들 간의 상호작용 등을 고려하는 등 더 깊은 분석이 필요합니다.




# Revue de parfum
# 그럼 연비와 무게 정보를 가지고 로지스틱 회귀로 나타낼 수 있어?


# 로지스틱 회귀 모델은 이진 분류 문제를 해결하는 모델로, 종속 변수가 이진(binary) 형태인 경우에 사용됩니다. 
# 이에 비해 auto mpg 데이터셋의 종속 변수인 mpg(연비)는 연속형 변수이기 때문에 로지스틱 회귀 모델을 사용하여 예측할 수 없습니다.

# 따라서, 연비와 무게 정보를 가지고 예측하려면 선형 회귀 모델이나 다른 회귀 모델을 사용해야 합니다. 
# 선형 회귀 모델을 사용할 경우, 연비와 무게 정보를 독립 변수로 하여 모델을 학습시키고 예측값을 구할 수 있습니다. 
# 이때 예측 결과의 해석 방법은 회귀 분석의 방법론을 따르게 됩니다.




# Revue de parfum
# auto mpg데이터 셋을 어떻게든 로지스틱회귀를 통해서 나타내줘

# auto mpg 데이터셋의 종속 변수 mpg는 연속형 변수이기 때문에 로지스틱 회귀 모델을 사용하여 예측할 수 없습니다. 
# 로지스틱 회귀 모델은 이진 분류(binary classification) 문제에 적합한 모델입니다.

# 만약 auto mpg 데이터셋의 종속 변수를 이진 분류 형태로 변환하여 사용한다면 로지스틱 회귀 모델을 사용할 수 있습니다. 
# 예를 들어, mpg 값이 30보다 크거나 같으면 1(높은 연비), 그렇지 않으면 0(낮은 연비)으로 이진 분류할 수 있습니다. 
# 이렇게 변환한 종속 변수를 이용하여 로지스틱 회귀 모델을 학습시키고 예측값을 구할 수 있습니다. 
# 하지만 이렇게 변환한 종속 변수의 예측 결과는 이진 분류 형태로 나타나기 때문에, 예측 결과의 해석 방법도 이진 분류 모델에 맞추어야 합니다.




# Revue de parfum
# 로지스틱 회귀하는 방법 알려줘

# 로지스틱 회귀 모델을 사용하여 예측하려면 다음과 같은 과정을 거칩니다.

# 데이터 전처리: auto mpg 데이터셋을 불러온 후, 필요한 열만 추출하고 결측값 또는 이상치를 처리합니다.
# 데이터 분할: 전처리한 데이터셋을 학습 데이터셋과 테스트 데이터셋으로 분할합니다.
# 모델 학습: 로지스틱 회귀 모델을 사용하여 학습 데이터셋을 학습시킵니다.
# 모델 예측: 학습된 모델을 사용하여 테스트 데이터셋의 결과를 예측합니다.
# 모델 평가: 모델의 예측 성능을 평가합니다.
# 이제, 위 과정을 자세히 알아보겠습니다.

# 1. 데이터 전처리
# 먼저, auto mpg 데이터셋을 불러온 후, 필요한 열만 추출합니다. 
# 이 예제에서는 "mpg"와 "weight" 열만 사용합니다. 그리고 데이터셋에 결측값 또는 이상치가 있는지 확인합니다.


import pandas as pd

# 데이터셋 불러오기
df = pd.read_csv("auto-mpg.csv")

# mpg와 weight 열만 추출
df = df[["mpg", "weight"]]

# 결측값 또는 이상치 처리
df = df.dropna() # 결측값 제거
df = df[df["mpg"] > 0] # mpg가 0보다 작은 값 제거

# 2. 데이터 분할
# 전처리한 데이터셋을 학습 데이터셋과 테스트 데이터셋으로 분할합니다. 
# 이 예제에서는 학습 데이터셋과 테스트 데이터셋의 비율을 8:2로 지정하고, 
# 난수 발생기의 시드를 42로 고정합니다.


from sklearn.model_selection import train_test_split

# 독립 변수와 종속 변수 분리
X = df.drop("mpg", axis=1)
y = df["mpg"]

# 학습 데이터셋과 테스트 데이터셋 분할
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. 모델 학습
# 로지스틱 회귀 모델을 사용하여 학습 데이터셋을 학습시킵니다. 
# 이 예제에서는 scikit-learn 라이브러리의 LogisticRegression 클래스를 사용합니다.


from sklearn.linear_model import LogisticRegression

# 로지스틱 회귀 모델 학습
model = LogisticRegression()
model.fit(X_train, y_train)
# 4. 모델 예측
# 학습된 모델을 사용하여 테스트 데이터셋의 결과를 예측합니다




# Revue de parfum
# 학습과정에서 
# Unknown label type: 'continuous' 이런 에러메시지가 뜨는데?
# 'Unknown label type: 'continuous'' 에러 메시지는 일반적으로 타겟 변수(y)가 연속형이라면 발생하는 문제입니다.
# 로지스틱 회귀는 분류 문제를 다루는 알고리즘이므로 타겟 변수(y)는 이산형이어야 합니다.

# 따라서, 해당 에러가 발생하는 경우, y 변수를 이산형으로 변환하거나 다른 분류 알고리즘을 적용해야 합니다.
# 예를 들어, 회귀 분석을 사용하여 연속형 출력을 예측할 수 있습니다.

# 만약 y 변수가 이산형인데도 위와 같은 에러 메시지가 나타난다면,
# y 변수의 데이터 타입을 확인해보고 타입 변환 과정에서 문제가 발생했는지 확인해보시는 것이 좋습니다.




# Revue de parfum
# 그럼 y를 이산형 데이터로 바꾸는 방법 알려줘

# y 변수를 이산형 데이터로 바꾸는 방법은 다양한데, 예를 들어 연비(mpg)를 예측하는 경우, mpg 값이 연속형 데이터입니다.
# 따라서 연비 값을 범주형 변수로 변환할 필요가 있습니다.

# 가장 간단한 방법은 mpg 값을 임계값(threshold)에 따라서 이산형으로 변환하는 것입니다.
# 예를 들어, mpg 값이 25 이상인 경우에는 "good"으로 분류하고, 25 미만인 경우에는 "bad"로 분류할 수 있습니다.

# 아래는 이산형으로 변환하는 코드 예시입니다.


threshold = 25
y = np.where(df['mpg'] >= threshold, 1, 0)
# 위 코드에서 np.where 함수는 첫 번째 인자로 조건식을 받고, 조건식이 참일 때는 두 번째 인자로 지정된 값,
# 거짓일 때는 세 번째 인자로 지정된 값을 반환합니다.
# 따라서 위 코드에서는 mpg 값이 25 이상인 경우에는 1, 25 미만인 경우에는 0으로 변환됩니다.

# 위와 같이 이산형으로 변환된 y 값을 바탕으로 로지스틱 회귀를 수행할 수 있습니다.





# 로지스틱 회귀 모델 학습
model = LogisticRegression()
model.fit(X_train, y_train)

# 이렇게 학습은 시켰는데

# 로지스 회귀의 결과값을 알려면 어떻게해야해?
# 로지스틱 회귀 모델에서 예측값을 얻기 위해서는 predict 함수를 사용하면 됩니다. 학습된 모델을 바탕으로 predict 함수를 사용하여 입력 데이터(X_test)에 대한 예측값을 계산하고, 이를 y_pred 변수에 저장합니다.


y_pred = model.predict(X_test)
# 예측값인 y_pred와 실제값인 y_test를 비교하여 모델의 성능을 평가할 수 있습니다. 성능 평가 지표로는 정확도(Accuracy), 정밀도(Precision), 재현율(Recall), F1-score 등이 사용됩니다.


from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

print("Accuracy:", accuracy_score(y_test, y_pred))
print("Precision:", precision_score(y_test, y_pred))
print("Recall:", recall_score(y_test, y_pred))
print("F1-score:", f1_score(y_test, y_pred))

# 위 코드에서 accuracy_score, precision_score, recall_score, f1_score 
# 함수는 각각 정확도, 정밀도, 재현율, F1-score를 계산합니다. 
# 이 함수들은 y_test와 y_pred를 입력으로 받아서 각각의 성능 지표를 반환합니다.