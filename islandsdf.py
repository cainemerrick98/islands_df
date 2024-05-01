from finding_islands import find_tables
import pyexcel as excl
import pandas as pd


def extract_tables(path:str, sheet_name:str=''):
    """
    Inspired by the number of islands leet code problem: https://leetcode.com/problems/number-of-islands/description/
    
    This function can take a csv, xls or xlsx filepath and will return a data frame for each table in the spreadsheet. A table
    is defined by a region of cells with data inside them entirely surrounded by cells with no data.
    """
    data = read_file(path, sheet_name)
    transformed_data = transform_data(data)
    table_coords = find_tables(transformed_data)

    tables = []
    for coords in table_coords:
        top_row, top_col, bottom_row, bottom_col = coords
        df_data = [row[top_col:bottom_col+1] for row in data[top_row:bottom_row+1]]
        df_columns = df_data.pop(0)

        df = pd.DataFrame(columns=df_columns, data=df_data)
        tables.append(df)
    
    return tables
        



def read_file(path:str, sheet_name:str=''):
    """
    Uses pyexcel to read the data in the file. returns the data in the file as a list of 
    lists. 
    """
    sheet = excl.get_sheet(file_name=path, sheet_name=sheet_name)
    data = sheet.to_array()
    return data

def transform_data(data: list[list]) -> list[list[int]]:
    """
    transforms the data into 0s and 1s. 0s represent empty cells and 1s represent cells with data
    this how the search algorithm expects the data
    """
    transformed_data = [[1 if value != '' else 0 for value in row] for row in data]
    return transformed_data



