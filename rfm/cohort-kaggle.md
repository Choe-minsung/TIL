# Cohort Analysis - kaggle

[`Online Retail dataset (kaggle)`](https://www.kaggle.com/code/ahmetokanyilmaz/cohort-analysis-with-python)

- dataset : 영국 소매업체의 2009/01/12 ~ 2011/09/12 간 전 세계 실제 전자상거래 data

- columns : ![image](https://github.com/Choe-minsung/TIL/assets/145301343/c8660dd8-3d67-4bad-b553-91d2ba55472d)

### preprocessing
1. 결측치 처리
2. 이상치 처리 : describe() -> 수치형 feature 중 min 값이 0 보다 작은 Quantity 삭제
![image](https://github.com/Choe-minsung/TIL/assets/145301343/ae8428ca-c237-4d16-ac28-7d29444055e1)

3. Date 처리 : 'order_month' -> 주문일시 (년/월), 'cohort' -> 각 고객ID 별 최초 구매 날짜(min 값 기준)

### cohort table
1. cohort, order_month 기준 groupby
2. 각 그룹 내 고객ID의 unique 갯수 count (고유 고객수) -> 'n_customers'
3. 최초주문으로부터 해당 주문일시의 개월 차이 'period_number' (= order_month - cohort)
![image](https://github.com/Choe-minsung/TIL/assets/145301343/9dec4b55-ee6f-45b6-9202-8e390187642b)

### retention matrix
1. 피벗테이블 생성 : 'cohort' -> index, 'period_number' -> column, value -> 'n_customers'
2. 고객 유지율 비율 계산을 위해 기준 산출 : 'period_number' 가 0인 column -> 'cohort_size'
3. retention matrix 피벗 생성
![image](https://github.com/Choe-minsung/TIL/assets/145301343/09f74c21-5dbe-48d2-9a25-9c12277f7e96)

### Heatmap
![image](https://github.com/Choe-minsung/TIL/assets/145301343/7d713653-50c8-4269-8c54-e5a46a12cb0c)

### Insights
- 두 번째 달에는 고객 수가 급격히 감소하며, 평균적으로 약 80%의 고객이 해당 달에 구매를 하지 않는다.
- 첫 번째 코호트(2010–12)는 다른 코호트와 비교하여 높은 성과를 보이며, 첫 번째 구매 후 1년이 지난 후에도 약 50%의 유지율을 보인다.
- 이는 주로 소매업체와의 기존 관계를 바탕으로 플랫폼에 처음 가입한 전용 고객 코호트로 추측된다.
- 이러한 패턴은 주기적인 구매와 비활성 기간이 번갈아 발생하는 기업의 특성을 반영한다.

