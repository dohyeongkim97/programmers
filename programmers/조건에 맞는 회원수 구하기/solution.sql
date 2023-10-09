// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/131535

-- 코드를 입력하세요
SELECT count(*) from USER_INFO
where joined between '2021-01-01' and '2021-12-31'
and age between 20 and 29;