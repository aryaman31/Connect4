#Connect 4
#To-Do list :-
#   - Make diagnal winning
#   - Make computer AI for single player mode
game = [[" "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "],      # 6 up , 7 left
        [" "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "],
       [" "," "," "," "," "," "," "]]

def draw():
    for line in game:
        k = ""
        for i in line:
            k = k + "[" + i + "]"
        print(k)
    k = ""
    for i in range(1,8):
        k = k + " " + str(i) + " "
    print(k)

def intro():
    print("Welcome to connect 4, Python Edition")
    print("Same rules as connect 4, but only in python")
    print("")
    print("This is the board you are going to play on")
    draw()
    print()
    print("You have to enter the row you want drop you peg in")
    print("There are two pegs : X , O")
    print("Have fun !")

def place(c,peg):
    rowNum = input("Enter your row number :\n")
    correctNums = ["1","2","3","4","5","6","7"]
    while rowNum not in correctNums:
        rowNum = input("Please enter a valid input:\n")

    temp = False
    rowNum = int(rowNum) - 1
    for i in range(5,-1,-1):
        if game[i][rowNum] == " ":
            game[i][rowNum] = peg
            temp = True
            break
    if temp == False:
        c = c -1
        print("This row is full, pick another row")
    return c

def arrayWinn(array,peg,win):
    for i in array:
        c = 0
        for j in i:
            if j == peg:
                c = c + 1
            else:
                c = 0

            if c == 4 :
                win = True
    return win

def winning(game,peg):
    win = False
    # Horizontal winning
    win = arrayWinn(game,peg,win)
    # Verticle winning
    c = 0
    for i in range(0,7):
        for j in range(0,6):
            if game[j][i] == peg:
                c = c + 1
            else :
                c = 0

            if c == 4:
                win = True

    win = diagnalWinning(game,peg,win)
    return win

def diagnalWinning(game,peg,win):
    comb = []
    for i in range(6):
        k = []
        a = 0
        for j in range(i+1):
            b = i - a
            k.append(game[b][j])
            a = a + 1
        comb.append(k)

    a = 6
    for i in range(6):
        k = []
        a = a - 1
        c = 6
        for j in range(i+1):
            b = a + j
            k.append(game[b][c])
            c = c - 1
        comb.append(k)

    # Other side
    a = 6
    for i in range(6):
        k = []
        a = a - 1
        for j in range(i+1):
            b = a + j
            k.append(game[b][j])
        comb.append(k)

    a = 7
    for i in range(6):
        k = []
        a = a - 1
        for j in range(i+1):
            c = a + j
            k.append(game[j][c])
        comb.append(k)
    
    win = arrayWinn(comb,peg,win)
    return win

def main():
    intro()
    play = False
    c = 0
    while play == False:
        draw()
        c = c + 1
        if c % 2 != 0:
            peg = "X"
        else:
            peg = "O"
        print(peg," Turn")
        c = place(c,peg)
        win = winning(game,peg)
        if win == True:
            draw()
            play = True
            print(peg,"WON !")
            break




main()

    
        
