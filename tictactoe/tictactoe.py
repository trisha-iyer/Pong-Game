
def sum(a, b, c):
    return a + b + c

def printBoard(xstate, ostate) :
    zero = 'X' if xstate[0] else ('O' if ostate[0] else 0)
    one = 'X' if xstate[1] else ('O' if ostate[1] else 1)
    two = 'X' if xstate[2] else ('O' if ostate[2] else 2)
    three = 'X' if xstate[3] else ('O' if ostate[3] else 3)
    four = 'X' if xstate[4] else ('O' if ostate[4] else 4)
    five = 'X' if xstate[5] else ('O' if ostate[5] else 5)
    six = 'X' if xstate[6] else ('O' if ostate[6] else 6)
    seven = 'X' if xstate[7] else ('O' if ostate[7] else 7)
    eight = 'X' if xstate[8] else ('O' if ostate[8] else 8)

    print(f"{zero} | {one} | {two} ")
    print(f"--|---|---")
    print(f"{three} | {four} | {five} ")
    print(f"--|---|---")
    print(f"{six} | {seven} | {eight} ")

def checkWin(xstate, ostate) :
    wins = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]
    for win in wins :
        if(sum(xstate[win[0]], xstate[win[1]], xstate[win[2]]) == 3):
            print("X won !")
            return 1

        if(sum(ostate[win[0]], ostate[win[1]], ostate[win[2]]) == 3):
            print("O won !")
            return 0 
        
        
    return -1
    

if __name__ == "__main__" :
    xstate = [0,0,0,0,0,0,0,0,0]
    ostate = [0,0,0,0,0,0,0,0,0]
    turn = 1 # 1 for X and 0 for O
    print("welcome to tic tac toe")
    while True:
        printBoard(xstate, ostate)
        if turn == 1:
            print("X's chance")
        else:
            print("O's chance")

        value = int(input("Please enter a position: "))
        if turn == 1:
            xstate[value] = 1
        else:
            ostate[value] = 1

        
        '''if(turn == 1):
            print("X's chance")
            value = int(input("please enter a position: "))
            xstate[value] = 1
        else :
            print("O's chance")
            value = int(input("please enter a position: "))
            ostate[value] = 1'''

        cwin = checkWin(xstate, ostate)
        if cwin != -1 :
            print("match over")
            break

        # Check for a draw after every move
        if all(xstate[i] or ostate[i] for i in range(9)):
            print("It's a draw!")
            break

        
        turn = 1 - turn


