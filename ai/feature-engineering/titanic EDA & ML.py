#!/usr/bin/env python
# coding: utf-8

# # Kaggle : titanic dataset
# ### EDA & Feature Engineering & ML prediction
# - https://www.kaggle.com/competitions/titanic/data

# ### Index
# 1. Data Dictionary
# 2. EDA
# 3. CDA 1, 2
# 4. Feature Engineering 1, 2, 3, 4
# 5. ML modeling
# 6. Prediction

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt


# In[2]:


train = pd.read_csv('train.csv')
test = pd.read_csv('test.csv')
sub = pd.read_csv('gender_submission.csv')

train.shape, test.shape, sub.shape


# # Data Dictionary
# 
# |Variable|Definition|Key|
# |------------|-----------|-----------|
# |survival|	Survival	|0 = No, 1 = Yes |
# |pclass	|Ticket class	|1 = 1st, 2 = 2nd, 3 = 3rd|
# |sex	|Sex	|
# |Age	|Age in years	|
# |sibsp	|# of siblings / spouses aboard the Titanic|	
# |parch	|# of parents / children aboard the Titanic|	
# |ticket	|Ticket number	|
# |fare	|Passenger fare	|
# |cabin	|Cabin number	|
# |embarked	|Port of Embarkation	|C = Cherbourg, Q = Queenstown, S = Southampton|

# In[3]:


train.head()


# In[4]:


test.head()


# In[5]:


sub.head()


# In[6]:


train.info()


# # EDA

# In[7]:


train.describe()


# In[8]:


col = train.select_dtypes(include = ['int', 'float']).columns

plt.title('Pearson Correlation')
sns.heatmap(train[col].corr(), annot = True, fmt = '.2f')


# In[9]:


# 성별 countplot
sns.countplot(x = train['Sex'])


# In[10]:


# 나이 histplot + kde : T
sns.histplot(train['Age'], kde = True)


# In[11]:


# Pclass (ticket grade) countplot
sns.countplot(x = train['Pclass'])


# In[12]:


# Embarked (port of embarkation) countplot
sns.countplot(x = train['Embarked'])


# In[13]:


# Fare plot

plt.figure(figsize = (6, 12))

plt.subplot(2,1,1)
plt.title('Fare kdeplot')
sns.histplot(train['Fare'], kde = True)

plt.subplot(2,1,2)
plt.title('Fare boxplot')
sns.boxplot(train['Fare'])

plt.show()


# # CDA 1. target : Fare

# In[14]:


import scipy.stats as spst


# In[15]:


train.columns


# In[16]:


# 독립변수, 종속변수를 input으로 받는 kdeplot, 유의성검정 함수 생성

def get_test(ind_var, de_var):
    
    print(train[ind_var].corr(train[de_var]))
    
    plt.figure(figsize = (8, 8))
    
    plt.subplot(1,2,1)
    sns.scatterplot(x = train[ind_var], y = train[de_var])

    plt.subplot(1,2,2)
    sns.boxplot(x = train[ind_var], y = train[de_var])
    
    plt.show()


# In[17]:


# 가설 1. 성별이 운임에 유의하다.

# 'Sex' 컬럼 값 mapping
train['Sex'] = train['Sex'].map({'male': 0, 'female': 1})
test['Sex'] = test['Sex'].map({'male': 0, 'female': 1})

get_test('Sex', 'Fare')


# In[18]:


# 가설 2. 나이가 운임에 유의하다.

get_test('Age', 'Fare')


# In[19]:


# 가설 3. 티켓등급(1 = 1st, 2 = 2nd, 3 = 3rd)이 운임에 유의하다.

get_test('Pclass', 'Fare')


# In[20]:


# 가설 4. 승선한 포트(C = Cherbourg, Q = Queenstown, S = Southampton)가 운임에 유의하다.

train['Embarked'] = train['Embarked'].map({'S': 0, 'C': 1, 'Q': 2})
test['Embarked'] = test['Embarked'].map({'S': 0, 'C': 1, 'Q': 2})

get_test('Embarked', 'Fare')


# In[ ]:





# In[ ]:





# # CDA 2. target : Survived

# In[21]:


# 가설 1. 성별이 생존여부에 유의하다.

get_test('Sex', 'Survived')


# In[22]:


# 가설 2. 나이가 생존여부에 유의하다.

get_test('Age', 'Survived')


