# Feature Engineering

[`Feature Engineering A-Z`](https://feaz-book.com/)  
[`youtube - Youhan Lee`](https://www.youtube.com/@YouHanLee)

- model 정확도 높이기 위해
- datasets - **train, test 둘 다 적용시켜야 함**

---
# EDA ~ CDA ~ Feature Engineering ~ ML pred 실습
[`Kaggle : Titanic`](https://www.kaggle.com/competitions/titanic/overview)

### Feature Engineering
- model의 정확성을 위해 데이터의 feature들을 가공하여주는 것

- 'Age' null값 처리
1. 177개의 결측치 존재, 'Name'에서 Mr. Mrs. 와 같은 호칭인 'Initial' 컬럼 추출
2. ('Age'가 null)이고 ('Initial'이 각각 ['Master', 'Miss', 'Mr', 'Mrs', 'Other']) 인 데이터를 해당 'Initial' 의 평균 'Age' 로 채우기
3. train 데이터셋의 'Initial' 데이터를 기반으로 train, test에 'Age'의 null값을 채우기

- 'Age' 컬럼을 continuous -> categorical 형변환
1. bin : -np.inf, 11, 21, 31, 41, 51, 61, 71, np.inf
2. label : 0, 1, 2, 3, 4, 5, 6, 7
3. pd.cut() 활용 범주화
(주의! : 정보손실 발생 가능성o)

- 'Embarked' null 처리
1. 2개의 'Embarked' 결측치 존재
2. 891개 중 2개이므로 max 값으로 처리

- 'Initial', 'Embarked' : categorical 처리
1. object -> categorical

- One-hot encoding
1. categorical 컬럼들을 (0, 1, 2, ...)이 아닌 여러 dummies 컬럼으로 만듦
2. model의 정확도 향상
