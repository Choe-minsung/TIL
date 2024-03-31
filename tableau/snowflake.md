# 스노우플레이크 (데이터 연동)

[`Snowflake`](https://www.snowflake.com/en/)  
[`youtube - DK BMC`](https://www.youtube.com/@DKBMCOfficial)  

### 환경

- version : Tableau Desktop 2024.01 ver

---

### Snowflake DB에 데이터 업로드
1. *csv 데이터 수집 (snowflake는 xlsx 파일 호환 x)* : 내 Tableau 리포지토리 데이터 원본에 있는 **'Sample - Superstore.xls'** 파일의 **sheet 별**로 **csv 형태**로 각각 저장(3개)
<img width="600" alt="image" src="https://github.com/Choe-minsung/TIL/assets/145301343/292a9138-871d-4471-8a18-7e939d2c2de6">

2. snowflake에서 좌측 탭 **'Data-Databases'** 에서 **New Database** 클릭 - Name : **Tableau**, Comment : **Tableau DB** 입력 후 생성
<img width="600" alt="image" src="https://github.com/Choe-minsung/TIL/assets/145301343/97d4c52a-7c06-44a6-bb19-efb404614f4c">

3. Public 스키마에서 우상단 **'Create-Table-Standard'** 클릭 - 각 csv 파일(3개) 별 **테이블 생성 쿼리** 입력 후 Create
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

4. 생성 된 각 테이블 선택 - 우상단 **'Load Data'-Browse-업로드 할 csv 파일 선택-Next** - File format : **'Delimited Files (CSV or TSV)'**, Skip header : **'Skip first line'**, Field optionally enclosed by : **'Double quotes'** - Load - Done

### Tableau로 연결
1. Tableau 시작화면 좌측 탭 '서버에연결-자세히-Snowflake' - 드라이버 다운로드 후 재시작
2. 다시 Tableau 시작화면 좌측 탭 **'서버에연결-자세히-Snowflake'** - 서버 : **Dedicated Login URL (snowflake 가입 시 이메일 발송)**, 인증 : '사용자 이름 및 비밀번호', 사용자이름 : (가입 시 내 ID), 비밀번호 : (내 비밀번호) - 로그인
3. 좌측 탭 웨어하우스 : **'COMPUTE_WH'**, 데이터베이스 : **'TABLEAU'**, 스키마 : **'PUBLIC'**
4. 테이블을 순서대로 각각 더블클릭하여 관계로 불러오기 - SUPERSTORE_ORDERS 클릭 - '지금 업데이트' 클릭
