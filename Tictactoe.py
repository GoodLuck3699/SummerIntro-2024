def printBoard(array):
    print(" ", array[0], "|", array[1], "|", array[2], " \n", end = "")
    print("--------------")
    print(" ", array[3], "|", array[4], "|", array[5], " \n", end = "")
    print("--------------")
    print(" ", array[6], "|", array[7], "|", array[8], " \n", end = "")

def win(array):
    if(array[0] == "X" and array[1] == "X" and array[2] == "X"):
        return 2
    elif(array[0] == "O" and array[1] == "O" and array[2] == "O"):
        return 1
    
    if(array[3] == "X" and array[4] == "X" and array[5] == "X"):
        return 2
    elif(array[3] == "O" and array[4] == "O" and array[5] == "O"):
        return 1
    
    if(array[6] == "X" and array[7] == "X" and array[8] == "X"):
        return 2
    elif(array[6] == "O" and array[7] == "O" and array[8] == "O"):
        return 1
    #Golom
    if(array[0] == "X" and array[3] == "X" and array[6] == "X"):
        return 2
    elif(array[0] == "O" and array[3] == "O" and array[6] == "O"):
        return 1
    
    if(array[1] == "X" and array[4] == "X" and array[7] == "X"):
        return 2
    elif(array[1] == "4" and array[1] == "O" and array[7] == "O"):
        return 1
    
    if(array[2] == "X" and array[4] == "X" and array[8] == "X"):
        return 2
    elif(array[2] == "O" and array[4] == "O" and array[8] == "O"):
        return 1
    #LOL

    if(array[0] == "X" and array[4] == "X" and array[8] == "X"):
        return 2
    elif(array[0] == "O" and array[4] == "O" and array[8] == "O"):
        return 1

    if(array[2] == "X" and array[4] == "X" and array[6] == "X"):
        return 2
    elif(array[2] == "O" and array[4] == "O" and array[6] == "O"):
        return 1
    
array = [" "] * 9
turn = 1
winner = 0

while turn < 9:

#Winner

    winner = win(array)
    if winner == 1:
        print( "Player", winner, " is the winner!")
        again = input("Would you like to play again? Y = Yes. Anything else is a no: ")
    elif winner == 2:
        print( "Player", winner, " is the winner!")
        again = input("Would you like to play again? Y = Yes. Anything else is a no: ")
    elif winner == 0:
        print("Som wrong with this prgm")

        if again == "Y":
            array = [" "] * 9
            turn = 1
            winner  = 0
            continue
        else:
            print("Okay! Have a great day!")
            break

#Game Play

    option = input("Pick a square (1 to 9): ").strip()
    if option.isdigit() != True:
        print("Invalid option.")
        continue

    option = int(option)

    if option > 9 or option < 1:
        print("Invalid option.")
        continue

    if array[option-1] != " ":
        print("Spot already filled. Pick a different one.")
        continue


    if turn % 2 == 1:
        array[option-1] = "X"
    else:
        array[option-1] = "O"
    turn += 1
    printBoard(array)

#Tie

    if turn >= 9:
        print("Tie")
        again = input("Would you like to play again? Y = Yes. Anything else is a no: ")
        if again == "Y":
            array = [" "] * 9
            turn = 1
            winner  = 0
            continue
        else:
            print("Have a nice day!")
            break