-- 코드를 입력하세요
SELECT ANIMAL_ID, NAME, 
    CASE 
        WHEN SEX_UPON_INTAKE LIKE '%Spayed%' or sex_upon_intake like '%Neutered%' THEN 'O' 
        ELSE 'X' 
    END AS '중성화'
FROM ANIMAL_INS
ORDER BY ANIMAL_ID asc;