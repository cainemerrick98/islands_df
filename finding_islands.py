from collections import deque

class IslandFinderBfs:
    """ 
    A class for implementing the algorithm to find each table within 
    the dataset.
    """
    def __init__(self):
        pass

    
    def find_tables(self, sheet: list[list[int]]) -> list[list[int]]:
        """
        Finds the top left and bottom right cell for all of the tables 
        in the array passed and returns them in a list of lists.
        """
        table_coords = []
        checked = [[0 for j in range(len(i))] for i in sheet]

        for row in range(len(sheet)):
            for col in range(len(sheet[0])):
                if sheet[row][col] == 1 and checked[row][col] == 0:
                    checked[row][col] = 1
                    b_row, b_col = self.__bfs(sheet, (row, col), checked)
                    table_coords.append([row, col, b_row, b_col])
        
        return table_coords

    def __bfs(self, sheet: list[list[int]], root:tuple, checked:list[list[int]]) -> tuple[int, int]:
        """
        An impmenentation of breadth first search. Used to find all the cells with data
        connected to the cell with data in the top left of the table (the root)
        """
        search_queue = deque()
        search_queue.append(root)
        bottom_right = (root[0], root[1])
        while len(search_queue):
            curr_node = search_queue.popleft()
            if curr_node[0] >= bottom_right[0] and curr_node[1] >= bottom_right[1]:
                bottom_right = curr_node
            
            search_queue.extend(self.__find_connected_nodes(sheet, curr_node, checked))
        
        return bottom_right

    def __find_connected_nodes(self, sheet: list[list[int]], curr_node:tuple, checked:list[list[int]]) -> list[tuple[int, int]]:
        """
        A helper function to return the cells connected to curr node
        """
        moves = [(1,0), (0,1), (-1,0), (0,-1)]
        connections = []
        for move in moves:
            row = curr_node[0] + move[0]
            col = curr_node[1] + move[1]

            if row >= 0 and row<len(sheet) and col>=0 and col<len(sheet[0]):
                if checked[row][col] == 0 and sheet[row][col] == 1:
                    checked[row][col] = 1
                    connections.append((row, col))
        return connections
