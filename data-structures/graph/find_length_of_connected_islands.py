class Island():
    def __init__(self, island, row, column):
        self.island = island
        self.row = row
        self.column = column

    def visit_and_mark_island(self, row, column):
        if row < 0 or row >= self.row or column < 0 or column >= self.column or self.island[row][column] != 1:
            return
        self.island[row][column] = -1

        self.visit_and_mark_island(row-1, column-1)
        self.visit_and_mark_island(row-1, column)
        self.visit_and_mark_island(row-1, column+1)
        self.visit_and_mark_island(row, column-1)
        self.visit_and_mark_island(row, column+1)
        self.visit_and_mark_island(row+1, column-1)
        self.visit_and_mark_island(row+1, column)
        self.visit_and_mark_island(row+1, column+1)

    def count_connected_islands(self):
        connected_island = 0
        for i in range(self.row):
            for j in range(self.column):
                if self.island[i][j] == 1:
                    self.visit_and_mark_island(i, j)
                    connected_island += 1

        print("Number of Connected Island: ", connected_island)


if __name__ == "__main__":
    islands = [
        [1, 1, 0, 0, 0],
        [0, 1, 0, 0, 1],
        [1, 0, 0, 1, 1],
        [0, 0, 0, 0, 0],
        [1, 0, 1, 0, 1]
    ]
    no_of_rows = len(islands)
    no_of_columns = len(islands[0])
    Island(islands, no_of_rows, no_of_columns).count_connected_islands()
