# Tableau 배우기

[`Tableau 도움말`](https://help.tableau.com/current/pro/desktop/ko-kr/datafields_typesandroles_datatypes.htm)  
[`youtube - DK BMC`](https://www.youtube.com/@DKBMCOfficial)  

### 환경

- version : Tableau Desktop 2024.01 ver

- **데이터 연결방식**
1. 라이브 : 데이터 원본 실시간 동기화 (원본 수정시 실시간 반영)
2. 추출 : Hyper 형태로 복사본 불러옴 (처리속도 빠름o)

- **데이터 유형**
1. ![image](https://github.com/Choe-minsung/TIL/assets/145301343/b99c3734-9f94-441e-84ba-bce3e58e80d9) : 텍스트
2. ![image](https://github.com/Choe-minsung/TIL/assets/145301343/98cc2f2e-8918-4559-8e35-b65679506065) : 날짜(달력)
3. ![image](https://github.com/Choe-minsung/TIL/assets/145301343/ca44b6aa-ffe4-4c7c-bf83-0f31a5fb63ab) : 날짜+시간
4. ![image](https://github.com/Choe-minsung/TIL/assets/145301343/e1330c23-48a7-4131-9a09-62a53c6451ff) : 숫자
5. ![image](https://github.com/Choe-minsung/TIL/assets/145301343/22d66edd-d6c1-44af-8745-6bdf5bd2e114) : boolean
6. ![image](https://github.com/Choe-minsung/TIL/assets/145301343/c86026ae-370d-4600-8468-a03e8277cf2c) : map

- **데이터 형태**
1. 범주값 : 열에 사용
2. 수치값 (측정값) : 행으로 사용 (집계, 평균 등) 
<img width="152" alt="image" src="https://github.com/Choe-minsung/TIL/assets/145301343/eb922ae6-26f1-4fa3-84c6-7a7f58f43462">


### 데이터 결합 (컬럼 추가)
- **관계** : 각각 테이블 더블클릭
1. 동일컬럼 존재시에만 결합 가능 (key 컬럼이 고유값인지 확인! 아니면 중복발생)
2. 먼저 불러온 테이블이 outer table (root table) 로 삭제시 하위 테이블 모두 삭제됨
3. 일 : 다, 다 : 다 ...

- **Join** : 1개의 테이블 더블클릭 - 열기 - 2번째 테이블 더블클릭
1. inner, left, right, outer 조인방식 설정 가능

- **혼합**
1. 시트에 union 할 2개의 테이블 불러오기 : 하단탭 데이터 원본에서 1개 테이블 더블클릭 - 하단탭 시트 1 - 상단탭 데이터 - 새 데이터원본 - 원하는 excel파일 - 다시 하단탭 데이터 원본에서 새 테이블 더블클릭 - 하단탭 시트 1
<img width="150" alt="image" src="https://github.com/Choe-minsung/TIL/assets/145301343/e6e1e299-b3a8-420e-a6d1-820b8889546e">

2. 열설정, 마크(data) 설정 : 첫번째 테이블클릭 -  열로 설정할 컬럼 '열'에 드랍 - 두번째 테이블클릭 - 마크(data)로 설정할 컬럼 '마크 - 텍스트'에 드랍
<img width="490" alt="image" src="https://github.com/Choe-minsung/TIL/assets/145301343/dbf6467d-1a4b-475b-a2a8-894bdc90f07d">

### 데이터 결합 (행 추가)
- **Union** : 행 방향으로 붙이기 (컬럼명, 컬럼수 동일해야 함)
1. 1개 테이블 더블클릭 - 바로 아래 다른 테이블 드랍
2. '새 유니온' 클릭 - 2개 테이블 넣기

### 시각화
- **차트 그리기**
1. 범주컬럼 더블클릭 or '열'에 드랍
2. 수치컬럼 더블클릭 or '마크-레이블' or '행'에 드랍
3. 표현방식 조정 (라인, 막대, 영역차트, 파이차트, 누적막대...)

- **차트 정렬**
1. '열'로 지정된 컬럼 우클릭 - '정렬'
