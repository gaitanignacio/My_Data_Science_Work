/****************************************/
/***************PART G*******************/
/****************************************/
SELECT 'This is matrix A';
SELECT row_num, col_num, value FROM A;
SELECT 'This is matrix B';
SELECT row_num, col_num, value FROM B;
SELECT 'This is matrix C = A x B';
--SELECT value FROM (
SELECT a.row_num as row_num,b.col_num as col_num,SUM (a.value*b.value) as value 
FROM A JOIN B on a.col_num=b.row_num
GROUP BY a.row_num,b.col_num;
--) WHERE row_num=2 AND col_num=3;

