-- 코드를 입력하세요
SELECT MCDP_CD as '진료과코드', count(*) as '5월예약건수'
from appointment
where month(APNT_YMD) = 5
and year(APNT_YMD) = 2022
group by MCDP_CD
order by count(*) asc, MCDP_CD asc
;