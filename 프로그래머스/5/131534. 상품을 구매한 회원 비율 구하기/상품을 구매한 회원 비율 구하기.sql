# cte : 2021년에 가입한 회원 테이블
WITH CTE AS (
    SELECT O.USER_ID, O.SALES_AMOUNT, DATE_FORMAT(O.SALES_DATE, '%Y-%m-%d') AS SALES_DATE
        FROM USER_INFO AS I
        JOIN ONLINE_SALE AS O ON I.USER_ID = O.USER_ID
        WHERE YEAR(I.JOINED) = 2021
)

# cte 확인
# SELECT *
#     FROM CTE;
    

SELECT YEAR(SALES_DATE) AS YEAR, MONTH(SALES_DATE) AS MONTH,
        COUNT(DISTINCT(USER_ID)) AS PUCHASED_USERS,
        ROUND(COUNT(DISTINCT(USER_ID)) / (SELECT COUNT(*) FROM USER_INFO WHERE JOINED LIKE '2021%'), 1) AS PUCHASED_RATIO
    FROM CTE
    GROUP BY YEAR, MONTH
    ORDER BY YEAR, MONTH;