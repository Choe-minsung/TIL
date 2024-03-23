-- 코드를 입력하세요
SELECT PT_NAME, PT_NO, GEND_CD, AGE,
        COALESCE(TLNO, 'NONE') AS TLNO # 전화번호가 없는 경우, 'NONE'으로 출력
    FROM PATIENT
    WHERE AGE <= 12 AND GEND_CD = 'W'
    ORDER BY AGE DESC, PT_NAME ASC; # 나이를 기준으로 내림차순 정렬하고, 나이 같다면 환자이름을 기준으로 오름차순 정렬