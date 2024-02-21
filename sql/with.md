# WITH 문

[`MySQL WITH (Common Table Expressions) `](https://dev.mysql.com/doc/refman/8.0/en/with.html)


### WITH 문이란

1. SubQuery 활용 이름을 가진 **가상테이블** (CTE) 정의
2. Query 가독성 향상, **재사용성**
3. **계층형쿼리** (순환절) 구현


### 구조

```sql
WITH 가상테이블명 AS (
  ~
  서브쿼리
  ~
  )

Main Query


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



