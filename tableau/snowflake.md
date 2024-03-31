# 스노우플레이크 (데이터 연동)

[`Snowflake`](https://www.snowflake.com/en/)  
[`youtube - DK BMC`](https://www.youtube.com/@DKBMCOfficial)  

### 환경

- version : Tableau Desktop 2024.01 ver

---

### DB 생성
1. *csv 데이터 수집 (snowflake는 xlsx 파일 호환 x)* : 내 Tableau 리포지토리 데이터 원본에 있는 'Sample - Superstore.xls' 파일의 sheet 별로 csv 형태로 각각 저장(3개)
<img width="600" alt="image" src="https://github.com/Choe-minsung/TIL/assets/145301343/292a9138-871d-4471-8a18-7e939d2c2de6">

2. snowflake에서 좌측 탭 'Data-Databases' 에서 New Database 클릭 - Name : Tableau, Comment : Tableau DB 입력 후 생성
<img width="600" alt="image" src="https://github.com/Choe-minsung/TIL/assets/145301343/97d4c52a-7c06-44a6-bb19-efb404614f4c">

3. Public 스키마에서 우상단 'Create-Table-Standard' 클릭 - 각 csv 파일(3개) 별 테이블 생성 쿼리 입력 후 Create
```
-- order 시트
Create or replace table superstore_orders
(
  rowId string,
  OrderId string,
  OrderDate date,
  CustomerId string,
  Segment string,
  City string,
  Sales float,
  Quantity float,
  Profit float,
  Discount float
)
```

```
-- people 시트
Create or replace table superstore_people
(
  regionalManager string,
  region string
)
```

```
-- return 시트
Create or replace table superstore_return
(
  returned string,
  orderId string
)
```
