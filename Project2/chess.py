#Defining a chess_board
def chess_board(self):
    chess_board = [[1] * 8 for i in range(8)]

#Converting index value of array from integer to alphabet
chess_map_from_index_to_alphabet = {
   0: "a",
   1: "b",
   2: "c",
   3: "d",
   4: "e",
   5: "f",
   6: "g",
   7: "h"
}

#Converting index value of array from alphabet to integer
chess_map_from_alphabet_to_index = {
   "a" : 0,
   "b" : 1,
   "c" : 2,
   "d" : 3,
   "e" : 4,
   "f" : 5,
   "g" : 6,
   "h" : 7
}

#All possible moves for Knight
def Get_Knight_Moves(pos, chess_board,user_positions):
    """ A function that returns the all possible moves
        of a knight stood on a given position
    """
    row,column = list(pos.strip().lower())
    row = int(row)-1
    column = chess_map_from_alphabet_to_index[column]
    i,j = row,column
    feasible_moves = []
    #RUp and Right move
    try:
        if i+1 < 0 or j-2 < 0:
            pass
        else:
            if ["".join([str(i+1),chess_map_from_index_to_alphabet[j-2]])] not in user_positions:
                feasible_moves.append([i + 1, j - 2])
    except:
        pass
    #Right and Up move
    try:
        if i+2 < 0 or j-1 < 0:
            pass
        else:
            if ["".join([str(i+2),chess_map_from_index_to_alphabet[j-1]])] not in user_positions:
                feasible_moves.append([i + 2, j - 1])
    except Exception as e:
        print(e)
        pass
    #Right and Down Move
    try:
        if i+2 < 0 or j+1 < 0:
            pass
        else:
            if ["".join([str(i+2),chess_map_from_index_to_alphabet[j+1]])] not in user_positions:
                feasible_moves.append([i + 2, j + 1])
    except Exception as e:
        print(e)
        pass
    #Down And Right Move
    try:
        if i+1 < 0 or j+2 < 0:
            pass
        else:
            if ["".join([str(i+1),chess_map_from_index_to_alphabet[j+2]])] not in user_positions:
                feasible_moves.append([i + 1, j + 2])
        #print(feasible_moves)
    except:
        pass
    #Down And Left Move
    try:
        if i-1 < 0 or j+2 < 0:
            pass
        else:
            if ["".join([str(i-1),chess_map_from_index_to_alphabet[j+2]])] not in user_positions:
                feasible_moves.append([i - 1, j + 2])
        #print(feasible_moves)
    except:
        pass
    #Left and Down Move
    try:
        if i-2 < 0 or j+1 < 0:
            pass
        else:
            if ["".join([str(i-2),chess_map_from_index_to_alphabet[j+1]])] not in user_positions:
                feasible_moves.append([i - 2, j + 1])
        #print(feasible_moves)
    except:
        pass
    #left and Up Move
    try:
        if i-2 < 0 or j-1 < 0:
            pass
        else:
            if ["".join([str(i-2),chess_map_from_index_to_alphabet[j-1]])] not in user_positions:
                feasible_moves.append([i - 2, j - 1])
        #print(feasible_moves)
    except:
        pass
    #up and Left Move
    try:
        if i-1 < 0 or j-2 < 0:
            pass
        else:
            if ["".join([str(i-1),chess_map_from_index_to_alphabet[j-2]])] not in user_positions:
                feasible_moves.append([i - 1, j - 2])
        #print(feasible_moves)
    except:
        pass

    # Now let us filter all negative values
    temporary = [i for i in feasible_moves if i[0] >=0 and i[1] >=0]
    feasible_moves = ["".join([str(i[0] + 1),chess_map_from_index_to_alphabet[i[1]]]) for i in temporary]
    for x in user_positions:
        if x in feasible_moves:
            feasible_moves.remove(x)
    feasible_moves.sort()
    p = len(feasible_moves)
    for a in range (p):
        print (str(a+1)+"-" +str(feasible_moves[a]))
    print(feasible_moves)
    return feasible_moves

