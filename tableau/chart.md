# Chart, Plot

[`Tableau 도움말`](https://help.tableau.com/current/pro/desktop/ko-kr/datafields_typesandroles_datatypes.htm)  
[`youtube - DK BMC`](https://www.youtube.com/@DKBMCOfficial)  

### 환경

- version : Tableau Desktop 2024.01 ver
---

- ### 병렬막대그래프
1. '열'에 날짜컬럼(우클릭으로 원하는 '년'or'월'or'일' 만 추출하여 드랍) + 측정값이름('행'이 2개이므로 각각의 레이블 달기 위해), '행'에 수익, 매출
<img width="450" alt="image" src="https://github.com/Choe-minsung/TIL/assets/145301343/11e5aff1-08c8-48f1-9f78-f3d00decada6">

2. '행'이 2개이므로 병렬로 표현하기 위해 1개의 행을 우클릭 - **'이중축'**
<img width="450" alt="image" src="https://github.com/Choe-minsung/TIL/assets/145301343/f53e195b-6321-4422-a323-d2fc87d77e84">

### 히스토그램 : 연속형 측정값의 빈도 표시, 양적 데이터 차트, 막대 사이가 붙은 막대그래프
1. 범주 별 매출 히스토그램 : '열'에 (매출) 드랍 - 우상단 탭 **'표현방식-히스토그램 뷰'** - (범주)를 **'마크-색상'** 에 드랍 - '열'에 (매출)이 **연속형 구간차원**인지, '행'에 (매출)이 **카운트** 인지 확인
2. 테이블에 자동 생성 된 **매출(구간차원) 우클릭** 후 **'편집-구간차원 크기'** (눈금) 조절
3. **y축 최댓값과 최솟값의 차이가 극단적**일 때 시트에 y축을 우클릭 후 **'축 편집-눈금-로그'** 체크  
<img width="450" alt="image" src="https://github.com/Choe-minsung/TIL/assets/145301343/a8b2ff45-2d2e-4137-bee9-09c3f1a755e1">

### 라인그래프
1. '열'에 날짜컬럼(우클릭으로 원하는 '년'or'월'or'일' 만 추출하여 드랍), '행'에 수익, 매출

2. '행'이 2개이므로 동시에 표현하기 위해 1개의 행을 우클릭 - **'이중축'**
<img width="450" alt="image" src="https://github.com/Choe-minsung/TIL/assets/145301343/9d2af884-899a-4c02-bd73-710dd4fb5949">

3. 하나의 y축 우클릭시 '축 동기화' 하여 y축 값 수준을 맞춰줌  
<img width="450" alt="image" src="https://github.com/Choe-minsung/TIL/assets/145301343/8d4b6e61-4876-41e2-bff5-bb8d97d54e69">

### 트리맵
1. 제품카테고리 별 매출액 트리맵 : (제품카테고리)를 '마크-레이블' - (매출)을 '색상', '크기'  
<img width="450" alt="image" src="https://github.com/Choe-minsung/TIL/assets/145301343/b62b7513-0f8e-4cc7-9fb9-38a1dedcd2dc">
  
2. 제품명 별 매출액 트리맵 : (제품명)을 '마크-레이블' - (매출)을 '색상', '크기'  
<img width="450" alt="image" src="https://github.com/Choe-minsung/TIL/assets/145301343/78e59d71-416d-4bd6-8c8c-6a8acd9d023c">

3. 제품명이 너무 많으므로 **필터**로 **상위 10개**만 표현 : (**제품명**)을 **필터**에 드랍 - 상단탭 '상위'에서 '필드기준'에서 **'상위-10'**, **'매출-합계'** 으로 설정  
<img width="450" alt="image" src="https://github.com/Choe-minsung/TIL/assets/145301343/8aa767d2-9c6d-4be7-8ff4-bdf376216ee3">

### 파이차트 & 도넛차트
1. (고객 세그먼트), (매출) 각각 더블클릭 - 우상단 탭 '표현 방식 - 파이차트' - (매출)을 '마크-레이블'에 추가 - 내림차순 정렬  

2. 내림차순 정렬 - 레이블을 구성비율로 표시  
<img width="450" alt="image" src="https://github.com/Choe-minsung/TIL/assets/145301343/737d28cb-a56a-4443-ae7e-c2cca55a5dd4">  

3. **총 매출을 가운데 표시**하기 위해 **이중축 활용 도넛차트 생성** : **'열' 빈공간**에 더블클릭 - **0 입력** - ctrl로 하나 더 생성 - 2번째 차트의 **'마크' 모두 삭제**  
<img width="450" alt="image" src="https://github.com/Choe-minsung/TIL/assets/145301343/eb460fb7-e65a-429f-b872-e32662cb32d3">  

4. 2번째 차트의 '마크-레이블'에 매출 추가 - 두 파이차트 크기 조절 - '열'에서 2번째 차트를 **'이중축'** 설정  
<img width="450" alt="image" src="https://github.com/Choe-minsung/TIL/assets/145301343/c2049b50-2ee1-40c2-819e-a48394e8a340">  

5. 2번째 차트 '마크-색상' 흰색으로 변경 - 시트 빈 공간 우클릭 **'서식'** -  상단탭 **'테두리'** 의 행구분선, 열구분선의 '패널-없음' - 상단탭 **'라인'** 의 '영(0)기준선-없음' - 시트의 위 아래 **'머리글설정-해제'**  
<img width="150" alt="스크린샷 2024-03-01 101020" src="https://github.com/Choe-minsung/TIL/assets/145301343/ac375f4b-e734-4a88-872f-db66e6d181e7">  

<img width="150" alt="image" src="https://github.com/Choe-minsung/TIL/assets/145301343/cd1c4abd-543b-45f1-9c6f-238e54e1d44e">  

6. '마크-색상' - 효과 - 테두리 - 흰색  
<img width="450" alt="image" src="https://github.com/Choe-minsung/TIL/assets/145301343/5c4d3eb7-337e-478a-98f4-8d47ca96eac6">  

### 버블차트
1. (국가/지역), (매출) 각각 더블클릭 - 우상단 탭 **'표현 방식-채워진 버블 차트'** - (매출)을 '마크-색상'에 추가  
<img width="450" alt="image" src="https://github.com/Choe-minsung/TIL/assets/145301343/e7ae6e57-315f-4e5f-9aee-d14966d7d354">

### 분산형차트
1. '열'에 (매출), '행'에 (수익) 드랍
2. (제품 하위 카테고리)를 **'마크-세부정보'** - (제품 카테고리)를 **'마크-색상'** 에 드랍
3. 데이터 탭 옆 **'분석탭'** 에서 **'추세선'** 드래그 - 시트위에 **'선형'** 에 드랍  
<img width="450" alt="image" src="https://github.com/Choe-minsung/TIL/assets/145301343/3bbccc3a-b7a2-4528-a02b-94c0181d4c5b">  
  
4. 범주 별 추세선이 아닌 **전체차트의 추세선** : 추세선 하나 우클릭 **'모든 추세선 편집'** - **'요소'** 에서 색상으로 지정된 **필드 체크 해제**  
<img width="450" alt="image" src="https://github.com/Choe-minsung/TIL/assets/145301343/2e99cb90-66e9-472c-a999-2bf75e3e1818">  

### 박스플롯 : IQR, 분포와 이상치 분석
1. 지역, 고객 세그먼트 별 매출 박스플롯 : '열'에 (세그먼트), (지역), '행'에 (매출) 드랍 - 우상단 탭 **'표현방식-박스플롯'**
2. '마크'로 내려온 (지역)을 다시 '열'로 드랍 - (고객이름)을 **'마크-세부정보'** 에 드랍 - (세그먼트)를 **'마크-색상'** 에 드랍
3. **y축 최댓값과 최솟값의 차이가 극단적**일 때 시트에 y축을 우클릭 후 **'축 편집-눈금-로그'** 체크  
<img width="450" alt="image" src="https://github.com/Choe-minsung/TIL/assets/145301343/842e2aea-7e67-44d3-9d2c-bd02a9f575a0">

### 영역차트 : 연속형 데이터의 누계
1. '열'에 날짜컬럼(우클릭으로 원하는 '년'or'월'or'일' 만 추출하여 드랍), '행'에 (매출)
2. 우상단 탭 **'표현방식-영역차트(연속형)'** - (매출)을 **'마크-레이블'** 에, (세그먼트)를 **'마크-색상'** 에 드랍
3. 차트에 마우스 오버 시 구성비율을 표시하기 위해 : (매출)을 **'마크-세부정보'** 에 드랍 - 드랍한 (매출) 우클릭 후 **'퀵 테이블 계산-구성비율'** - 다시 우클릭 후 **'다음을 사용하여 계산-테이블(아래로)'**
<img width="450" alt="image" src="https://github.com/Choe-minsung/TIL/assets/145301343/1e696629-2773-4d7a-a1d0-f399fccca497">

### 간트(Gantt)차트 : 시간에따른 변화
1. 고객명에 따른 제품 카테고리 별, 배송형태 별, 배송기간 간트차트 : '열'에 배송날짜(우클릭으로 원하는 '년'or'월'or'일' 만 추출하여 드랍), '행'에 (범주), (하위범주) 드랍
2. '배송기간' 계산필드 생성 : 상단탭 **'분석-계산된 필드 만들기'** - 필드명은 **'배송기간'**, 함수는 **DATEDIFF('day', 주문날짜 테이블 드랍, 배송날짜 테이블 드랍)** - 생성된 계산필드를 **'마크-크기'** 에 드랍 후 우클릭 **'측정값-평균'** 으로 설정 - **'마크-Gantt차트'** 로 설정  
<img width="450" alt="image" src="https://github.com/Choe-minsung/TIL/assets/145301343/7f2f1bcd-f48b-4855-8ea5-48c98e53f85b">

3. 고객명에 따른 필터 걸기 : (고객이름) 필터에 드랍 - 아무고객 체크 후 확인 - 필터에 생성 된 (고객이름) 우클릭 후 **'필터표시'** - 오른쪽에 표시 된 (고객이름) 필터 세모모양 클릭 - **단일 값(드롭다운)** 으로 변경   
<img width="150" alt="image" src="https://github.com/Choe-minsung/TIL/assets/145301343/d7b48743-6a8e-4aa9-90f2-4d0ceb8ae9ee">

4. (배송형태)를 **'마크-색상'** 에 드랍
