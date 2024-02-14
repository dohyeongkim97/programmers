-- 코드를 입력하세요

SELECT MEMBER_ID, MEMBER_NAME, GENDER, DATE_FORMAT(DATE_OF_BIRTH, '%Y-%m-%d') AS DATE_OF_BIRTH 
from member_profile
where TLNO is not null
and month(date_of_birth) = 3
and gender = 'W'
order by member_id asc