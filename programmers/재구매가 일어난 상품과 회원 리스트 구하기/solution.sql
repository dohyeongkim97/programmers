// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/131536

-- 코드를 입력하세요
SELECT USER_ID, PRODUCT_ID FROM ONLINE_SALE
GROUP BY USER_ID, PRODUCT_ID
HAVING COUNT(*)>=2
ORDER BY USER_ID ASC, PRODUCT_ID DESC;