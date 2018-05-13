
/****************************************/
/***************PART A*******************/
/****************************************/

SELECT COUNT(*) FROM (
SELECT * FROM frequency WHERE docid="10398_txt_earn");


/****************************************/
/***************PART B*******************/
/****************************************/

SELECT COUNT(*) FROM (
SELECT term FROM frequency WHERE docid="10398_txt_earn" AND count=1);

/****************************************/
/***************PART C*******************/
/****************************************/

SELECT COUNT(*) FROM (
SELECT term FROM frequency WHERE docid="10398_txt_earn" AND count=1
UNION
SELECT term FROM frequency WHERE docid="925_txt_trade" AND count=1);

/****************************************/
/***************PART D*******************/
/****************************************/

SELECT COUNT(DISTINCT docid) FROM frequency WHERE term='law' OR term='legal';

/****************************************/
/***************PART E*******************/
/****************************************/

SELECT COUNT(*) FROM (
SELECT docid,COUNT(term) FROM frequency GROUP BY docid HAVING count(term)>300);


/****************************************/
/***************PART F*******************/
/****************************************/

SELECT 'The answer to part f is', COUNT(*) FROM (
SELECT DISTINCT a.docid FROM (SELECT * FROM frequency WHERE term='transactions') a JOIN (SELECT * FROM frequency WHERE term='world') b
ON a.docid=b.docid);







