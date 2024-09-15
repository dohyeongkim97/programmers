-- 코드를 작성해주세요

SELECT ROUND(AVG(CASE 
                    WHEN length is null THEN 10 
                    ELSE length 
                END), 2) AS average_length
FROM fish_info;