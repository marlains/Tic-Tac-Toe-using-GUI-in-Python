from gameboard import BoardClass
import socket
import tkinter as tk
import tkinter.font as font
from tkinter import messagebox

#THIS IS THE SERVER/MACHINE
class PlayerTwo:
    
    """A simple class to store and handle information about PlayerTwo."""
    
    def __init__(self):
        """Make PlayerTwo.

        Args:
        boardclass (str): Object of BoardClass
        """
      
        #intializing my gameboard class variable
        self.playerTwoBoard = BoardClass(games = 1, wins = 0, ties = 0, losses = 0)

        #empty list
        self.buttonList = []

        #call my method to create my canvas and add my widgets
        self.canvasSetup()
        self.initTKVariables()
        self.setHost()
        self.setPort()
        self.createUserName()
        self.playerTurn()
        self.createBoardButtons()
        self.createSubmitButton()
        self.runUI()
 
    def connectsocket(self):
        """create socket object for my server, bind my host and port number together,
        allow my serverSocket to listen."""
        
        self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.serverSocket.bind((str(self.host.get()), int(self.port.get())))
        self.serverSocket.listen(1)

        #while True:
        clientSocket, clientAddress = self.serverSocket.accept()
        self.clientSocket = clientSocket
        #print("Client connected from: ", clientAddress)
        self.user_one = self.clientSocket.recv(1024).decode()
        self.clientSocket.send(str(self.user_two.get()).encode())

    def firstReceive(self):
        #prepare to receive the first move from PlayerOne
        self.turnLabel.configure(text="Waiting for the other player to make a move.")
        self.master.update()
        move = self.clientSocket.recv(1024).decode()
        #update the PlayerTwo board to reflect the move from PlayerOne
        self.playerTwoBoard.updateGameBoard(move, 'X')
        rowReceive = int(move[0])
        colReceive = int(move[1])
        #finding button
        button_tuple = (rowReceive, colReceive)
        position = self.buttonIndex(button_tuple)
        #insert 'X' on Tic Tac Toe board and disable button
        position.configure(text="X", state="disabled")
        self.master.update()
        self.turnLabel.configure(text="Your turn, make a move.")
        self.master.update()

    def initTKVariables(self):
        """A method that initializes the tk variables."""
        
        #set the host of Player 2
        self.host = tk.StringVar()
        #set the port of Player 2
        self.port = tk.StringVar()
        #set Player 2 user name
        self.user_two = tk.StringVar()

    def canvasSetup(self):
        """A method that sets up and initilizes the class canvas."""
        
        self.master  = tk.Tk()
        #sets the window title
        self.master.title("Tic Tac Toe - Player 2")
        #sets the default size of the window
        self.master.geometry('390x530')
        #set the background color of the window
        self.master.configure(background='white')
        #setting the x(horizontal) and y (vertical) to not be resizable.
        self.master.resizable(0,0)

    def createUserName(self):
        """A method that creates a label and entry field for the PlayerTwo user."""
        
        self.userNameLabel = tk.Label(self.master, text = "Username:")
        self.userNameLabel.grid(row = 0, column = 0, sticky = 'W', pady = 1)
        self.userNameEntry = tk.Entry(self.master, textvariable=self.user_two)
        self.userNameEntry.grid(column=1, columnspan=2,row=0)

    def setHost(self):
        """ Set the host of Player 2."""
        
        self.hostLabel = tk.Label(self.master, text = "Host:")
        self.hostLabel.grid(row = 1, column = 0, sticky = 'W', pady = 1)
        self.hostEntry = tk.Entry(self.master, textvariable=self.host)
        self.hostEntry.grid(column=1, columnspan=2,row=1)

    def setPort(self):
        """ Set the port of Player 2."""
        
        self.portLabel = tk.Label(self.master, text = "Port:")
        self.portLabel.grid(row = 2, column = 0, sticky = 'W', pady = 1)
        self.hostEntry = tk.Entry(self.master, textvariable=self.port)
        self.hostEntry.grid(column=1, columnspan=2,row=2)

    def createSubmitButton(self):
        """A method that creates a submit button, which is used after PlayerTwo has entered their username, host, and port.
            Before this button is pressed, the board buttons are diabled. After it's pressed, the board buttons are enabled.
        """
        
        self.submission = tk.Button(self.master,text="Submit",command=self.submitButton)
        self.submission.grid(row=4,column=2)

    def submitButton(self):
        """Connect my players (which also puts my buttons on the window)."""

        #self.host.get()
        #self.port.get()
        #self.user_two.get()
        self.connectsocket()
        #self.createBoardButtons()
        self.firstReceive()

    def playerTurn(self):
        """Creating a label that will display who's turn it is."""
        
        self.turnLabel = tk.Label(self.master, text = "Enter information to connect.")
        self.turnLabel.grid(row = 5, column = 0, columnspan = 3)

    def createBoardButtons(self):
        """Nine buttons for each square of the Tic Tac Toe board."""

        self.buttonList.append(tk.Button(self.master,text="",height=4,width=8,bg="black",font="Times 19 bold",state='normal',command=lambda: self.buttonClick(7,0)))
        self.buttonList[0].grid(row=7,column=0)
        self.buttonList.append(tk.Button(self.master,text="",height=4,width=8,bg="black",font="Times 19 bold",state='normal',command=lambda: self.buttonClick(7,1)))
        self.buttonList[1].grid(row=7,column=1)
        self.buttonList.append(tk.Button(self.master,text="",height=4,width=8,bg="black",font="Times 19 bold",state='normal',command=lambda: self.buttonClick(7,2)))
        self.buttonList[2].grid(row=7,column=2)
        self.buttonList.append(tk.Button(self.master,text="",height=4,width=8,bg="black",font="Times 19 bold",state='normal',command=lambda: self.buttonClick(8,0)))
        self.buttonList[3].grid(row=8,column=0)
        self.buttonList.append(tk.Button(self.master,text="",height=4,width=8,bg="black",font="Times 19 bold",state='normal',command=lambda: self.buttonClick(8,1)))
        self.buttonList[4].grid(row=8,column=1)
        self.buttonList.append(tk.Button(self.master,text="",height=4,width=8,bg="black",font="Times 19 bold",state='normal',command=lambda: self.buttonClick(8,2)))
        self.buttonList[5].grid(row=8,column=2)
        self.buttonList.append(tk.Button(self.master,text="",height=4,width=8,bg="black",font="Times 19 bold",state='normal',command=lambda: self.buttonClick(9,0)))
        self.buttonList[6].grid(row=9,column=0)
        self.buttonList.append(tk.Button(self.master,text="",height=4,width=8,bg="black",font="Times 19 bold",state='normal',command=lambda: self.buttonClick(9,1)))
        self.buttonList[7].grid(row=9,column=1)
        self.buttonList.append(tk.Button(self.master,text="",height=4,width=8,bg="black",font="Times 19 bold",state='normal',command=lambda: self.buttonClick(9,2)))
        self.buttonList[8].grid(row=9,column=2)

    def buttonIndex(self, button_tuple):
        self.button_dict = {(0, 0): self.buttonList[0], (0, 1): self.buttonList[1], (0, 2): self.buttonList[2],
                            (1, 0): self.buttonList[3], (1, 1): self.buttonList[4], (1, 2): self.buttonList[5],
                            (2, 0): self.buttonList[6], (2, 1): self.buttonList[7], (2, 2): self.buttonList[8]}
        return self.button_dict[button_tuple]
      
    def buttonClick(self, row, col):
        """Handles the command for self.button1 of the Tic Tac Toe board.
            When a button is clicked, 'X' is written and the button is connected to self.board in Boardclass()."""

        button_index = (f'{row-7}{col}')
        #update game baord
        self.playerTwoBoard.updateGameBoard(button_index, 'O')
        #finding button
        button_tuple = (int(button_index[0]), int(button_index[1]))
        position = self.buttonIndex(button_tuple)
        #position = self.button_dict[button_tuple]
        #insert 'O' on Tic Tac Toe board and disable button
        position.configure(text="O", state="disabled")
        self.master.update()
        #send move.
        self.clientSocket.send(button_index.encode())
        #check if there's a winner or if board is full
        if self.playerTwoBoard.isWinner() or self.playerTwoBoard.boardIsFull():
            self.playerTwoBoard.choice = 'O'
            self.playAgain()
        else:
            #call the receive function
            self.buttonReceive()

    def buttonReceive(self):
        #prepare to receive a move
        self.turnLabel.configure(text="Waiting for the other player to make a move.")
        self.master.update()
        move = self.clientSocket.recv(1024).decode()
        #update the PlayerTwo board to reflect the move from PlayerOne
        self.playerTwoBoard.updateGameBoard(move, 'X')
        rowReceive = int(move[0])
        colReceive = int(move[1])
        #finding button
        button_tuple = (rowReceive, colReceive)
        position = self.buttonIndex(button_tuple)
        #insert 'X' on Tic Tac Toe board and disable button
        position.configure(text="X", state="disabled")
        self.master.update()
        #check is there is a winner before making a move
        #check if the board is full before making a move
        self.playerTwoBoard.choice = 'O'
        self.playAgain()
        self.turnLabel.configure(text="Your turn, make a move.")
        self.master.update()

    def playAgain(self):
        """If the game is already won or the board is full,
            - wait to receive move from PlayerOne
                - if yes, send a message to PlayerTwo to let them know that a new game will start and reset PlayerOne board
                - if no, send a goodbye message to PlayerTwo and display the game statistics
        """
        
        if self.playerTwoBoard.isWinner() or self.playerTwoBoard.boardIsFull():
            #if 'yes' button is pressed, send that info to player2 and reset the board
            self.playAgainPopUp = self.clientSocket.recv(1024).decode()
            if self.playAgainPopUp == 'yes':
                #reset self.board and UI buttons
                self.playerTwoBoard.resetGameBoard()
                for i in range(9):
                    self.buttonList[i].configure(text="", state="normal")
                    self.master.update()
                self.firstReceive()
            elif self.playAgainPopUp == 'no':
                self.gameOverPopUp = tk.messagebox.showinfo("Game Stats", self.EndGameStats())
                self.master.destroy()

    def EndGameStats(self):
        stats = 'Your username: ' + self.user_two.get()
        stats += '\nOpponent\'s username: ' + self.user_one
        stats += '\nNumber of games played: ' + str(self.playerTwoBoard.games)
        stats += '\nNumber of games won: ' + str(int(self.playerTwoBoard.games) - int(self.playerTwoBoard.losses))
        stats += '\nNumber of games lost: ' + str(self.playerTwoBoard.losses)
        stats += '\nNumber of games tied: ' + str(self.playerTwoBoard.ties)
        return stats
        
    def runUI(self):
      """A method that starts the UI - event handler."""
      
      self.master.mainloop()
      

if __name__ == '__main__':
    player_two = PlayerTwo()
