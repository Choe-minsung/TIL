# 대시보드

[`Tableau 도움말`](https://help.tableau.com/current/pro/desktop/ko-kr/datafields_typesandroles_datatypes.htm)  
[`youtube - DK BMC`](https://www.youtube.com/@DKBMCOfficial)  

### 환경

- version : Tableau Desktop 2024.01 ver

---

### 대시보드 예시
- *호주 대시보드(국기이미지, 호주매출, 호주설명-Wiki) 만들기*  
1. 하단탭 **'데이터원본'** 에서 **'주문'** 테이블의 **'국가/지역'** 컬럼의 데이터 유형을 **'지리적역할-국가/지역'** 으로 변경    
<img width="336" alt="image" src="https://github.com/Choe-minsung/TIL/assets/145301343/cb95b5ea-8108-4691-abae-db98406012b3">  

2. 하단탭 **'시트'** 에서 (국가/지역) 더블클릭 - 마크에 올라간 (국가/지역) 우클릭 후 필터에서 호주만 선택 - (매출)을 **'마크-색상'**, **'마크-레이블'** 에 올리기  
3. 하단탭 **'새 대시보드'** 클릭 - 좌삳단 탭 **'대시보드-크기'** 에서 **'PowerPoint 크기'** 추천
4. 만들어놓은 시트 1 더블클릭 - 좌하단 **'개체-텍스트'** 10시방향에 드랍 후 '호주(Austraila)' 입력 - **'개체-이미지'** 1시방향에 드랍 후 호주 국기 url 입력 - **'개체-웹페이지'** 5시방향에 드랍 후 WIkipedia url 입력

<img width="600" alt="image" src="https://github.com/Choe-minsung/TIL/assets/145301343/f0c97d1a-d4f7-416f-8690-ff0ef327ba52">


### 대시보드 구성
1. 바둑판식 : 레이아웃을 자동으로 비율 맞추어 구성해 줌
2. 부동 : 자유형식, 대시보드 크기 바뀌는경우 레이아웃이 어지러워짐
3. **추천** : 기본 - 바둑판식, 빈 공간에만 shift + 개체드랍 으로 텍스트 or 이미지 삽입
