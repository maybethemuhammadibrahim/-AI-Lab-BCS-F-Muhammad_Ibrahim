def isSafePlacement(placedQueens, currentRow, testCol):
    for pastRow, pastCol in enumerate(placedQueens):
        if pastCol == testCol:
            return False
        # check diagonals using absolute difference of rows and columns
        if abs(pastRow - currentRow) == abs(pastCol - testCol):
            return False
    return True

def solveNQueens(boardSize, currentRow=0, placedQueens=None):
    if placedQueens is None:
        placedQueens = []

    if currentRow == boardSize:
        return placedQueens

    for testCol in range(boardSize):
        if isSafePlacement(placedQueens, currentRow, testCol):
            placedQueens.append(testCol)
            
            validBoard = solveNQueens(boardSize, currentRow + 1, placedQueens)
            if validBoard:
                return validBoard
                
            placedQueens.pop()

    return None

def printBoard(queenPositions):
    boardSize = len(queenPositions)
    print("--- task 7 n-queens variation ---")
    for row in range(boardSize):
        rowStr = ["_"] * boardSize
        rowStr[queenPositions[row]] = "Q"
        print(" ".join(rowStr))

if __name__ == "__main__":
    finalBoard = solveNQueens(4)
    if finalBoard:
        printBoard(finalBoard)
    else:
        print("no solution found")