-- 코드를 입력하세요
# used goods file
# used goods board
# select * from 
# (
select concat('/home/grep/src/', B.board_id, '/', B.file_id, B.file_name, B.file_ext) from (
SELECT * from 
used_goods_board
order by views desc
limit 1) A
join 
used_goods_file B
on A.board_id = B.board_id
order by file_id desc
