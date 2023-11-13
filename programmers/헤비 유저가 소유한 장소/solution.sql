// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/77487

-- 코드를 입력하세요
SELECT B.ID, B.NAME, B.HOST_ID FROM(
SELECT * FROM PLACES
GROUP BY HOST_ID
HAVING COUNT(*) > 1) A
LEFT JOIN PLACES B ON A.HOST_ID = B.HOST_ID
ORDER BY B.ID;