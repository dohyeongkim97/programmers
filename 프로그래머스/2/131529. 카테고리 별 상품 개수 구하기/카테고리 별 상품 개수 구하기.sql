-- 코드를 입력하세요
SELECT substr(product_code, 1, 2) as category, count(*) FROM PRODUCT
group by substr(product_code, 1, 2)
order by category