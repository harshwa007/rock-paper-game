import random as rd
import time as tm


def time_sleep():
    tm.sleep(2)


game=['rock','paper','scissor']
player1=input("enter your choice\t")
if player1 in game:
    print("your choice is ",player1)

else:
    print("invalid choice")         #Game result: you loss!!
time_sleep()                        #Game result: you win!!
while True:
    pc_player1=rd.choice(game)
    print(pc_player1)
    if pc_player1==player1:
        print("Game Result : Tie!")
        break
    elif player1==game[0]:
        if pc_player1==game[1]:
            print("Game result: you loss!!")
            break
        if pc_player1==game[2]:
            print("Game result: you win!!")
            break
    elif player1==game[1]:
        if pc_player1==game[0]:
            print("Game result: you loss!!")
            break
        if pc_player1==game[2]:
            print("Game result: you win!!")
            break
    else:
        if pc_player1==game[0]:
            print("Game result: you loss!!")
            break
        if pc_player1==game[1]:
            print("Game result: you win!!")
            break

