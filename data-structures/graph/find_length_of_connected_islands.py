Class Island():
    def __init__(self, islands, no_of_rows, no_of_columns):
	self.islands = islands
	self.no_of_rows = no_of_rows
	self.no_of_columns = no_of_columns

if __name__ == "__main__":
    island = island(islands, no_of_rows, no_of_columns).findNumberOfConnectedIslands()
