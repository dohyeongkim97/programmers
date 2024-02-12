-- 코드를 입력하세요
select A.cart_id from
(
(SELECT cart_id, NAME from cart_products
where name like '%Milk%') A
inner join
(select cart_id, NAME from cart_products
where name like '%Yogurt') B
on A.cart_id = B.cart_id
) 