from flask.scaffold import F

import linecache


class Puzzle:
    """
    A class that will hold logic for the sudoku board, including the numbers, their positions and board methods.
    """

    def __init__(self, n):
        self.grid = []
        self.rawGrid = []
        self.mistake = False
        self.full = False
        self.complete = False
        self.id = n

        self.genNewPuzzle(n)

    def genNewPuzzle(self, n):
        """
        Read the input of the nth line of sudokus.txt and fill in the blank playing grid attribute 
        as well as the rawGrid to act as a template, so game.html knows when an element is player input. 

        The way the grid will be formated in the page is of the form grid[y][x], where the y value is the rows.
        """
        try:
            line = linecache.getline("sudokus.txt", n)[:-1]
        except:
            print("An error has occurred")
        else:
            for i in range(9):
                self.grid.append([])
                self.rawGrid.append([])

                for char in line[(i*9): ((i + 1) * 9)]:
                    if char == "0": char = ""
                    self.grid[i].append(char)
                    self.rawGrid[i].append(char)

    def isFull(self):
        """
        Check if the game is full.
        """
        return self.full

    def madeMistake(self):
        return self.mistake
        

    def isLegal(self):
        """
        Check if the board is legal. First check the rows to make sure there are no duplicates (so must contain numbers 1-9), then do the same with the columns,
        and finally, do the same with each square.
        """
        #Rows
        for i in range(9):
            if self.__containsDuplicates(self.grid[i]):
                return False
        
        #Columns
        for j in range(9):
            columnList = []
            for i in range(9):
                columnList.append(self.grid[i][j])
            if self.__containsDuplicates(columnList):
                return False
        
        #Squares
        #Loop through the rows 3 at a time.
        for n in range(3):
            #For each set of 3 rows loop through the columns 3 at a time.
            for m in range(3):
                square = []
                #Now loop through our square, adding elements to a list to be checked for duplicates.
                for k1 in range(3*n, 3*n+3):
                    for k2 in range(3*m, 3*m+3):
                        square.append(self.grid[k1][k2])
                
                if self.__containsDuplicates(square):
                    return False
        return True

    def isOver(self):
        """
        Checks if the game is over, and if it is changes the complete attribute. If it is full but not correct it updates the mistake attribute.
        """
        if self.isFull():
            if self.isLegal():
                self.complete = True
            else:
                self.mistake = True


    @staticmethod
    def __containsDuplicates(aList):
        """
        return True if a list contains a duplicate, false otherwise.
        """
        for i in range(len(aList)):
            if aList[i] in aList[i+1:]:
                return True
        return False

    def updateGrid(self, data):
        """
        Takes user input and updates the grid with the new data. It also checks if the grid is full.
        """
        if data:
            self.full = True
            for index, value in data.items():
                if not value == "":
                    j, i = int(index[0]), int(index[2])
                    self.grid[j][i] = value
                else:
                    self.full = False

            


# if __name__ == "__main__":
#     sudoku = Puzzle()
#     sudoku.genNewPuzzle()
