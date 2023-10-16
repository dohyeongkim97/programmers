// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/133025

-- 코드를 입력하세요
SELECT A.FLAVOR
FROM FIRST_HALF A
JOIN ICECREAM_INFO B ON A.FLAVOR = B.FLAVOR
WHERE B.INGREDIENT_TYPE = 'fruit_based'
AND A.TOTAL_ORDER >= 3000;