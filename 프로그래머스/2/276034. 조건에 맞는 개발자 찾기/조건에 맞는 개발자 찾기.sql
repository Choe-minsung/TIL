-- 코드를 작성해주세요

# SKILL_CODE가 4, 16, 128, 256 ... 임
# 2진수(b)로 표현시 b100, b1000, b10000...이 되므로 &(비트연산자) 연산으로 연산속도 높이기!
# 256(Python) -> b10000000, 400(Python + Java + JavaScript) -> b11001000 / 256 & 400 -> b10000000 -> True!

SELECT ID, EMAIL, FIRST_NAME, LAST_NAME
    FROM DEVELOPERS AS D
    WHERE D.SKILL_CODE & (SELECT CODE
                         FROM SKILLCODES
                         WHERE NAME = 'Python')
          or
          D.SKILL_CODE & (SELECT CODE
                         FROM SKILLCODES
                         WHERE NAME = 'C#')
    ORDER BY ID;