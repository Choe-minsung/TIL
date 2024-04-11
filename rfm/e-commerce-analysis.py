#!/usr/bin/env python
# coding: utf-8

# # E-Commerce Data Analysis (USING RFM)
# - kaggle competition : https://www.kaggle.com/datasets/carrie1/ecommerce-data?resource=download

# - dataset : 영국 소매업체의 2010/01/12 ~ 2011/09/12 간 전 세계 실제 전자상거래 data

# - columns
# 
# | 컬럼명      | 컬럼정보  |
# |-------------|-----------|
# | InvoiceNo   | 송장 번호 |
# | StockCode   | 주식 코드 |
# | Description | 거래 정보 |
# | Queantity   | 거래 수량 |
# | InvoiceDate | 송장 일자 |
# | UnitPrice   | 단가      |
# | CustomerId  | 고객 ID   |
# | Country     | 국가      | 

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import warnings
warnings.filterwarnings("ignore")


# In[2]:


df = pd.read_csv('data.csv')

df.tail(4)


# In[3]:


df.info()


# In[4]:


df.describe()


# In[5]:


# 결측치 처리

df.isna().sum()


# In[6]:


# CustomerID 가 null인 행만 삭제 (Description은 없어도 상관x)

df = df.dropna(subset = ['CustomerID'], axis = 0)

df.shape


# ### Recency (R)

# In[7]:


# Date 컬럼 생성

import datetime as dt

df['date'] = pd.DatetimeIndex(df['InvoiceDate']).date

df.tail(2)


# In[8]:


# Customer 별 최근 구매 날짜

recency_df = df.groupby(['CustomerID'], as_index = False)['date'].max()

recency_df = recency_df.rename({'date' : 'LastPurchaseDate'}, axis = 1)

recency_df


# In[9]:


# 날짜 범위 탐색

print('날짜 범위는 {0} 부터 {1} 까지입니다.'.format(df['date'].min(), df['date'].max()))


# In[10]:


# 마지막 날짜를 오늘날짜로 지정

now = df['date'].max()

now


# In[11]:


# 오늘로부터 최근 구매 날짜까지 일 수

recency_df['Recency'] = recency_df.LastPurchaseDate.apply(lambda x : (now - x).days)

recency_df


# ### Frequency (F)

# In[12]:


# 원시 dataframe copy하여 사용

frequency_df = df.copy()

frequency_df.tail(2)


# In[13]:


# 주문 건수(frequency) 만 파악, 한 제품 다량 구매 -> 1건으로 처리

frequency_df = frequency_df.drop_duplicates(['CustomerID', 'InvoiceNo'], keep = 'first', ignore_index = True)

frequency_df.tail(5)


# In[14]:


# CustomerID 별 빈도수

frequency_df = frequency_df.groupby('CustomerID', as_index = False)['InvoiceNo'].count()

frequency_df = frequency_df.rename({'InvoiceNo' : 'Frequency'}, axis = 1)

frequency_df.tail(4)


# ### Monetary (M)

# In[15]:


# 총 주문 비용 = 단가 * 수량

df['Total_cost'] = df['UnitPrice'] * df['Quantity']

df.tail(2)


# In[16]:


# CutomerID 별 총 주문금액 -> monetary df 생성

monetary_df = df.groupby('CustomerID', as_index = False)['Total_cost'].sum()

monetary_df = monetary_df.rename({'Total_cost' : 'Monetary'}, axis = 1)

monetary_df


# ### RFM (R, F, M 결합)

# In[17]:


# r + f merge

rf = recency_df.merge(frequency_df, on = 'CustomerID')

rf


# In[18]:


# rf + m merge

rfm = rf.merge(monetary_df, on = 'CustomerID')

rfm


# In[20]:


# index 고객ID로 초기화

rfm = rfm.set_index('CustomerID')

rfm


# In[21]:


# 최근 구매 일자 column 삭제

rfm = rfm.drop('LastPurchaseDate', axis = 1)

rfm


# ### Customer Segmentation

# In[25]:


rfm.describe()


# In[26]:


# 원시 df copy하여 사용 (유지보수)

rfm_segmentation = rfm.copy()


# In[27]:


# Elbow Method (k Clustering)

from sklearn.cluster import KMeans

k = range(1, 20)

# list comprehension / k 만큼 Kmeans(클러스터 수 1 ~ 19)
kmeans = [KMeans(n_clusters = i) for i in k]

# list comprehension / k 만큼 Kmeans(클러스터 수 1 ~ 19)에 rfm table 학습 / 학습 된 score 산출
score = [kmeans[i].fit(rfm_segmentation).score(rfm_segmentation) for i in range(len(kmeans))]

plt.plot(k, score)
plt.xlabel('Number of Clusters')
plt.ylabel('Score')
plt.title('Elbow Curve')

plt.show()


# In[29]:


# k = 3 일때 Elbow라 판단

kmeans = KMeans(n_clusters = 3, random_state = 42).fit(rfm_segmentation)

# 'cluster' 컬럼에 군집 번호(kmeans의 레이블) 입력

rfm_segmentation['cluster'] = kmeans.labels_

# check
rfm_segmentation


# In[36]:


# boxplot으로 cluster label 별 R, F, M 비율 확인

plt.figure(figsize = (16,10))

plt.subplot(1,3,1)
sns.boxplot(x = rfm_segmentation['cluster'], y = rfm_segmentation['Recency'])

plt.subplot(1,3,2)
sns.boxplot(x = rfm_segmentation['cluster'], y = rfm_segmentation['Frequency'])

plt.subplot(1,3,3)
sns.boxplot(x = rfm_segmentation['cluster'], y = rfm_segmentation['Monetary'])

plt.show()


# ### cluster 별 특성
# 1. cluster 0 : **Silver** grade customer / long term recency, low frequency of purchase , Low consumption amount
# 2. cluster 1 : **Platinum** grade customer / short term recency, proper frequency of purchase , high consumption amount
# 3. cluster 2 : **Gold** grade customer / short term recency, proper frequency of purchase, proper consumtion amount

# In[ ]:




