# #Tic Tac Toe

board = [" " for x in range(9)]

def print_board():
    row1 = "| {} | {} | {} |".format(board[0], board[1], board[2])
    row2 = "| {} | {} | {} |".format(board[3], board[4], board[5])
    row3 = "| {} | {} | {} |".format(board[6], board[7], board[8])


    print()
    print(row1)
    print(row2)
    print(row3)
    print()

def player_move(icon,name):
    # if icon == "X":
    #     number = 1
    # elif icon == "O":
    #     number = 2
    print(f"{name},your Turn!")
    choice = int(input("Enter your move (1-9): ").strip())
    if board[choice - 1] == " ":
        board[choice - 1] = icon
    else:
        print()
        print("That space is already taken!")

def is_victory(icon):
    win_condition=[(0,1,2),(3,4,5),(6,7,8),(0,4,8),(2,4,6),(0,3,6),(1,4,7),(2,5,8)]
    for condition in win_condition:
        # if condition[0]==board[0] and condition[1]==board[1] and condition[2]==board[2]:
        if board[condition[0]]==board[condition[1]]==board[condition[2]]==icon:
            return True
    return False
    # if (board[0] == icon and board[1] == icon and board[2] == icon) or \
    #    (board[3] == icon and board[4] == icon and board[5] == icon) or \
    #    (board[6] == icon and board[7] == icon and board[8] == icon) or \
    #    (board[0] == icon and board[3] == icon and board[6] == icon) or \
    #    (board[1] == icon and board[4] == icon and board[7] == icon) or \
    #    (board[2] == icon and board[5] == icon and board[8] == icon) or \
    #    (board[0] == icon and board[4] == icon and board[8] == icon) or \
    #    (board[2] == icon and board[4] == icon and board[6] == icon):
        # return True
    # else:
    #     return False



def is_draw():
    if " " not in board:
        return True
    else:
        return False

def main():
    playe_1=input("Player 1, Enter Your Name:").title()
    player1_icon=input(f"{playe_1} Enter X or O").upper()
    playe_2=input("Player 2, Enter your name:").title()
    player2_icon="O"
    if playe_1=="O":
        player2_icon="X"
    print(f"{playe_1} you are {player1_icon}\n{playe_2} you are {player2_icon}")
    while True:
        print_board()
        player_move(player1_icon,playe_1)
        print_board()
        if is_victory(player1_icon):
            print(f"{playe_1} wins! Congratulations!")
            break
        elif is_draw():
            print("It's a draw!")
            break
        player_move(player2_icon,playe_2)
        if is_victory(player2_icon):
            print_board()
            print(f"{playe_2} wins! Congratulations!")
            break
        elif is_draw():
            print("It's a draw!")
            break
if __name__=='__main__':
    main()









































# board=[" " for i in range(9)]
# def print_board():
#     row1=f" {board[0]} | {board[1]} | {board[2]} \n___________"
#     row2=f" {board[3]} | {board[4]} | {board[5]} \n___________"
#     row3=f" {board[6]} | {board[7]} | {board[8]} "
#     print("\n".join([row1,row2,row3]))

# def player_moves(icon):
#     if icon == "X":
#         number=1
#     elif icon=="O":
#         number=2
#     print(f"Your turn player {number}")
#     chosse=int(input("Enter box number 1-9:").strip())
#     if board[chosse-1]==" ":
#         board[chosse-1]== icon
#     else:
#         print("Already filled")

# def is_vict(icon):
#     win_condition=[(0,1,2),(3,4,5),(6,7,8),(0,4,8),(2,4,6),(0,3,6),(1,4,7),(2,5,8)]
#     for condition in win_condition:
#         if board[condition[0]]==board[condition[1]]==board[condition[2]]==icon:
#             return True
#     return False

# def draw_match():
#     return " " not in board

# while True:
#     print_board()
#     player_moves("X")
#     if is_vict("X"):
#         print("X Won the Game")
#         break
#     elif draw_match():
#         print("Draw match!!!")
#         break
#     print_board()
#     player_moves("O")
#     if is_vict("O"):
#         print("O Won the Game")
#         break
#     elif draw_match():
#         print("Draw match!!!")
#         break














































# # print("\t\t|\tX\t|\tX\t\n\n----------------------------------------------------------------")
# # print("\tX\t|\tX\t|\tX\t\n\n----------------------------------------------------------------")
# # print("\tX\t|\tX\t|\tX\t\n\n")

# import random as r


# ttt_list=[f"\t{1}\t|\t{2}\t|\t{3}\t\n\t\t|\t\t|\t\t\n-----------------------------------------------------",
#         f"\t{4}\t|\t{5}\t|\t{6}\t\n\t\t|\t\t|\t\t\n-----------------------------------------------------",
#         f"\t{7}\t|\t{8}\t|\t{9}\t\n\t\t|\t\t|\t\t\n"]

# game=[]
# for box in ttt_list:
#     print(box)


# user_input=input("Chosse X or O:").upper()
# computer="O"
# if user_input=="O":
#     computer="X"

# k=0
# user_choices=[]
# computer_choices=[]
# while k<4:
    
#     chosse_place=int(input("Enter the box number:"))
#     computer_chosse=r.randint(1,9)

#     if chosse_place not in user_choices and chosse_place not in computer_choices:
#         user_choices.append(chosse_place)
#     else:
#         chosse_place=int(input("The box num is already filled, enter another box num:"))
#         user_choices.append(chosse_place)



#     if computer_chosse not in user_choices and computer_chosse not in computer_choices:
#         computer_choices.append(computer_chosse)
        
#     else:
#         computer_chosse=r.randint(1,9)
#         computer_choices.append(computer_chosse)


    
#     print(f"Computer Chosee:{computer_chosse}")
    
    


    

#     # for i in game:
#     #     print(i) 
#     # while True:
#     #     for i in ttt_list:
#     #         for j in i:
#     #             print(j)
#     #     break
#     for i in ttt_list:
#         for j in i:

#             # print(f"element:{j} indx:{i.index(j)}")
#             if j==str(chosse_place):
#                 # print(f"element:{j} indx:{i.index(j)}")
                
#                 i=i.replace(j,user_input)
#             if j==str(computer_chosse):
#                 # print(f"element:{j} indx:{i.index(j)}")
#                 i=i.replace(j,computer)
#                 # print(i)
#         # print(i)
#         game.append(i)
#         # print(i)
#     k+=1

# # for i in game:
# #     for j in i:
# #         print(j)
# #     print("\n"*5)
# prob=0
# def see(l):
#     for i in l:
#         if i in user_choices:
#             prob+=1
# see([3,5,7])
# see([1,2,3])
# see([4,5,6])
# see([7,8,9])
# see([1,5,9])

# print(prob)
# print(user_choices,computer_choices)