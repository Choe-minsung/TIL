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

```sql
SELECT D.deptno, (SELECT MIN(empno) FROM EMP WHERE deptno = D.deptno) as EMPNO 
FROM DEPT AS D
ORDER BY D.DEPTNO;

```

___

### 문제예시 - [`상품을 구매한 회원 비율 구하기`](https://school.programmers.co.kr/learn/courses/30/lessons/131534) (Programmers)
```sql

# cte : 2021년에 가입한 회원 테이블
WITH CTE AS (
    SELECT O.USER_ID, O.SALES_AMOUNT, DATE_FORMAT(O.SALES_DATE, '%Y-%m-%d') AS SALES_DATE
        FROM USER_INFO AS I
        JOIN ONLINE_SALE AS O ON I.USER_ID = O.USER_ID
        WHERE YEAR(I.JOINED) = 2021
)

# cte 확인
SELECT *
    FROM CTE;
    
# main query
SELECT YEAR(SALES_DATE) AS YEAR, MONTH(SALES_DATE) AS MONTH,
        COUNT(DISTINCT(USER_ID)) AS PUCHASED_USERS,
        ROUND(COUNT(DISTINCT(USER_ID)) / (SELECT COUNT(*) FROM USER_INFO WHERE JOINED LIKE '2021%'), 1) AS PUCHASED_RATIO
    FROM CTE
    GROUP BY YEAR, MONTH
    ORDER BY YEAR, MONTH;
```
1. with 문으로 CTE 가상테이블 생성
2. main query에 FROM 절에 CTE 테이블 불러오기
3. SELECT 절 속 subquery 사용하여 USER_INFO 테이블의 가입년도가 2021년인 모든 행 갯수 반환
4. sol




