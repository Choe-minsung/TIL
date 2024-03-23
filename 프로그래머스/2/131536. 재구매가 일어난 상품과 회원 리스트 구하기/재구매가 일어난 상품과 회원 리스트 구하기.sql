-- 코드를 입력하세요

SELECT USER_ID, PRODUCT_ID
    FROM ONLINE_SALE
    GROUP BY USER_ID, PRODUCT_ID  # 회원ID, 상품ID를 그룹핑
    HAVING COUNT(USER_ID) >= 2  # 각 세트가 2번이상인 경우 (재구매 한 경우)
    ORDER BY USER_ID, PRODUCT_ID DESC;