// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/59040

-- 코드를 입력하세요
SELECT ANIMAL_TYPE, COUNT(ANIMAL_TYPE) AS count
FROM ANIMAL_INS
WHERE ANIMAL_TYPE = 'CAT' OR ANIMAL_TYPE = 'DOG'
GROUP BY ANIMAL_TYPE
ORDER BY ANIMAL_TYPE