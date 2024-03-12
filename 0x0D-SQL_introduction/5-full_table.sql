-- Script to print full description of table first_table
SELECT CONCAT('Table: ', table_name, '\n', 
              'Create Table: ', create_statement) AS Description
FROM information_schema.tables
WHERE table_schema = 'hbtn_0c_0'
AND table_name = 'first_table';