#Defining all possible moves of Rook
def Get_Rook_Moves(pos, chess_board, user_positions):
    row, column = list(pos.strip().lower())
    row = int(row) - 1
    column = chess_map_from_alphabet_to_index[column]
    i,j = row, column
    currposrow = i + 1;
    currposcolumn = j + 1;
    feasible_moves = []

    # Compute the moves in columns
    for j in range(8):
        if j != column and ["".join([str(row + 1),chess_map_from_index_to_alphabet[j]])] in user_positions:
            pass
        if j != column and ["".join([str(row + 1),chess_map_from_index_to_alphabet[j]])] not in user_positions:
            feasible_moves.append((row, j))
    # Compute the moves in row
    for i in range(8):
        if i != row and ["".join([str(i + 1),chess_map_from_index_to_alphabet[column]])] in user_positions:
            pass
        if i != row and ["".join([str(i + 1),chess_map_from_index_to_alphabet[column]])] not in user_positions:
            feasible_moves.append((i, column))
    feasible_moves = ["".join([str(i[0] + 1),chess_map_from_index_to_alphabet[i[1]]]) for i in feasible_moves]
    #print (feasible_moves)
    for x in user_positions:
        yourrow, yourcolumn = list(x.strip().lower())
        yourcolumn = chess_map_from_alphabet_to_index[yourcolumn] + 1;
        if x in feasible_moves:
            if currposrow == int(yourrow)  and currposcolumn < yourcolumn:
                for value in range(yourcolumn,9):
                    removing = ["".join([str(currposrow),chess_map_from_index_to_alphabet[value - 1]])]
                    feasible_moves = list(set(feasible_moves) - set(removing))
            if currposrow == int(yourrow)  and currposcolumn > yourcolumn:
                for value in range(1,yourcolumn + 1):
                    removing = ["".join([str(currposrow),chess_map_from_index_to_alphabet[value - 1]])]
                    feasible_moves = list(set(feasible_moves) - set(removing))
            if currposcolumn == int(yourcolumn)  and currposrow < int(yourrow):
                for value in range(int(yourrow),9):
                    removing = ["".join([str(value),chess_map_from_index_to_alphabet[currposcolumn-1]])]
                    feasible_moves = list(set(feasible_moves) - set(removing))
            if currposcolumn == int(yourcolumn)  and currposrow > int(yourrow):
                for value in range(1,int(yourrow) + 1):
                    removing = ["".join([str(value),chess_map_from_index_to_alphabet[currposcolumn-1]])]
                    feasible_moves = list(set(feasible_moves) - set(removing))
    feasible_moves.sort()
    p = len(feasible_moves)
    for a in range (p):
        print (str(a+1)+"-" +str(feasible_moves[a]))
    return (feasible_moves)
#Defining all possible moves for Bishop
def Get_Bishop_Moves(pos,chess_board,user_positions):
    row,column = list(pos.strip().lower())
    row = int(row)-1
    column = chess_map_from_alphabet_to_index[column]
    i,j = row,column
    feasible_moves = []
    #Down And Right Moves
    a= i+1
    b= j+1
    while(7>=a>=0 and 7>=b>=0):
        if ["".join([str(a),chess_map_from_index_to_alphabet[b]])] not in user_positions:
            feasible_moves.append((a,b))
        a,b = a+1,b+1
    #Up and left moves    
    a= i-1
    b= j-1
    while(7>=a>=0 and 7>=b>=0):
        if ["".join([str(a),chess_map_from_index_to_alphabet[b]])] not in user_positions:
            feasible_moves.append((a,b))
        a,b = a-1,b-1
    #Up and Right Moves
    a= i+1
    b= j-1
    while(7>=a>=0 and 7>=b>=0):
        if ["".join([str(a),chess_map_from_index_to_alphabet[b]])] not in user_positions:
            feasible_moves.append((a,b))
        a,b = a+1,b-1
    #down and left Moves
    a= i-1
    b= j+1
    while(7>=a>=0 and 7>=b>=0):
        if ["".join([str(a),chess_map_from_index_to_alphabet[b]])] not in user_positions:
            feasible_moves.append((a,b))
        a,b = a-1,b+1
    #Now we will filter all Negative Values
    feasible_moves = ["".join([str(i[0] + 1),chess_map_from_index_to_alphabet[i[1]]]) for i in feasible_moves]
    for x in user_positions:
        if x in feasible_moves:
            feasible_moves.remove(x)
    feasible_moves.sort()
    p = len(feasible_moves)
    for a in range (p):
        print (str(a+1)+"-" +str(feasible_moves[a]))
    #print (feasible_moves)
    return (feasible_moves)
        
