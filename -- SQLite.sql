-- SQLite
select * from locations l 
left outer join inventory i on (l.id = i.location_id and i.product_id = 2) 
where i.location_id is null

select * from inventory i
where i.product_id == 2

select * from locations l 
left outer join inventory i on (l.id = i.location_id) 
where i.location_id is null

select * from products p
left outer join inventory i on (p.id == i.product_id)