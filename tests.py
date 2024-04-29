import unittest
from finding_islands import IslandFinderBfs
from islandsdf import IslandsDf

class TestIslandFinderBfs(unittest.TestCase):
    
    def setUp(self):
        self.sheet = [
            [1, 1, 0, 0, 0],
            [1, 1, 0, 0, 0],
            [0, 0, 0, 1, 1],
            [0, 0, 0, 1, 1],
            [0, 0, 0, 1, 1]
            ]

        self.empty_checked = [[0 for i in j] for j in self.sheet]
        self.island_finder = IslandFinderBfs()
        return super().setUp()
    
    def test_find_connected_nodes(self):
        """
        find connected nodes should find all adjacent nodes in the array
        if they equal to one and return their coordinates

        In this case (0,0) is connected to (1,0) and (0,1) and both are 1.
        Hence, it should return [(1,0), (0,1)] 
        """
        
        curr_node = (0, 0)
        expected_result = [(1, 0), (0, 1)]

        island_finder = IslandFinderBfs()
        
        connections = island_finder._IslandFinderBfs__find_connected_nodes(self.sheet, curr_node, self.empty_checked)

        self.assertListEqual(expected_result, connections)

    def test_find_tables_empty_array(self):
        """
        If find tables is passed an empty array (e.g. a sheet with no data) it should return an empty
        array
        """
        self.assertListEqual([], self.island_finder.find_tables(sheet=[]))
    
    def test_find_tables_non_empty_array(self):
        """
        when their is some data find tables should return the top left and bottom 
        right coordinates of the table in an array.
        Therefore, given the test data, find tables should return 
        [
            [0, 0, 1, 1],
            [2, 3, 4, 4]
        ]
        """
        expected_result = [
            [0, 0, 1, 1],
            [2, 3, 4, 4]
        ]

        tables_coords = self.island_finder.find_tables(self.sheet)
        self.assertListEqual(expected_result, tables_coords)


class TestIslandsDf(unittest.TestCase):

    def setUp(self) -> None:
        self.path = r'C:\Users\caine\OneDrive\Documents\islands_df\test_data_1.csv'
        self.islands_df = IslandsDf()
    
    def test_read_file(self):
        """
        Should read all of the data in the file and return an array containing all the cells
        within the range between the topleft data cell and the bottomright data cell
        """
        expected_data = [
            ['Name', 'Age', 'Employed', '', '', '', ''], 
            ['Caine', 26, 'TRUE', '', '', '', ''], 
            ['Charlotte', 25, 'FALSE', '', '', '', ''], 
            ['Karen', 30, 'FALSE', '', '', '', ''], 
            ['Keir', 30, 'TRUE', '', '', '', ''], 
            ['Andy', 60, 'TRUE', '', '', '', ''], 
            ['', '', '', '', '', '', ''], 
            ['', '', '', '', 'Model', 'Make', 'Horse Power'], 
            ['', '', '', '', 'Ford', 'Fiesta', 100], 
            ['', '', '', '', 'Ford', 'X1', 75], 
            ['', '', '', '', 'VW', 'Caddy', 60], 
            ['', '', '', '', 'Seat', 'IBIZA', 40]
            ]
        data = self.islands_df.read_file(self.path)
        self.assertListEqual(data, expected_data)

    def test_transform_data(self):
        """
        Should replace cells with data with a 1 and cells without data with a 0
        """
        expected_data = [
            [1, 1, 1, 0, 0, 0, 0], 
            [1, 1, 1, 0, 0, 0, 0], 
            [1, 1, 1, 0, 0, 0, 0], 
            [1, 1, 1, 0, 0, 0, 0], 
            [1, 1, 1, 0, 0, 0, 0], 
            [1, 1, 1, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 1, 1, 1], 
            [0, 0, 0, 0, 1, 1, 1],
            [0, 0, 0, 0, 1, 1, 1],
            [0, 0, 0, 0, 1, 1, 1],
            [0, 0, 0, 0, 1, 1, 1],
            ]
        file_data = self.islands_df.read_file(self.path)
        transformed_data = self.islands_df.transform_data(file_data)
        self.assertListEqual(transformed_data, expected_data)

    def test_extract_tables(self):
        """
        Should return two dataframes with the structure as below
        """
        dataframes = self.islands_df.extract_tables(self.path)
        self.assertEqual(2, len(dataframes))

        df1, df2 = dataframes
        self.assertEqual(5, len(df1))
        self.assertEqual(4, len(df2))

        df1_cols = ['Name', 'Age', 'Employed']
        df2_cols = ['Model', 'Make', 'Horse Power']
        self.assertListEqual(df1.columns.tolist(), df1_cols)
        self.assertListEqual(df2.columns.tolist(), df2_cols)

