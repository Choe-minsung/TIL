-- 코드를 입력하세요

SELECT *
    FROM FOOD_PRODUCT
    WHERE PRICE = (SELECT MAX(PRICE)  # subquery : price가 max(price)인 조건
                    FROM FOOD_PRODUCT);