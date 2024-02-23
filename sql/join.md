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

# where 절 subquery : 중첩 서브쿼리 (Nested Subquery)

SELECT MONTH(START_DATE) AS MONTH, CAR_ID,
        COUNT(*) AS RECORDS
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
    WHERE CAR_ID IN (SELECT CAR_ID
                     FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
                     WHERE START_DATE BETWEEN '2022-08-01' AND '2022-10-31'
                     GROUP BY CAR_ID
                     HAVING COUNT(*) >= 5)
            AND START_DATE BETWEEN '2022-08-01' AND '2022-10-31'
    GROUP BY MONTH, CAR_ID
    HAVING COUNT(*) > 0
    ORDER BY MONTH, CAR_ID DESC;
```
1. 전체 행 갯수 RECORDS 컬럼 정의
2. where 절에 대여 시작일 기준 2022년 8월 ~ 2022년 10월까지 총 대여 횟수가 5회 이상인 car_id 반환 중첩 서브쿼리 사용
3. where 절에 대여 시작일 기준 2022년 8월 ~ 2022년 10월까지 총 대여 횟수가 5회 이상인 조건 삽입
4. GROUP BY 절에 대여시작달, car_id HAVING 조건에 특정 월의 총 대여 횟수가 0인 경우 결과에서 제외
5. 정렬
6. sol