#Defining all the possible moves for Queen
def Get_Queen_Moves(pos,chess_board,user_positions):
    row,column = list(pos.strip().lower())
    row = int(row)-1
    column = chess_map_from_alphabet_to_index[column]
    i,j = row,column
    currposrow = i + 1;
    currposcolumn = j + 1;
    feasible_moves = []
    #Down And Right Moves
    a= i+1
    b= j+1
    while(7>=a>=0 and 7>=b>=0):
        if ["".join([str(a),chess_map_from_index_to_alphabet[b]])] not in user_positions:
            feasible_moves.append((a,b))
        a,b = a+1,b+1
        break
    #up and left moves    
    a= i-1
    b= j-1
    while(7>=a>=0 and 7>=b>=0):
        if ["".join([str(a),chess_map_from_index_to_alphabet[b]])] not in user_positions:
            feasible_moves.append((a,b))
        a,b = a-1,b-1
        break
    #up and right moves
    a= i+1
    b= j-1
    while(7>=a>=0 and 7>=b>=0):
        if ["".join([str(a),chess_map_from_index_to_alphabet[b]])] not in user_positions:
            feasible_moves.append((a,b))
        a,b = a+1,b-1
        break
    #Down and left moves
    a= i-1
    b= j+1
    while(7>=a>=0 and 7>=b>=0):
        if ["".join([str(a),chess_map_from_index_to_alphabet[b]])] not in user_positions:
            feasible_moves.append((a,b))
        a,b = a-1,b+1
        break
    for j in range(8):
        if j != column and ["".join([str(row),chess_map_from_index_to_alphabet[j]])] not in user_positions:
            feasible_moves.append((row, j))
    for i in range(8):
        if i != row and ["".join([str(i),chess_map_from_index_to_alphabet[column]])] not in user_positions:
            feasible_moves.append((i, column))
    #Now we will filter all Negative Values
    feasible_moves = ["".join([str(i[0] + 1),chess_map_from_index_to_alphabet[i[1]]]) for i in feasible_moves]
    for x in user_positions:
        yourrow, yourcolumn = list(x.strip().lower())
        yourcolumn = chess_map_from_alphabet_to_index[yourcolumn] + 1;
        if x in feasible_moves:
            if currposrow == int(yourrow)  and currposcolumn < yourcolumn:
                for value in range(yourcolumn,9):
                    removing = ["".join([str(currposrow),chess_map_from_index_to_alphabet[value - 1]])]
                    feasible_moves = list(set(feasible_moves) - set(removing))
            if currposrow == int(yourrow)  and currposcolumn > yourcolumn:
                for value in range(1,yourcolumn + 1):
                    removing = ["".join([str(currposrow),chess_map_from_index_to_alphabet[value - 1]])]
                    feasible_moves = list(set(feasible_moves) - set(removing))
            if currposcolumn == int(yourcolumn)  and currposrow < int(yourrow):
                for value in range(int(yourrow),9):
                    removing = ["".join([str(value),chess_map_from_index_to_alphabet[currposcolumn-1]])]
                    feasible_moves = list(set(feasible_moves) - set(removing))
            if currposcolumn == int(yourcolumn)  and currposrow > int(yourrow):
                for value in range(1,int(yourrow) + 1):
                    removing = ["".join([str(value),chess_map_from_index_to_alphabet[currposcolumn-1]])]
                    feasible_moves = list(set(feasible_moves) - set(removing))
    feasible_moves.sort()
    p = len(feasible_moves)
    for a in range (p):
        print (str(a+1)+"-" +str(feasible_moves[a]))
    #print (feasible_moves)
    return (feasible_moves)

#Defining all possible moves for King
def Get_King_Moves(pos,chess_board,user_positions):
    row,column = list(pos.strip().lower())
    row = int(row)-1
    column = chess_map_from_alphabet_to_index[column]
    i,j = row,column
    feasible_moves = []
    #Down
    if ["".join([str(i+1),chess_map_from_index_to_alphabet[j]])] not in user_positions:
        feasible_moves.append((i+1, j))
    #Diagonally Right Down
    if ["".join([str(i+1),chess_map_from_index_to_alphabet[j+1]])] not in user_positions:
        feasible_moves.append((i+1, j+1))
    #Right
    if ["".join([str(i),chess_map_from_index_to_alphabet[j+1]])] not in user_positions:
        feasible_moves.append((i, j+1))
    #Diagonally Right Up
    if ["".join([str(i-1),chess_map_from_index_to_alphabet[j+1]])] not in user_positions:
        feasible_moves.append((i-1, j+1))
    #up
    if ["".join([str(i-1),chess_map_from_index_to_alphabet[j]])] not in user_positions:
        feasible_moves.append((i-1, j))
    #Diagonally Left up
    if ["".join([str(i-1),chess_map_from_index_to_alphabet[j-1]])] not in user_positions:
        feasible_moves.append((i-1, j-1))
    #Left
    if ["".join([str(i),chess_map_from_index_to_alphabet[j-1]])] not in user_positions:
        feasible_moves.append((i, j-1))
    #Diagonally Left Down
    if ["".join([str(i+1),chess_map_from_index_to_alphabet[j-1]])] not in user_positions:
        feasible_moves.append((i+1, j-1))
    #Now let us filter all negative values
    feasible_moves = ["".join([str(i[0] + 1),chess_map_from_index_to_alphabet[i[1]]]) for i in feasible_moves]
    for x in user_positions:
        if x in feasible_moves:
            feasible_moves.remove(x)
    feasible_moves.sort()
    p = len(feasible_moves)
    for a in range (p):
        print (str(a+1)+"-" +str(feasible_moves[a]))
    #print (feasible_moves)
    return (feasible_moves)

