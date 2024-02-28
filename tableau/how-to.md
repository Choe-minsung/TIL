# Tableau 배우기

(강의 : youtube - DK BMC tableau 강의)

### 환경

- version : Tableau Desktop 2024.01 ver

- 데이터 연결방식
1. 라이브 : 데이터 원본과 동기화 (원본 수정시 시각화에도 실시간 반영)
2. 추출 : Hyper 형태로 원본을 불러와 처리속도 빠름o

- 데이터 유형
1. ![image](https://github.com/Choe-minsung/TIL/assets/145301343/b99c3734-9f94-441e-84ba-bce3e58e80d9) : 텍스트
2. ![image](https://github.com/Choe-minsung/TIL/assets/145301343/98cc2f2e-8918-4559-8e35-b65679506065) : 날짜(달력)
3. ![image](https://github.com/Choe-minsung/TIL/assets/145301343/ca44b6aa-ffe4-4c7c-bf83-0f31a5fb63ab) : 날짜+시간
4. ![image](https://github.com/Choe-minsung/TIL/assets/145301343/e1330c23-48a7-4131-9a09-62a53c6451ff) : 숫자
5. ![image](https://github.com/Choe-minsung/TIL/assets/145301343/22d66edd-d6c1-44af-8745-6bdf5bd2e114) : boolean
6. ![image](https://github.com/Choe-minsung/TIL/assets/145301343/c86026ae-370d-4600-8468-a03e8277cf2c) : map

- 데이터 결합 (관계) : 각각 테이블 더블클릭
1. 동일컬럼 존재시에만 결합 가능 (key 컬럼이 고유값인지 확인! 아니면 중복발생)
2. 먼저 불러온 테이블이 outer table (root table) 로 삭제시 하위 테이블 모두 삭제됨
3. 일 : 다, 다 : 다 ...

- 데이터 결합 (join) : 1개의 테이블 더블클릭 - 열기 - 2번째 테이블 더블클릭
1. inner, left, right, outer 조인방식 설정 가능

- 데이터 결합 (union)
1. 시트에 union 할 2개의 테이블 불러오기 : 하단탭 데이터 원본에서 1개 테이블 더블클릭 - 하단탭 시트 1 - 상단탭 데이터 - 새 데이터원본 - 원하는 excel파일 - 다시 하단탭 데이터 원본에서 새 테이블 더블클릭 - 하단탭 시트 1  
<img width="150" alt="image" src="https://github.com/Choe-minsung/TIL/assets/145301343/e6e1e299-b3a8-420e-a6d1-820b8889546e">

2. 열설정, 마크(data) 설정 : 첫번째 테이블클릭 -  열로 설정할 컬럼 '열'에 드랍 - 두번째 테이블클릭 - 마크(data)로 설정할 컬럼 '마크 - 텍스트'에 드랍
<img width="490" alt="image" src="https://github.com/Choe-minsung/TIL/assets/145301343/dbf6467d-1a4b-475b-a2a8-894bdc90f07d">