# In[23]:


# 가설 3. 티켓등급(1 = 1st, 2 = 2nd, 3 = 3rd)이 생존여부에 유의하다.

get_test('Pclass', 'Survived')


# In[24]:


# 가설 4. 승선한 포트(C = Cherbourg, Q = Queenstown, S = Southampton)가 생존여부에 유의하다.

get_test('Embarked', 'Survived')


# In[25]:


sns.violinplot(x='Embarked', y='Survived', data=train, ci=None)


# # Feature Engineering
# - model 정확도 높이기 위해
# - model이 학습하는 데이터의 feature들을 가공하여주는 것
# - train, test 둘 다 적용시켜야 함

# In[26]:


train.isna().sum()


# ### 1-1. 'Age' null 처리
# - 177개의 'Age' 결측치 존재
# - 'Name' -> 'Initial'을 추출, 이 것으로 'Age'를 추측하여 결측치 채우기

# In[27]:


train['Age'].isna().sum()


# In[28]:


train['Name'].info()


# - train['Name'] 은 Series형태이므로 .str 후 정규표현식으로 Mr. Mrs. 처럼 . 앞에 단어 찾기

# In[29]:


# 정규표현식으로 Mr. Mrs. 등 호칭 추출

train['Initial'] = train['Name'].str.extract('([A-Za-z]+)\.')
test['Initial'] = test['Name'].str.extract('([A-Za-z]+)\.')


# In[30]:


train.head()


# In[31]:


# crosstab으로 Initial 값 별 성별 확인

pd.crosstab(train['Initial'], train['Sex'])


# In[32]:


# 'Mr', 'Miss', 'Mrs' 를 제외한 나머지 호칭 replace (남 or 여 모르겠는건 'Other')

train['Initial'] = train['Initial'].replace(['Mlle', 'Mme', 'Ms', 'Dr', 'Major', 'Lady', 'Countess', 'Jonkheer', 'Col', 'Rev', 'Capt', 'Sir', 'Don', 'Dona'],
                        ['Miss', 'Miss', 'Miss', 'Mr', 'Mr', 'Mrs', 'Mrs', 'Other', 'Other', 'Other', 'Mr', 'Mr', 'Mr', 'Mr'])

test['Initial'] = test['Initial'].replace(['Mlle', 'Mme', 'Ms', 'Dr', 'Major', 'Lady', 'Countess', 'Jonkheer', 'Col', 'Rev', 'Capt', 'Sir', 'Don', 'Dona'],
                        ['Miss', 'Miss', 'Miss', 'Mr', 'Mr', 'Mrs', 'Mrs', 'Other', 'Other', 'Other', 'Mr', 'Mr', 'Mr', 'Mr'])

train['Initial']


# In[33]:


train.groupby('Initial')['Age'].mean()


# In[34]:


train.groupby('Initial')['Age'].mean().plot.bar()


# In[35]:


# train 데이터의 'Initial' 컬럼의 평균 'Age' 값 확인

Init = train.groupby('Initial')['Age'].mean()

Init


# In[36]:


Init.keys()[0]


# In[37]:


Init.values[0]


# In[38]:


# 반복문으로 ('Age'가 null)이고 ('Initial'이 각각 ['Master', 'Miss', 'Mr', 'Mrs', 'Other']) 인 데이터를
# 해당 'Initial' 의 평균 'Age' 로 채우기

# * train 데이터셋의 'Initial' 데이터를 기반으로 train, test에 'Age'의 null값을 채우기 *

for i in range(5):
    train.loc[(train['Age'].isna()) & (train['Initial'] == Init.keys()[i]),'Age'] = Init.values[i]
    test.loc[(test['Age'].isna()) & (test['Initial'] == Init.keys()[i]),'Age'] = Init.values[i]
    
train['Age'].isna().sum(), test['Age'].isna().sum()


# ### 1-2. Age 컬럼 contiuous -> categorical
# - bin : -np.inf, 11, 21, 31, 41, 51, 61, 71, np.inf
# - label : 0, 1, 2, 3, 4, 5, 6, 7
# 
# - 주의! : 정보손실 발생 가능성o

# In[39]:


train.head()


# In[40]:


# pd.cut() 활용 범주화

bin = [-np.inf, 11, 21, 31, 41, 51, 61, 71, np.inf]
label = [0, 1, 2, 3, 4, 5, 6, 7]

