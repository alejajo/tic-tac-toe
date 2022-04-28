'''
Tic-tac-toe game utils.
'''


def create_empty_board():

    board = []
    for i in range(3):
        board.append([None] * 3)

    return board


def print_board(board):

    print('\n'.join([str(row) for row in board]))


def update_board(board, x, y,  player):
    board[x][y]=str (player) 
    pass


def check_for_winner(board):
    if board[1][0] and board[1][1] and board[1][2] or board[2][0] and board[2][1] and board[2][2] or board[0][0] and board[0][1] and board[0][2] :
        print("-----------------------------")
        print("-----------------------------")
        print("-----------------------------")
        print("    HAS GANADO EL JUEGO   ")
        print("-----------------------------")
        print("-----------------------------")
        print("-----------------------------")

    if board[0][1] and board[0][0] and board[0][2] or board[1][1] and board[1][0] and board[1][2] or board[2][1] and board[2][0] and board[2][2]:
        print("-----------------------------")
        print("-----------------------------")
        print("-----------------------------")
        print("    HAS GANADO EL JUEGO   ")
        print("-----------------------------")
        print("-----------------------------")
        print("-----------------------------")
    if board[2][2] and board[1][1] and board[0][0] or board[2][0] and board[1][1] and board[0][2]:
        print("-----------------------------")
        print("-----------------------------")
        print("-----------------------------")
        print("    HAS GANADO EL JUEGO   ")
        print("-----------------------------")
        print("-----------------------------")
        print("-----------------------------")
                
           
    



'''
Testing: 
'''

board = create_empty_board()
print_board(board)
x=int(input("Ingrese el numero en coordenada x:      ")) 
y=int(input("Ingrese el numero en coordenada y:      "))
player="O"

update_board(board,x,y,player)
print_board(board)

x=int(input("Ingrese el numero en coordenada x:      ")) 
y=int(input("Ingrese el numero en coordenada y:      "))
player="O"

update_board(board,x,y,player)
print_board(board)

x=int(input("Ingrese el numero en coordenada x:      ")) 
y=int(input("Ingrese el numero en coordenada y:      "))
player="O"

update_board(board,x,y,player)
print_board(board)

w=check_for_winner(board)
