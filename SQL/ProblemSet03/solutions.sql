1)Find the titles of all movies directed by Steven Spielberg. (1 point possible)

select title from movie where director='Steven Spielberg';

E.T.

2)Find all years that have a movie that received a rating of 4 or 5, and sort them in increasing order. 

select m.year from movie m inner join Rating r on m.mID=r.mID where stars=4 or stars=5 order by year;

1937
1937
1939
1981
1981
2009

3)Find the titles of all movies that have no ratings. 
select title from movie where mID not in (select mId from Rating);

star wars
Titanic

4)Some reviewers didn't provide a date with their rating. Find the names of all reviewers who have ratings with a NULL value for the date.

select name from reviewer where rID in (select rID from rating where ratingDate is NULL);

Daniel Lewis

5)Write a query to return the ratings data in a more readable format: reviewer name, movie title, stars, and ratingDate. Also, sort the data, first by reviewer name, then by movie title, and lastly by number of stars.

select r.name,m.title,rt.stars,rt.ratingDate from Reviewer r join Rating rt on r.rid=rt.rid join Movie m on rt.mID=m.mID
 order by r.name,m.title,rt.stars desc;

Ashley White|E.T.|3|2011-01-02
Brittany Harris|Raiders of the Lost Ark|4|2011-01-12
Brittany Harris|Raiders of the Lost Ark|2|2011-01-30
Brittany Harris|The Sound of Music|2|2011-01-20
Chris Jackson|E.T.|2|2011-01-22
Chris Jackson|Raiders of the Lost Ark|4|
Chris Jackson|The Sound of Music|3|2011-01-27
Daniel Lewis|Snow White|4|
Elizabeth Thomas|Avatar|3|2011-01-15
Elizabeth Thomas|Snow White|5|2011-01-19
James Cameron|Avatar|5|2011-01-20
Mike Anderson|Gone with the wind|3|2011-01-09
Sarah Martinez|Gone with the wind|4|2011-01-27
Sarah Martinez|Gone with the wind|2|2011-01-22

6)For all cases where the same reviewer rated the same movie twice and gave it a higher rating the second time, return the reviewer's name and the title of the movie.

select r.name,m.title from Reviewer r join
   ...> Rating rt on r.rid=rt.rid
   ...> join Movie m on rt.mID=m.mID
   ...> group by rt.rid,rt.mid having count(rt.rid)>1;  

7)For each movie that has at least one rating, find the highest number of stars that movie received. Return the movie title and number of stars. Sort by movie title. 

select max(rt.stars),m.title from Rating rt inner join Movie m on rt.mID=m.mID group by m.title order by m.title;

5|Avatar
3|E.T.
4|Gone with the Wind
4|Raiders of the Lost Ark
5|Snow White
3|The Sound of Music

8)For each movie, return the title and the 'rating spread', that is, the difference between highest and lowest ratings given to that movie. Sort by rating spread from highest to lowest, then by movie title.

select m.title,max(rt.stars)-min(rt.stars) as Rating_spread from Rating rt inner join Movie m on rt.mID=m.mID group by m.title order by Rating_spread desc, m.title;

Avatar|2
Gone with the Wind|2
Raiders of the Lost Ark|2
E.T.|1
Snow White|1
The Sound of Music|1

10)Find the names of all reviewers who rated Gone with the Wind.

select name from Reviewer where rID=(select rID from Rating where mID=(select mID from Movie where title='Gone with the Wind'));

Sarah Martinez

11)For any rating where the reviewer is the same as the director of the movie, return the reviewer name, movie title, and number of stars.

select rt.stars,m.title,r.name from Movie m inner join Reviewer r on m.director=r.name inner join Rating rt on r.rID=rt.rID;

5|Titanic|James Cameron
5|Avatar|James Cameron

12. Return all reviewer names and movie names together in a single list, alphabetized. (Sorting by the first name of the reviewer and first word in the title is fine; no need for special processing on last names or removing "The".)
select r.name,m.title from Rating r1 inner join Movie m on r1.mID=m.mID inner join Reviewer r on r1.rID=r.rID order by r.name,m.title;

Ashley White|E.T.
Brittany Harris|Raiders of the Lost Ark
Brittany Harris|Raiders of the Lost Ark
Brittany Harris|The Sound of Music
Chris Jackson|E.T.
Chris Jackson|Raiders of the Lost Ark
Chris Jackson|The Sound of Music
Daniel Lewis|Snow White
Elizabeth Thomas|Avatar
Elizabeth Thomas|Snow White
James Cameron|Avatar
Mike Anderson|Gone with the Wind
Sarah Martinez|Gone with the Wind
Sarah Martinez|Gone with the Wind
                                                                                   
