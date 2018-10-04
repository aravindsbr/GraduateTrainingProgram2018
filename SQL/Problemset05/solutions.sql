1)Give the organiser's name of the concert in the Assembly Rooms after the first of Feb, 1997.

select m.m_name from musician m inner join concert c on m.m_no=c.concert_orgniser where concert_venue='Assembly Rooms' and con_date>'1997-02-01';

James Steeple

2)Find all the performers who played guitar or violin and were born in England.

select m.m_name from musician m inner join performer p on m.m_no=p.perf_is inner join place pl on m.born_in=pl.place_no where (p.instrument='guitar' or p.instrument='violin') and pl.place_country='England';

Harry Forte
Harriet Smithson
Davis Heavan
James First
Theo Mengel
Alan Fluff

3)List the names of musicians who have conducted concerts in USA together with the towns and dates of these concerts.

select m.m_name,pl.place_town,c.con_date from musician m join concert c on m.m_no=c.concert_orgniser join place pl on pl.place_no=c.concert_in where place_country='USA';

James Steeple|New York|1997-06-15

4)How many concerts have featured at least one composition by Andy Jones? List concert date, venue and the composition's title.

select con.con_date,con.concert_venue,com.c_title from concert con inner join composition com on con.concert_in=com.c_in inner join musician m on m.m_no=con.concert_orgniser where m.m_name='Andy Jones';
