select a.name as employee from employee a where a.salary > (select b.salary from employee b where b.id = a.managerid)

-- Another way

select a.name as employee from employee a join employee b on a.managerid = b.id where a.salary > b.salary