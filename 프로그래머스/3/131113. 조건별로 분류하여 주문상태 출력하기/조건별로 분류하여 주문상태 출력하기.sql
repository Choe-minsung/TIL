-- 코드를 입력하세요
SELECT ORDER_ID, PRODUCT_ID,
        # 5/1 보다 작으
        COALESCE(DATE_FORMAT(OUT_DATE, '%Y-%m-%d'), NULL) AS OUT_DATE,
        IF(OUT_DATE <= '2022-05-01', '출고완료', IF(OUT_DATE IS NULL,'출고미정', '출고대기')) AS 출고여부
    FROM FOOD_ORDER
    ORDER BY ORDER_ID;  # 주문ID 기준 오름차순