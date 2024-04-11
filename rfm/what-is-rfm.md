# RFM (Recency Frequency Monetary) Analysis

RFM is a method used for analyzing customer value. It is commonly used in database marketing and direct marketing and has received particular attention in retail and professional services industries

RFM stands for the three dimensions:

1. **Recency (최근 주문 일자)** : How recently did the customer purchase?
2. **Frequency (주문 빈도)** : How often do they purchase?
3. **Monetary Value (주문 금액)** : How much do they spend?


---
# Customer Segmentation using RFM Analysis

[`E-commerce dataset (kaggle)`](https://www.kaggle.com/datasets/carrie1/ecommerce-data?resource=download)

- dataset : 영국 소매업체의 2010/01/12 ~ 2011/09/12 간 전 세계 실제 전자상거래 data
- columns : ![image](https://github.com/Choe-minsung/TIL/assets/145301343/f0bda063-49c0-40aa-a89f-f67d946f1491)

### Recency (R)
1. Date 컬럼 생성
2. 고객 별 최근 구매 날짜
3. 오늘로부터 최근 구매 날짜까지의 일수 df 생성

### Frequency (F)
1. 고객 당 송장번호 갯수 학인 (주문 건수 파악 / 송장번호당 여러개 주문 -> 1개로 취급)
2. 고객 당 주문 건수 df 생성

### Monetary (M)
1. 총 주문금액 컬럼 생성 (단가 * 수량)
2. 고객 당 총 주문금액 df 생성

### RFM (R, F, M merge)
1. recency_df + frequency_df = rf
2. rf + monetary_df = rfm  
![image](https://github.com/Choe-minsung/TIL/assets/145301343/390b3d3c-a3ce-409d-8cc1-a1e700f41921)

### Customer Segmentation
1. Elbow Method로 최적 k(cluster 수)확인  
![image](https://github.com/Choe-minsung/TIL/assets/145301343/5f0db4fd-52fe-422d-8131-8d99e15d08e6)

2. 최적 k로 KMeans 학습  
![image](https://github.com/Choe-minsung/TIL/assets/145301343/86bf73b9-17b0-48a2-a460-f2a63c5b12f5)

3. boxplot으로 cluster label 별 R, F, M 분포 확인![image](https://github.com/Choe-minsung/TIL/assets/145301343/7e65563e-d76a-43f6-aa86-52c7b970c201)


### Conclusion
- 고객 Segmentation 별 (Cluster 별) 특성
1. cluster 0 : **Silver** grade customer / long term recency, low frequency of purchase , Low consumption amount
2. cluster 1 : **Platinum** grade customer / short term recency, proper frequency of purchase , high consumption amount
3. cluster 2 : **Gold** grade customer / short term recency, proper frequency of purchase, proper consumtion amount












