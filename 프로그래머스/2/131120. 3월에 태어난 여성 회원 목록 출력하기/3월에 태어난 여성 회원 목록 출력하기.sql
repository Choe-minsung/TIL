-- 코드를 입력하세요

SELECT MEMBER_ID, MEMBER_NAME, GENDER,
        DATE_FORMAT(DATE_OF_BIRTH, "%Y-%m-%d") AS DATE_OF_BIRTH # 날짜컬럼 포맷지정
    FROM MEMBER_PROFILE
    WHERE MONTH(DATE_OF_BIRTH) = '3' # 생일이 3월인
        AND GENDER = 'W' # 여성회원
        AND TLNO IS NOT NULL # 전화번호가 NULL이 아닌
    ORDER BY MEMBER_ID ASC; # 회원ID 기준 오름차순 정렬