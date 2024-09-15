-- 코드를 작성해주세요

select count(*) as FISH_COUNT, name.fish_name as FISH_NAME from 
fish_info info 
left join fish_name_info name 
on info.fish_type = name.fish_type
group by name.fish_name
order by FISH_COUNT desc;
