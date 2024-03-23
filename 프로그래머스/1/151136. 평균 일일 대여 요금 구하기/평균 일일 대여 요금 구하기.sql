-- 코드를 입력하세요
SELECT ROUND(AVG(DAILY_FEE), 0) AS AVERAGE_FEE  # 소수 첫 번째 자리에서 반올림
    FROM CAR_RENTAL_COMPANY_CAR 
    WHERE CAR_TYPE = 'SUV'; #  자동차 종류가 'SUV'