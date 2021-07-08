from flask.scaffold import F


class Puzzle:
    """
    A class that will hold logic for the sudoku board, including the numbers, their positions and board methods.
    """

    def __init__(self):
        self.grid = []

        #The way the grid is formated in the page is of the form grid[y][x], where the y value is the rows.

        # fill in the board to test the html.
        for i in range(9):
            self.grid.append([" ", " ", " ", " ", " ", " ", " ", " ", " "])

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

        for i in range(9):
            if self.__containsDuplicates(self.grid[i]):
                return False
        
        #add more logic for the other axis

        return True




    @staticmethod
    def __containsDuplicates(aList):
        for i in range(len(aList)):
            if aList[i] in aList[i+1:]:
                return True
        return False


if __name__ == "__main__":
    sudoku = Puzzle()
    # print(sudoku.__containsDuplicates([1, 2, 3, 4, 5, 6, 7, 8, 9]) == False)
    # print(sudoku.__containsDuplicates([1, 2, 3, 2, 4, 5, 6, 8, 9]) == True)
    

