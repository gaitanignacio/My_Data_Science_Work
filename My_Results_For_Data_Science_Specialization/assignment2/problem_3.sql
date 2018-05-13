/****************************************/
/***************PART H*******************/
/****************************************/

--SELECT 'This is matrix A';
--SELECT docid , term , count FROM frequency LIMIT 5;
--SELECT 'This is matrix At';
--SELECT term, docid, count FROM frequency LIMIT 5;
--SELECT 'This is matrix C = A x At';
--SELECT a.docid as docid_row,b.docid as docid_col, SUM (a.count*b.count) as value 
--FROM frequency as A JOIN frequency as B on a.term=b.term
--WHERE b.docid='10080_txt_crude' and a.docid='17035_txt_earn'
--GROUP BY a.docid,b.docid;

/****************************************/
/***************PART I*******************/
/****************************************/

SELECT 'This is matrix of Similarity';
SELECT a.docid as docid_row,b.docid as docid_col, SUM (a.count*b.count) as value 
FROM (
SELECT * FROM frequency
UNION
SELECT 'q' as docid, 'washington' as term, 1 as count 
UNION
SELECT 'q' as docid, 'taxes' as term, 1 as count
UNION 
SELECT 'q' as docid, 'treasury' as term, 1 as count) as A JOIN 
(
SELECT * FROM frequency
UNION
SELECT 'q' as docid, 'washington' as term, 1 as count 
UNION
SELECT 'q' as docid, 'taxes' as term, 1 as count
UNION
SELECT 'q' as docid, 'treasury' as term, 1 as count) as B on a.term=b.term
WHERE a.docid='q'
GROUP BY a.docid,b.docid
ORDER BY 3 desc
LIMIT 10;
