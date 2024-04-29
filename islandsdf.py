from finding_islands import IslandFinderBfs
import pyexcel as excl
import pandas as pd

class IslandsDf:
    """
    Inspired by the number of islands leet code problem: https://leetcode.com/problems/number-of-islands/description/
    
    This class can take a csv, xls or xlsx filepath and will return a data frame for each table in the spreadsheet. A table
    is defined by a region of cells with data inside them entirely surrounded by cells with no data.
    """
    def __init__(self):
        self.island_finder = IslandFinderBfs()


    def extract_tables(self, path:str, sheet_name:str=''):
        """
        This is the main method on the class. It reads the files, uses the island finder to find the islands
        and then extracts the tables and returns them as a dictionary of pandas dataframes
        """
        data = self.read_file(path, sheet_name)
        transformed_data = self.transform_data(data)
        table_coords = self.island_finder.find_tables(transformed_data)

        tables = []
        for coords in table_coords:
            top_row, top_col, bottom_row, bottom_col = coords
            df_data = [row[top_col:bottom_col+1] for row in data[top_row:bottom_row+1]]
            df_columns = df_data.pop(0)

            df = pd.DataFrame(columns=df_columns, data=df_data)
            tables.append(df)
        
        return tables
            


    
    def read_file(self, path:str, sheet_name:str=''):
        """
        Uses pyexcel to read the data in the file. returns the data in the file as a list of 
        lists. 
        """
        sheet = excl.get_sheet(file_name=path, sheet_name=sheet_name)
        data = sheet.to_array()
        return data
    
    def transform_data(self, data: list[list]) -> list[list[int]]:
        """
        transforms the data into 0s and 1s. 0s represent empty cells and 1s represent cells with data
        this how the search algorithm expects the data
        """

        transformed_data = [[1 if value != '' else 0 for value in row] for row in data]
        return transformed_data

    

