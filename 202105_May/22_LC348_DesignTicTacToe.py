
class TicTacToe:
    def __init__(self, n) -> None:
        self.n = n
        self.rows = [0 for i in range(n)]
        self.cols = [0 for i in range(n)]
        self.diagonal = 0
        self.anti_diagonal = 0

    def move(self, row, col, player):
        current_player = 1 if player == 1 else -1
        
        self.rows[row] += current_player
        self.cols[col] += current_player

        if row == col:
            self.diagonal += current_player 
        
        if col == (self.n - row - 1):
            self.anti_diagonal += current_player
        
        if abs(self.rows[row]) == self.n or \
           abs(self.cols[col]) == self.n or \
           abs(self.diagonal) == self.n or \
           abs(self.anti_diagonal) == self.n:
            return player
        
        return 0

class TicTacToe_BruteForce:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.size = n
        self.matrix = [[0 for x in range(self.size)] for y in range(self.size)]
        

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.r
                1: Player 1 wins.
                2: Player 2 wins.
        """
        self.matrix[row][col] = player
        
        for index in range(self.size):
            

            r = index
            c = 0
            while self.matrix[r][c] == player and c < self.size:
                if c == self.size - 1:
                    return player
                c += 1
            c = index
            r = 0
            while self.matrix[r][c] == player and r < self.size:
                if r == self.size - 1:
                    return player
                r += 1

        i = 0
        while self.matrix[i][i] == player and i < self.size:
            if i == self.size - 1:
                return player
            i += 1

        i = self.size - 1 
        while self.matrix[i][i] == player and i >= 0:
            if i == 0:
                return player
            i -= 1
        return 0

# Your TicTacToe object will be instantiated and called as such:
obj = TicTacToe_BruteForce(3)
obj = TicTacToe(3)
output = []
for item in [
    [0, 0, 1], [0, 2, 2], [2, 2, 1], [1, 1, 2], [2, 0, 1], [1, 0, 2], [2, 1, 1]
]:
    row = item[0]
    col = item[1]
    player = item[2]
    output.append(obj.move(row,col,player))

# print(output)
assert output == [0, 0, 0, 0, 0, 0, 1], "Failed."

print('Success!')