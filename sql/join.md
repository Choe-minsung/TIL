# Join

[`MySQL JOIN`](https://dev.mysql.com/doc/refman/8.0/en/join.html)


### Join 

1. 두개의 테이블 연결시켜 원하는 데이터 추출
2. Outer Table (Pk) **1 : M** Inner Table (FK)


### 구조

1. **Nested Loop Join** : 중첩 for문 역할
- **OLTP** (Online Transaction Processing, 정교한 소규모 데이터 높은빈도 처리) 환경에 적절
- Outer Table(소량 데이터) **1 : M** Inner Table(다량 데이터)
- Inner Table의 index 걸려있지 않으면 비효율적 (full scan 해야함)


2. **Sort Merge Join**
- 두 테이블을 join 컬럼 기준으로 PGA(Program Global Area) 영역 내에서 빠르게 정렬 후 join
- Inner Table에 index 걸려있지 않을때 사용
- **Range Join** (<-> Equal Join) 에 사용
- Table Random Access (데이터 건수 감소, 큰 부하) 발생 x, 성능에 유리


3. **Hash Join** : 대용량 테이블 join, Batch (일괄처리) 시 사용
- **OLAP** (Online Analytical Processing, 대규모 데이터 낮은빈도 처리) 환경에 적절
- Outer Table을 Hash 영역에 추가 (Build Input 취급)
- Outer Table이 join 컬럼 기준으로 Hash Function 적용 (join 컬럼 중복값 없을수록 유리)
- Outer Table 크기 작을수록 유리
- Table Random Access (데이터 건수 감소, 큰 부하) 발생 x, 성능에 유리

___

### 문제예시 - [`특정 기간동안 대여 가능한 자동차들의 대여비용 구하기`](https://school.programmers.co.kr/learn/courses/30/lessons/157339) (Programmers)
```sql

# 가상테이블 생성
WITH CTE1 AS (
    SELECT *
    FROM CAR_RENTAL_COMPANY_CAR
    WHERE CAR_TYPE IN ('세단', 'SUV')
    ),
    
    CTE2 AS (
    SELECT *
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
    WHERE START_DATE > '2022-11-30' OR END_DATE < '2022-11-01'
    )

# CTE 확인
SELECT *
    FROM CTE1;
    
SELECT *
    FROM CTE2;

# main query
SELECT a.CAR_ID AS CAR_ID, a.CAR_TYPE AS CAR_TYPE,
    ROUND(IF(DATEDIFF(b.END_DATE, b.START_DATE) + 1 >= 90, a.DAILY_FEE * 30 * 0.9,
       IF(DATEDIFF(b.END_DATE, b.START_DATE) + 1 >= 30, a.DAILY_FEE * 30 * 0.93,
        IF(DATEDIFF(b.END_DATE, b.START_DATE) + 1 >= 7, a.DAILY_FEE * 30 * 0.95, a.DAILY_FEE * 30))), 0) AS FEE
    FROM CTE1 AS a
    JOIN CTE2 AS b ON a.CAR_ID = b.CAR_ID
    GROUP BY a.CAR_ID
    HAVING FEE BETWEEN 500000 AND 1999999
    ORDER BY FEE DESC, a.CAR_TYPE, a.CAR_ID DESC;
    


```
1. With 문으로 조건1(car_type이 '세단' or 'SUV'), 조건2(2022/11/01 ~ 2022/11/30에 대여기록이 없는) 에 맞는 테이블 각각 생성
2. FEE 컬럼 생성 : 각 대여기간에 따른 할인율 계산
3. car_id로 그룹핑, HAVING 조건절에 컬럼 별칭으로 FEE 조건 입력 (where 절에는 컬럼별칭으로 연산 불가)
4. 정렬
5. sol





