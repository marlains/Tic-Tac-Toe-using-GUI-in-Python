class BoardClass:
    """A simple class to store and handle information about BoardClass.

    Attributes:
        board (list): The game board
        move_index (dict): Dictionary with the move (1-9) as the item and the board index as the value
        user_one (str): Player One's user name
        user_two (str): Player Two's user name
        last_player (str): The user name of the last player to have a turn
        choice (str) : The player's symbol
        wins (int): The number of wins
        ties (int): The number of ties
        losses (int): The number of losses
    """
    
    def __init__(self, user_one: str = '', user_two: str = '', last_player: str = '', choice: str = "", move: str = "", games: int = 1, wins: int = 0, ties: int = 0, losses: int = 0):
        """Make a BoardClass.

        Args:
            board (list): The game board
            move_index (dict): Dictionary with the move (1-9) as the item and the board index as the value
            user_one (str): Player One's user name
            user_two (str): Player Two's user name
            last_player (str): The user name of the last player to have a turn
            button (str): Which button the player pressed on the Tic Tac Toe board
            choice (str) : The player's symbol
            games (int): The number of games played
            wins (int): The number of wins
            ties (int): The number of ties
            losses (int): The number of losses
        """

        self.setBoard()
        self.setMoveIndex()
        self.user_one = user_one
        self.user_two = user_two
        self.last_player = last_player
        self.choice = choice
        self.move = move
        self.games = games
        self.wins = wins
        self.ties = ties
        self.losses = losses

    def setBoard(self) -> None:
        """This is my Tic Tac Toe board. A big list that contains three additional lists which represent the rows.
        Each row contains three empty strings which represent each square.

        Args:
            board: The game board
        """
        
        self.board = [['','',''],
                     ['','',''],
                     ['','','']]
        
    def setMoveIndex(self) -> None:
        """Dictionary that tells us which board cell the player wants to place their move by having they keys be 1-9"""
        self.move_index = {1: (0, 0), 2: (0, 1), 3: (0, 2),
                           4: (1, 0), 5: (1, 1), 6: (1, 2),
                           7: (2, 0), 8: (2, 1), 9: (2, 2)}
        
    def updateGamesPlayed(self):
        """Increment the number of games played by 1."""
        
        #if self.boardIsFull() or self.isWinner():
        self.games += 1

    def resetGameBoard(self) -> list:
        """Loop over all the indexes of self.board and clearing each one"""

        for row in range(len(self.board)):
            for square in range(len(self.board[row])):
                self.board[row][square] = ''
        self.updateGamesPlayed()
        return self.board

    """def updateGameBoard(self, move, choice):
        
        position = self.move_index[int(move)]
        self.board[position[0]][position[1]] = choice
    """

    def updateGameBoard(self, move, choice):
        """uses row and column indexes to update the appropriate cell in self.board."""
        
        self.board[int(move[0])][int(move[1])] = choice

    def isWinner(self):
        """index through all possible winning combos + increment the number of wins"""

        #player 1 is the winner
        if (self.board[0][0] == 'X') and (self.board[0][1] == 'X') and (self.board[0][2] == 'X'):
            if self.choice == 'X':
                self.wins += 1
            elif self.choice == 'O':
                self.losses += 1
            return True
        elif (self.board[1][0] == 'X') and (self.board[1][1] == 'X') and (self.board[1][2] == 'X'):
            if self.choice == 'X':
                self.wins += 1
            elif self.choice == 'O':
                self.losses += 1
            return True
        elif (self.board[2][0] == 'X') and (self.board[2][1] == 'X') and (self.board[2][2] == 'X'):
            if self.choice == 'X':
                self.wins += 1
            elif self.choice == 'O':
                self.losses += 1
            return True
        elif (self.board[0][0] == 'X') and (self.board[1][0] == 'X') and (self.board[2][0] == 'X'):
            if self.choice == 'X':
                self.wins += 1
            elif self.choice == 'O':
                self.losses += 1
            return True
        elif (self.board[0][1] == 'X') and (self.board[1][1] == 'X') and (self.board[2][1] == 'X'):
            if self.choice == 'X':
                self.wins += 1
            elif self.choice == 'O':
                self.losses += 1
            return True
        elif (self.board[0][2] == 'X') and (self.board[1][2] == 'X') and (self.board[2][2] == 'X'):
            if self.choice == 'X':
                self.wins += 1
            elif self.choice == 'O':
                self.losses += 1
            return True
        elif (self.board[0][0] == 'X') and (self.board[1][1] == 'X') and (self.board[2][2] == 'X'):
            if self.choice == 'X':
                self.wins += 1
            elif self.choice == 'O':
                self.losses += 1
            return True
        elif (self.board[0][2] == 'X') and (self.board[1][1] == 'X') and (self.board[2][0] == 'X'):
            if self.choice == 'X':
                self.wins += 1
            elif self.choice == 'O':
                self.losses += 1
            return True
        #player 2 is the winner    
        elif (self.board[0][0] == 'O') and (self.board[0][1] == 'O') and (self.board[0][2] == 'O'):
            if self.choice == 'O':
                self.wins += 1
            elif self.choice == 'X':
                self.losses += 1
            return True
        elif (self.board[1][0] == 'O') and (self.board[1][1] == 'O') and (self.board[1][2] == 'O'):
            if self.choice == 'O':
                self.wins += 1
            elif self.choice == 'X':
                self.losses += 1
            return True
        elif (self.board[2][0] == 'O') and (self.board[2][1] == 'O') and (self.board[2][2] == 'O'):
            if self.choice == 'O':
                self.wins += 1
            elif self.choice == 'X':
                self.losses += 1
            return True
        elif (self.board[0][0] == 'O') and (self.board[1][0] == 'O') and (self.board[2][0] == 'O'):
            if self.choice == 'O':
                self.wins += 1
            elif self.choice == 'X':
                self.losses += 1
            return True
        elif (self.board[0][1] == 'O') and (self.board[1][1] == 'O') and (self.board[2][1] == 'O'):
            if self.choice == 'O':
                self.wins += 1
            elif self.choice == 'X':
                self.losses += 1
            return True
        elif (self.board[0][2] == 'O') and (self.board[1][2] == 'O') and (self.board[2][2] == 'O'):
            if self.choice == 'O':
                self.wins += 1
            elif self.choice == 'X':
                self.losses += 1
            return True
        elif (self.board[0][0] == 'O') and (self.board[1][1] == 'O') and (self.board[2][2] == 'O'):
            if self.choice == 'O':
                self.wins += 1
            elif self.choice == 'X':
                self.losses += 1
            return True
        elif (self.board[0][2] == 'O') and (self.board[1][1] == 'O') and (self.board[2][0] == 'O'):
            if self.choice == 'O':
                self.wins += 1
            elif self.choice == 'X':
                self.losses += 1
            return True
        
    def boardIsFull(self) -> True:
        """Check if there are any empty spaces on the board. Iterate through self.board.
        use any() or all()
        """
        
        if all(self.board[0]) and all(self.board[1]) and all(self.board[2]):
            self.ties += 1
            return True

    def computeStats(self):
        print(self.user_one)
        print(self.user_two)
        print(self.games)
        print(self.wins)
        print(self.losses)
        print(self.ties)
