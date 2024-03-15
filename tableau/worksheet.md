# 워크시트

[`Tableau 도움말`](https://help.tableau.com/current/pro/desktop/ko-kr/datafields_typesandroles_datatypes.htm)  
[`youtube - DK BMC`](https://www.youtube.com/@DKBMCOfficial)  

### 환경

- version : Tableau Desktop 2024.01 ver

---
### 마크 활용  
- *레이블 세부설정*  
1. '열'에 (국가/지역), '행'에 (매출) - '마크-레이블'에 (매출),(수량),(수익) 드랍  
2. **'마크-레이블-택스트...-'** 클릭 - **'매출 : <합계(매출)> 원'** 으로 레이블 수정 - **'마크-레이블-...-맞춤-방향'** 설정  
3. **'마크-세부정보'** 에 (범주), (할인율) 드랍 - **'마크-도구설명'** 클릭 - 필드명은 볼드체, 전체 글꼴색 초록색으로 변경  

<img width="450" alt="image" src="https://github.com/Choe-minsung/TIL/assets/145301343/bfe880b4-4448-4d0e-8349-62a8aa47c58a">  

### 서식 계층  
- 계층순서 : 1. 워크시트 - 2. 행/열 - 3. 특정필드, 필드 레이블 - 4. 도구설명, 제목, 마크  
- 상위계층 변경 후 하위계층 변경해야 상위계층의 변경사항 유지o  

1. 워크시트 : 상단탭 **'서식-통합문서'** 클릭 - 좌측탭 '글꼴' 에서 원하는 구역의 글꼴서식 변경o    
  <img width="450" alt="image" src="https://github.com/Choe-minsung/TIL/assets/145301343/6689dd42-58e5-4e3f-93fd-fe3c1d2b7104">  
  
2. 행/열 : 상단탭 **'서식-글꼴'** 클릭 - 좌측탭 '글꼴서식'에서 시트/행/열 탭 별 글꼴서식 변경o  
<img width="450" alt="image" src="https://github.com/Choe-minsung/TIL/assets/145301343/76525833-5d19-4a42-8f04-8ab1fa8a96c1">

 3. 특정필드, 필드 레이블 : 시트에 **원하는 필드** 위에 **우클릭** 후 '서식' 클릭 - 글꼴서식 변경o  

 4. 제목, 마크 : **'마크-텍스트-...'** 클릭 - 텍스트 편집 및 글꼴서식 변경o
<img width="344" alt="image" src="https://github.com/Choe-minsung/TIL/assets/145301343/822e58b3-bc31-4995-b660-47c71a6ffc93">

5. 모든 서식 설정 초기화 : 상단탭 **'서식-워크시트 서식 지우기'** 클릭  

### 서식   
- *서식 - 글꼴, 맞춤, 음영 실습*  
1. '행'에 (지역), (국가/지역) 드랍, '열'에 (범주), (하위범주) 드랍 - (매출) 더블클릭 하여 '마크-텍스트' 에 올리기  
2. 좌상단 탭 **'분석-총계'** 더블클릭 - **'서식-글꼴'** 클릭 - '시트' 탭에서 '워크시트'는 전체, '패널'은 데이터값, '머리글'은 행/열, '총계-패널'은 총계 데이터값  
<img width="158" alt="image" src="https://github.com/Choe-minsung/TIL/assets/145301343/2085ba3f-d9b1-415a-8e42-8949ffb3eb8c">

3. **'서식-맞춤'** : 데이터의 배열, 방향 등 설정o  
<img width="158" alt="image" src="https://github.com/Choe-minsung/TIL/assets/145301343/38dfe76a-701e-40de-af2c-e4fa8ae28352">

4. **'서식-음영'** : 셀의 음영 설정o  
<img width="120" alt="image" src="https://github.com/Choe-minsung/TIL/assets/145301343/70729fc1-eb3e-401a-b80d-fe044e964699">
