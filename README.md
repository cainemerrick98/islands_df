# Islands Df

Inspired by the leet code count the number of islands challenge - islands df can take a spreadsheet sheet with multiple tables and create a dataframe for each table in the sheet. 

It works by implementing BFS each time it finds a node with data, the BFS algorithm remembers the top left and bottom right cell of table. The data from the sheet within these bounds is then 
passed to the pandas dataframe constructor and each created dataframe is returned in a list
