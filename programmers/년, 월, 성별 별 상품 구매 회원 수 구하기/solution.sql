// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/131532

-- 코드를 입력하세요
SELECT 
    YEAR(B.SALES_DATE) AS YEAR,
    MONTH(B.SALES_DATE) AS MONTH,
    A.GENDER,
    COUNT(DISTINCT A.USER_ID) AS USERS
FROM USER_INFO A
JOIN ONLINE_SALE B 
ON A.USER_ID = B.USER_ID
WHERE A.GENDER IS NOT NULL
GROUP BY YEAR, MONTH, A.GENDER
ORDER BY YEAR, MONTH, A.GENDER