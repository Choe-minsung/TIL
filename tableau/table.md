# Table

[`Tableau 도움말`](https://help.tableau.com/current/pro/desktop/ko-kr/datafields_typesandroles_datatypes.htm)  
[`youtube - DK BMC`](https://www.youtube.com/@DKBMCOfficial)  

### 환경

- version : Tableau Desktop 2024.01 ver

---

- ### 텍스트 테이블
1. '열'에 날짜컬럼(우클릭으로 원하는 '년'or'월'or'일' 만 추출하여 드랍), '행'에 범주(제품 카테고리), 하위범주(제품 하위카테고리), '마크-레이블'에 매출
<img width="450" alt="image" src="https://github.com/Choe-minsung/TIL/assets/145301343/ad7a1f95-f9bc-43cc-8d7b-1cefe9727000">

2. 년도 별 매출 백분율 계산 : 레이블의 매출 우클릭 - '퀵 테이블 계산'에 구성비율 - '테이블 계산 편집'에 **테이블(아래로)**
<img width="450" alt="image" src="https://github.com/Choe-minsung/TIL/assets/145301343/319dba4f-d874-44a2-83a1-6b55d30435cd">

3. 년도 별, 범주 별 백분율 계산 : 레이블의 매출 우클릭 - '테이블 계산 편집'에 **패널(아래로)**  
<img width="450" alt="image" src="https://github.com/Choe-minsung/TIL/assets/145301343/afc75237-b6eb-401b-9e03-9633efc6b1ef">

### 하이라이트 테이블
1. (고객세그먼트)를 '열'로, (지역), (제품 카테고리)를 '행'으로 설정
2. (매출), (수익)을 더블클릭하여 측정값으로 설정
3. 현재 설정 된 측정값 레이블을 **'마크-색상'** 으로 **ctrl + 드랍**
<img width="450" alt="image" src="https://github.com/Choe-minsung/TIL/assets/145301343/be57c1ec-7f26-4943-8a43-96bb49d31be9">

4. '마크-차트종류'를 **'사각형'** 으로 설정 후 색상 측정값을 우클릭 후 **'별도의 범례 사용'**  
<img width="150" alt="image" src="https://github.com/Choe-minsung/TIL/assets/145301343/799a0fa8-76e8-4dea-ae34-5c5f2dfa38c3">

### 워드클라우드
1. (국가/지역)을 '마크-레이블'에, (매출)을 '마크-색상'에 추가 - (국가/지역)을 **우클릭** 한 상태로 **'마크-크기'** 에 드랍 - 필드 놓기에서 **카운드(국가/지역)** 선택  
<img width="150" alt="image" src="https://github.com/Choe-minsung/TIL/assets/145301343/92a1e04c-e3a8-4fe1-9a52-438628eab3b6">

2. '마크-표현방식' 을 '텍스트'로 변경 후 전체보기  
<img width="450" alt="image" src="https://github.com/Choe-minsung/TIL/assets/145301343/a9a6f0aa-de3c-4c89-8290-ba04e7c14230">