#Defining all Possible moves for Pawn
def Get_Pawn_Moves(pos, chess_board,user_positions):
    row,column = list(pos.strip().lower())
    row = int(row)-1
    column = chess_map_from_alphabet_to_index[column]
    i,j = row,column
    feasible_moves = []
    #2 Moves for the first position
    if i == 1 and ["".join([str(i+2),chess_map_from_index_to_alphabet[j]])] not in user_positions:
        feasible_moves.append((i+2, j))
    #Down
    if i+1 < 8 and ["".join([str(i+1),chess_map_from_index_to_alphabet[j]])] not in user_positions:
        feasible_moves.append((i+1, j))
    #Diagonally Right Down
    if i+1 < 8 and 0<= j+1 <8 and ["".join([str(i+1),chess_map_from_index_to_alphabet[j+1]])] not in user_positions: 
        feasible_moves.append((i+1, j+1))
    #Diagonally Left Down
    if i+1 < 8 and 0<= j-1 <8 and ["".join([str(i+1),chess_map_from_index_to_alphabet[j-1]])] not in user_positions: 
        feasible_moves.append((i+1, j-1))

    #Now let us filter all Negative Values
    feasible_moves = ["".join([str(i[0] + 1),chess_map_from_index_to_alphabet[i[1]]]) for i in feasible_moves]
    for x in user_positions:
        if x in feasible_moves:
            feasible_moves.remove(x)
    feasible_moves.sort()
    p = len(feasible_moves)
    for a in range (p):
        print (str(a+1)+"-" +str(feasible_moves[a]))   
    return (feasible_moves)
#main Function
choice = 0

feasible_moves = []
user_positions = []
#Case Condition of making a choice between 1-7
while (choice !=7):
    print("Please select one piece to move from the following:")
    print("1.Rook")
    print("2.Knight")
    print("3.Bishop")
    print("4.Queen")
    print("5.King")
    print("6.Pawn")
    print("7.Exit")
    print("------------------------------------------------------------------")
    print("------------------------------------------------------------------")
    choice= int(input())
    print("------------------------------------------------------------------")
    feasible_moves.clear()
    #Code for Rook
    if choice == 1:
        pos = input("Enter the desired position of your Rook: ")
        if pos in user_positions:
            print("Position is Already Filled")
            continue
        feasible_moves = Get_Rook_Moves(pos,chess_board,user_positions)
        user = int(input("Select position from the list of range {0}-{1}: ".format(1,str(len(feasible_moves)))))

        user_positions.append(feasible_moves[user-1])
        print(user_positions)
    #code for Knight
    if choice == 2:
        pos = input("Enter the desired position of your Knight: ")
        if pos in user_positions:
            print("Position is Already Filled")
            continue
        feasible_moves = Get_Knight_Moves(pos,chess_board,user_positions)
        user = int(input("Select position from the list of range {0}-{1}: ".format(1,str(len(feasible_moves)))))
        user_positions.append(feasible_moves[user-1])
        print(user_positions)
    #code for Bishop   
    if choice == 3:
        pos = input("Enter the desired position of your Bishop: ")
        if pos in user_positions:
            print("Position is Already Filled")
            continue
        feasible_moves = Get_Bishop_Moves(pos,chess_board,user_positions)
        user = int(input("select position from the list of range {0}-{1}: ".format(1,str(len(feasible_moves)))))
        user_positions.append(feasible_moves[user-1])
        print(user_positions)
    #Code for Queen   
    if choice == 4:
        pos = input("Enter the desired position of your Queen: ")
        if pos in user_positions:
            print("Position is Already Filled")
            continue
        feasible_moves = Get_Queen_Moves(pos,chess_board,user_positions)
        user = int(input("select position from the list of range {0}-{1}: ".format(1,str(len(feasible_moves)))))
        
        user_positions.append(feasible_moves[user-1])
        print(user_positions)
    #Code for King    
    if choice == 5:
        pos = input("Enter the desired position of your King: ")
        if pos in user_positions:
            print("Position is Already Filled")
            continue
        feasible_moves = Get_King_Moves(pos,chess_board,user_positions)
        user = int(input("select position from the list of range {0}-{1}: ".format(1,str(len(feasible_moves)))))
        
        user_positions.append(feasible_moves[user-1])
        print(user_positions)
    #Code for Pawn    
    if choice == 6:
        pos = input("Enter the desired position of your Pawn: ")
        if pos in user_positions:
            print("Position is Already Filled")
            continue
        feasible_moves = Get_Pawn_Moves(pos,chess_board,user_positions)
        user = int(input("select position from the list of range {0}-{1}: ".format(1,str(len(feasible_moves)))))
        
        user_positions.append(feasible_moves[user-1])
        print(user_positions)
    #Exit Case    
    if choice == 7:
        print("Hope you enjoyed playing the chess game")
        print("Thank You")
        break