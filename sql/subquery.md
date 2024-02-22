# Subquery

[`MySQL Subquery`](https://dev.mysql.com/doc/refman/8.3/en/subqueries.html)


### Subquery 

1. 하나의 쿼리문안의 또 다른 쿼리문
2. 괄호로 감싸 사용, **비교연산자** 사용가능, ORDER BY 정렬 사용 x
3. 메인쿼리가 서브쿼리를 포함 (**종속관계**)
4. 쿼리 구조화시켜 가독성 o


### 구조

1. WHERE 절 : **중첩 서브쿼리** (Nested Subquery)

```sql
SELECT name, height 
FROM USER_T
WHERE height > (SELECT height FROM USER_T WHERE name IN ('김경호'));

```

2. FROM 절 : **인라인 뷰** (Inline View)
- AS 별칭 지정 필수!

```sql
SELECT name, salary
FROM (
  SELECT *
  FROM employee AS E
  WHERE E.office_worker = '사원'
  ) AS SUB;

```

3. SELECT 절 : **스칼라 서브쿼리** (Scalar Subquery)
- 1개의 행 값만 반환
- 2개 이상의 값 반환시 err : 'Subquery returns more than 1 row'

```sql
SELECT D.deptno, (SELECT MIN(empno) FROM EMP WHERE deptno = D.deptno) as EMPNO 
FROM DEPT AS D
ORDER BY D.DEPTNO;

```

___

### 문제예시 - [`대여 횟수가 많은 자동차들의 월별 대여 횟수 구하기`](https://school.programmers.co.kr/learn/courses/30/lessons/151139) (Programmers)
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




