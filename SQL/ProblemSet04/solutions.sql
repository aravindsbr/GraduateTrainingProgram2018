1)Find the names of all students who are friends with someone named Gabriel.

1- select name from highschooler where id in(select id2 from friend where id1 in(select ID from highschooler where name = 'Gabriel'));
2- select h.name from highschooler h inner join friend f on h.ID=f.ID1 inner join highschooler h1 on h1.ID=f.ID2 where h1.name='Gabriel';
3- select name from highschooler where ID in (select ID2 from friend where ID1 = 1911 or ID1 = 1689);

op-
Jordan
Cassandra
Andrew
Alexis
Jessica

2)For every student who likes someone 2 or more grades younger than themselves, return that student's name and grade,
 and the name and grade of the student they like.

 select name1,grade1,name2,grade2 from
   ...> ( select h1.name as name1,h1.grade as grade1,h2.name as name2,h2.grade as grade2, h1.grade-h2.grade as difference
   ...> from highschooler h1 inner join likes l on l.id1=h1.id
   ...> inner join highschooler h2 on l.id2=h2.id)
   ...> where difference>=2;

John|12|Haley|10

4)Find all students who do not appear in the Likes table (as a student who likes or is liked) and return their names and grades. 
Sort by grade, then by name within each grade.

select name,grade from highschooler where id not in
   ...> (select id1 from likes)
   ...> union
   ...> select name,grade from highschooler where id not in
   ...> (select id2 from likes) order by grade,name;


Jordan|9
Tiffany|9
Andrew|10
Brittany|10
Haley|10
Kris|10
Austin|11
Gabriel|11
John|12
Jordan|12
Logan|12