train['Age_group'] = pd.cut(train['Age'], bins = bin, labels = label)
test['Age_group'] = pd.cut(test['Age'], bins = bin, labels = label)


# In[41]:


train[['Age', 'Age_group']]


# In[42]:


test[['Age', 'Age_group']]


# ### 2. Embarked null 처리
# - 2개의 'Embarked' 결측치 존재
# - 891개 중 2개이므로 max 값으로 처리

# In[43]:


train['Embarked'].isna().sum()


# In[44]:


train.shape


# In[45]:


train['Embarked'].value_counts()


# In[46]:


train['Embarked'] = train['Embarked'].fillna(0)

train['Embarked'].isna().sum()


# In[47]:


train.info()


# ### 3. 'Initial', 'Embarked' : categorical 처리
# - object -> categorical

# In[48]:


train['Initial'].info(), train['Initial'].value_counts()


# In[49]:


# 'Initial' 컬럼이 object type 이므로 categorical로 변경
# .map({'A' : 0, 'B' : 1 ... })

train['Initial'] = train['Initial'].map({'Mr' : 0, 'Miss' : 1, 'Mrs' : 2, 'Master' : 3, 'Other' : 4})
test['Initial'] = test['Initial'].map({'Mr' : 0, 'Miss' : 1, 'Mrs' : 2, 'Master' : 3, 'Other' : 4})


# In[50]:


train['Initial'], test['Initial']


# In[51]:


train['Embarked'].unique


# In[52]:


train['Embarked'] = train['Embarked'].astype(int)


# In[53]:


train.isna().sum()


# In[54]:


train.info()


# In[55]:


test.info()


# In[64]:


# heatmap

col = train.select_dtypes(['int', 'float', 'category']).columns

sns.heatmap(train[col].corr(), annot = True, fmt = '.2f')


# ### One-hot encoding
# 
# - categorical 컬럼들 (0, 1, 2, ...)이 아닌 여러 dummies 컬럼으로 만듦
# - model의 정확도 향상

# In[65]:


train.info()


# In[67]:


# pd.get_dummies(df, columns = ['', ''], drop_first = T/F)

col = ['Initial', 'Embarked'] # categorical 컬럼들 get_dummies 처리

train = pd.get_dummies(train, columns = col, drop_first = False)
test = pd.get_dummies(test, columns = col, drop_first = False)

train.head(), test.head()


# In[68]:


train.columns


# In[70]:


# modeling에 사용하지 않을 컬럼들 삭제

col = ['PassengerId', 'Name', 'SibSp', 'Parch', 'Ticket', 'Cabin']

train = train.drop(col, axis = 1)
test = test.drop(col, axis = 1)

train.shape, test.shape


# ### ML prediction : 'Survived'

# - target class : 'Survived'를 0 or 1로 예측하는 binary 예측이므로 Classifier 모형
# - ensemble 모델인 RandomForest ML model 사용

# In[72]:


# train 데이터셋 내에서 x, y 분리

from sklearn.model_selection import train_test_split

x = train.drop('Survived', axis = 1).values
y = train['Survived'].values

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = .2, random_state = 42)

x.shape, y.shape


# In[73]:


# modeling

from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier()

model.fit(x_train, y_train)


# In[83]:


# prediction

y_pred = model.predict(x_test)


# In[84]:


# estimation

from sklearn.metrics import *

accuracy_score(y_pred, y_test)


# In[89]:


# feature importance

model.feature_importances_, test.columns


# In[107]:


plt.barh(test.columns, model.feature_importances_)


# - **feature selection** : feature importance 를 보고 모델 성능에 영향이 적은 feature들을 제외하고 다시 적합시키는 것.

# ### submission prediction
# - train.csv : EDA 후, feature engineering한 뒤 model을 학습시키는데 사용
# - test.csv : train.csv 에서 target만 빠진 data, 이 test.csv의 target을 채워서 submission 'Survived' 컬럼에 채워넣기
# - submission.csv : test.csv에서 target을 예측한 값을 'Survived'에 채워넣어 최종 제출

# In[115]:


# test.csv의 target값 예측

pred = model.predict(test.values)

pred


# In[116]:


sub.head()


# In[117]:


# 제출파일 submission에 test.csv의 target 예측값을 채워넣어 제출

sub['Survived'] = pred

sub


# In[118]:


sub.to_csv('my_submission.csv', index = False)

