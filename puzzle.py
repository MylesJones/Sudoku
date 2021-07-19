from flask.scaffold import F

import linecache


class Puzzle:
    """
    A class that will hold logic for the sudoku board, including the numbers, their positions and board methods.
    """

    def __init__(self, n):
        self.grid = []

        #The way the grid is formated in the page is of the form grid[y][x], where the y value is the rows.

        # fill in the board to test the html.
        for i in range(9):
            self.grid.append([])
        self.genNewPuzzle(n)

    
    def genNewPuzzle(self, n):
        lineDict = {}
        
        try:
            line = linecache.getline("sudokus.txt", n)[:-1]
            # print(line)
            # print(len(line))
        except:
            print("An error has occurred")
        else:
            for i in range(9):
                lineDict[i] = line[(i*9): ((i + 1) * 9)]
                aList = []
                for char in lineDict[i]:
                    if char == "0":
                        char = ""
                    aList.append(char)
                self.grid[i] = aList
                # print(self.grid[i])

            


    def isOver(self):
        """
        Check if the game is over by first checking the board is legal, the check the board is complete.
        """

        if self.isLegal():
            #check board is full
            return True
        return False
        

    def isLegal(self):
        """
        Check if the board is legal.
        """
        #Check rows
        for i in range(9):
            if self.__containsDuplicates(self.grid[i]):
                return False
        
        #Check columns
        for j in range(9):
            columnList = []
            for i in range(9):
                columnList.append(self.grid[i][j])
            if self.__containsDuplicates(columnList):
                return False
        
        #check squares
        #Loop through the rows 3 at a time.
        for n in range(3):
            #For each set of 3 rows loop through the columns 3 at a time.
            for m in range(3):
                square = []
                for k1 in range(3*n, 3*n+3):
                    for k2 in range(3*m, 3*m+3):
                        square.append(self.grid[k1][k2])
                
                if self.__containsDuplicates(square):
                    return False
        return True




    @staticmethod
    def __containsDuplicates(aList):
        """
        return True if a list contains a duplicate, false otherwise.
        """
        for i in range(len(aList)):
            if aList[i] in aList[i+1:]:
                return True
        return False


if __name__ == "__main__":
    sudoku = Puzzle()
    sudoku.genNewPuzzle()
    # print(sudoku.__containsDuplicates([1, 2, 3, 4, 5, 6, 7, 8, 9]) == False)
    # print(sudoku.__containsDuplicates([1, 2, 3, 2, 4, 5, 6, 8, 9]) == True)
    

