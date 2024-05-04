# AutoML

[`AutoML.org`](https://www.automl.org/automl/)  

---

### AutoML description
- AutoML : Automated Machine Learning, 자동화된 ML
- 반복적이고 시간소요가 많은 모델 적합 과정 및 성능 검증 과정을 자동화

### AutoML libraries
1. **Pycaret** : 기존 Scikit-learn, XGBoost, LightGBM, spaCy 등 다양한 머신러닝 라이브러리를 ML High-Level API로 제작 / 데이터 분석 및 머신러닝 모델 성능 비교, Log 생성 및 이력 확인 가능
   - PyCaret 지원 모듈  
    지도학습 : 분류, 회귀  
    비지도학습 : 클러스터링, 이상탐지, 자연어처리, 연관규칙마이닝  
    시계열분석  
 
3. **H2O** AutoML
4. **TPOT** : genetic programming
5. **LightAutoML** : light ML Workflow based text

---
# AutoML library 활용 실습

[`HD현대 AI Challenge`](https://dacon.io/competitions/official/236158/codeshare/9222?page=1&dtype=recent)

### Pycaret
[`PyCaret docs`](https://pycaret.gitbook.io/docs)  
[`PyCaret setup`](https://pycaret.readthedocs.io/en/latest/api/regression.html)

```
# install PaCaret
!pip install pycaret
!pip install markupsafe == 2.0.1
```

```
from pycaret.regression import *
setup_reg = setup(data = train, target = 'CI_HOUR', train_size = .8, session_id = 42, fold = 5)
```
![image](https://github.com/Choe-minsung/TIL/assets/145301343/9cb35dde-7527-4426-9b4a-2336370acee7)

```
best = compare_models(sort = 'mae')
```
![image](https://github.com/Choe-minsung/TIL/assets/145301343/b2574840-26d2-413b-860e-3e0bf7c06449)
