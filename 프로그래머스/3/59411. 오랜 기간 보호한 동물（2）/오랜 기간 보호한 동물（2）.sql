-- 코드를 입력하세요
select C.animal_id, C.name from
(
SELECT A.animal_id, A.name, (B.datetime - A.datetime) as times from 
animal_ins A left join animal_outs B
on A.animal_id = B.animal_id
order by times desc
limit 2
) C