-- 코드를 입력하세요

SELECT A.car_id from 
car_rental_company_rental_history A left join car_rental_company_car B
on A.car_id = B.car_id
where month(A.start_date) = 10
and B.car_type = '세단'
group by A.car_id
order by A.car_id desc