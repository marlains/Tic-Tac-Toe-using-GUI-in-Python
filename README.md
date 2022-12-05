# Tic-Tac-Toe-using-GUI-in-Python

This project uses Python to create a basic Tic Tac Toe game. This is a 2-player game that uses sockets to communicate and Tkinter as the GUI.

I used Python 3.8 and programmed in IDLE. 

Python libraries used/imported: socket, tkinter, tkinter.messagebox

gameboard.py: This is a module that contain a class which holds the logic of the game (back-end). player1.py and player2.py will have their own objects of this class in their class/module.
              The BoardClass() class initializes the player names, number of games, and number of games won, lost, and tied. In addition, it updates the Tic Tac Toe board on the back-end,
              checks for winners, checks if the board is full, and increments the number of games played. Each method/function in the class has docstrings explaining its function.

player1.py: This is a module that contains the client class. Player 1 is the 'X', has the first turn in every game, and decides if they want to play again or of they want to quit the game.
            Contains the GUI and uses Boardclass() object for the logic of the game. 

player2.py: This is a module that contians the server class. Player 2 is the 'O', is the first receiver in every game, and follows the decisions of player 1.
            Contains the GUI and uses Boardclass() object for the logic of the game. 
