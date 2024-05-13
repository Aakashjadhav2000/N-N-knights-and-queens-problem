import numpy as np
import matplotlib.pyplot as plt
import random
from sqlite3 import Row
import sys
import math
import time


num_column = int(sys.argv[1])
num_row= int(sys.argv[2])
num_queens = int(sys.argv[3])
num_knights = int(sys.argv[4])
tmax = int(sys.argv[5])
output_file = sys.argv[6]
method_name = sys.argv[7]



if (method_name == "HC"):
    def main():
    
        start_time = time.time()
        board_1 = [[0 for i in range(num_column)] for j in range(num_row)]
    
        board_1 = queens_solve(num_column,num_row,num_queens)
        board_1 = knight_positons(board_1, num_knights)
        print("board for placemennt:")
        print_board_1(board_1,output_file)
        end_time = time.time()
        print("Time: %.2f" % (end_time - start_time))
        
        if (end_time - start_time) > tmax:
            print("Time limit exceeded")
            return


    def knight_positons(board_2, num_knights):
        #Place the knights on the board
        for i in range(num_knights):
            while True:
                row = random.randint(0, len(board_2) - 1)
                column = random.randint(0, len(board_2[0]) - 1)
                if board_2[row][column] == 0:
                    if knight_striking_knight(board_2, row, column):
                        break
                    elif knight_striking_queen(board_2, row, column):
                            break
                    else:
                        board_2[row][column] = 2
        return board_2

    def knight_striking_knight(board_2, row, column):
        # Check the squares that the knight can move to
        if row - 2 >= 0 and column - 1 >= 0 and board_2[row - 2][column - 1] == 2:
            return True
        if row - 2 >= 0 and column + 1 < len(board_2[0]) and board_2[row - 2][column + 1] == 2:
            return True
        if row - 1 >= 0 and column - 2 >= 0 and board_2[row - 1][column - 2] == 2:
            return True
        if row - 1 >= 0 and column + 2 < len(board_2[0]) and board_2[row - 1][column + 2] == 2:
            return True
        if row + 1 < len(board_2) and column - 2 >= 0 and board_2[row + 1][column - 2] == 2:
            return True
        if row + 1 < len(board_2) and column + 2 < len(board_2[0]) and board_2[row + 1][column + 2] == 2:
            return True
        if row + 2 < len(board_2) and column - 1 >= 0 and board_2[row + 2][column - 1] == 2:
            return True
        if row + 2 < len(board_2) and column + 1 < len(board_2[0]) and board_2[row + 2][column + 1] == 2:
            return True

        return False

    def knight_striking_queen(board_2, row, column):
        # Check the squares that the knight can move to
        if row - 2 >= 0 and column - 1 >= 0 and board_2[row - 2][column - 1] == 1:
            return True
        if row - 2 >= 0 and column + 1 < len(board_2[0]) and board_2[row - 2][column + 1] == 1:
            return True
        if row - 1 >= 0 and column - 2 >= 0 and board_2[row - 1][column - 2] == 1:
            return True
        if row - 1 >= 0 and column + 2 < len(board_2[0]) and board_2[row - 1][column + 2] == 1:
            return True
        if row + 1 < len(board_2) and column - 2 >= 0 and board_2[row + 1][column - 2] == 1:
            return True
        if row + 1 < len(board_2) and column + 2 < len(board_2[0]) and board_2[row + 1][column + 2] == 1:
            return True
        if row + 2 < len(board_2) and column - 1 >= 0 and board_2[row + 2][column - 1] == 1:
            return True
        if row + 2 < len(board_2) and column + 1 < len(board_2[0]) and board_2[row + 2][column + 1] == 1:
            return True

        return False

    def queens_solve(n,m,queens):
        board_2 = [[0 for i in range(n)] for j in range(m)]
        if solve_rec(board_2, 0,queens):
                return board_2
        return None

    def solve_rec(board_3, column, queens):
            if column >= queens:
                    return True
            for i in range(queens):
                    if check(board_3, i, column):
                            board_3[i][column] = 1
                            if solve_rec(board_3, column + 1,queens):
                                    return True
                            board_3[i][column] = 0
            return False


    def check(board_check, row_check, column_check):
    # check row 
        for i in range(column_check):
            if board_check[row_check][i] == 1:
                    return False
        
        # check column
        for i in range(row_check):
            if board_check[i][column_check] == 1:
                    return False

        # check upper diagonal on left side
        i = row_check
        j = column_check
        while i >= 0 and j >= 0:
                if board_check[i][j] == 1:
                        return False
                i -= 1
                j -= 1

        # check upper diagonal on right side
        i = row_check
        j = column_check
        while i >= 0 and j < len(board_check[0]):
                if board_check[i][j] == 1:
                        return False
                i -= 1
                j += 1
        

        # check lower diagonal on left side
        i = row_check
        j = column_check
        while j >= 0 and i < len(board_check):
                if board_check[i][j] == 1:
                        return False
                i += 1
                j -= 1


        # check lower diagonal on right side
        i = row_check
        j = column_check
        while j < len(board_check[0]) and i < len(board_check):
                if board_check[i][j] == 1:
                        return False
                i += 1
                j += 1

        return True

    # count conflicts between knight and queen
    def number_conflicts(board_1):
            conflicts = 0
            for i in range(len(board_1)):
                    for j in range(len(board_1[0])):
                            if board_1[i][j] == 1:
                                    conflicts += count_queen_conflicts(board_1, i, j)
                            if board_1[i][j] == 2:
                                    conflicts += count_knight_conflicts(board_1, i, j)
            return conflicts
    
    def count_queen_conflicts(board_conf, i, j):
            conflicts = 0
            # check row on left side
            for k in range(j):
                    if board_conf[i][k] == 1:
                            conflicts += 1

            # #check row on right side    
            for k in range(j+1,len(board_conf[0])):
                if board_conf[i][k] == 1:
                        conflicts += 1

            
            # check column on upper side
            for k in range(i):
                if board_conf[k][j] == 1:
                        conflicts += 1

            #check on column on lower side
            for k in range(i+1,len(board_conf)):
                if board_conf[k][j] == 1:
                        conflicts += 1

            # check upper diagonal on left side
            k = i
            l = j
            while k >= 0 and l >= 0:
                if board_conf[k][l] == 1:
                        conflicts += 1
                k -= 1
                l -= 1
            
            # check upper diagonal on right side
            k = i
            l = j
            while k >= 0 and l < len(board_conf[0]):
                if board_conf[k][l] == 1:
                        conflicts += 1
                k -= 1
                l += 1

            # check lower diagonal on left side
            k = i
            l = j
            while l >= 0 and k < len(board_conf):
                if board_conf[k][l] == 1:
                        conflicts += 1
                k += 1
                l -= 1

            # check lower diagonal on right side
            k = i
            l = j
            while l < len(board_conf[0]) and k < len(board_conf):
                if board_conf[k][l] == 1:
                        conflicts += 1
                k += 1
                l += 1
            return conflicts

    def count_knight_conflicts(board_2,i,j):
            conflicts = 0
            if i - 2 >= 0 and j - 1 >= 0 and board_2[i - 2][j - 1] == 2:
                    conflicts += 1
            if i - 2 >= 0 and j + 1 < len(board_2[0]) and board_2[i - 2][j + 1] == 2:
                    conflicts += 1
            if i - 1 >= 0 and j - 2 >= 0 and board_2[i - 1][j - 2] == 2:
                    conflicts += 1
            if i - 1 >= 0 and j + 2 < len(board_2[0]) and board_2[i - 1][j + 2] == 2:
                    conflicts += 1
            if i + 1 < len(board_2) and j - 2 >= 0 and board_2[i + 1][j - 2] == 2:
                    conflicts += 1
            if i + 1 < len(board_2) and j + 2 < len(board_2[0]) and board_2[i + 1][j + 2] == 2:
                    conflicts += 1
            if i + 2 < len(board_2) and j - 1 >= 0 and board_2[i + 2][j - 1] == 2:
                    conflicts += 1
            if i + 2 < len(board_2) and j + 1 < len(board_2[0]) and board_2[i + 2][j + 1] == 2:
                    conflicts += 1
            return conflicts



    def print_board_1(board_1,output_file):
            # replace 1 with Q and 0 with E and print the chessboard
            for i in range(len(board_1)):
                    for j in range(len(board_1)):
                            if board_1[i][j] == 1:
                                    board_1[i][j] = 'Q'
                            elif board_1[i][j] == 2:
                                    board_1[i][j] = 'K'
                            else:
                                    board_1[i][j] = 'E'
            with open(output_file, 'w') as f:        
                for i in range(len(board_1)):
                        for j in range(len(board_1)):
                            print(board_1[i][j], end=" ", file=f)
                            print(board_1[i][j], end=" ") 
                        print(file=f, end="\n")             
                        print()
                print(number_conflicts(board_1), file=f)
            # print the number of conflicts
            print("Number of conflicts: %d" % (number_conflicts(board_1)))
        

    if __name__ == "__main__":
            main()

elif(method_name=='SA'):
    def main():

        start = time.time()
        # generate a random board of knights
        board = [random.randint(0, num_column-1) for i in range(num_row)]

        # run simulated annealing on knight board
        board = simulated_annealing(board)

        board_n = []
        for i in range(num_column):
            # avoid knight position in all rows and choose from remaining
            board_n.append(random.choice(
                [ele for ele in range(num_row) if ele != board[i]]))

        # run simulated annealing on queens minding already placed knights
        board_n = simulated_annealing(board, board_n)

        # print final board
        printBoard(board, board_n, num_queens, num_knights)
        end = time.time()
        
        print("Time taken: ", end-start)
        
        if (end - start) > tmax:
            print("Time limit exceeded")
            return



    def simulated_annealing(board_1: list, board_2: list = None) -> list:

        # set the initial temperature
        temp = 1.0

        # set the initial temperature cooling rate
        coolingRate = 0.003

        # set the initial temperature minimum
        minTemp = 0.0005
        if(board_2):
        
            while temp > minTemp:
                # get a random neighbor
                neighbor = get_Random_Neighbor(board_1, board_2)
                current_Energy = get_Energy(board_1, "Q", board_2)
                neighbor_Energy = get_Energy(board_1, "Q", board_2)
                if neighbor_Energy < current_Energy:
                    board_2 = neighbor
                elif math.exp((current_Energy - neighbor_Energy) / temp) > random.random():
                    board_1 = neighbor
                temp -= temp * coolingRate
            return board_2

        # Place Knights first
        while temp > minTemp:
            # get a random neighbor
            neighbor = get_Random_Neighbor(board_1)
            # get the current energy
            current_Energy = get_Energy(board_1, "K")

            # get the neighbor's energy
            neighbor_Energy = get_Energy(neighbor, "K")

            # if the neighbor's energy is lower, move to the neighbor
            if neighbor_Energy < current_Energy:
                board_1 = neighbor
            # if the neighbor's energy is higher, move to the neighbor with a probability
            elif math.exp((current_Energy - neighbor_Energy) / temp) > random.random():
                board_1 = neighbor

            # cool the system
            temp -= temp * coolingRate

        return board_1


    def get_Random_Neighbor(board_1: list, board_2: list = None) -> list:

        # IF KNIGHTS HAVE BEEN PLACED ALREADY,
        if(board_2):
            # MODIFY THESE TO GENERATE RANDOM NEIGHBORS MINDING THE KNIGHTS
    
            neighbor = board_2[:]
            index = random.randint(0, len(board_2)-1)
            # avoid position of K in row to prevent overwriting
            value = random.choice([ele for ele in range(
                len(board_2)) if ele != board_1[index]])

            neighbor[index] = value

            return neighbor

        # PLACING KNIGHTS
        neighbor = board_1[:]

        # get a random index
        index = random.randint(0, len(board_1)-1)

        # get a random value
        value = random.randint(0, len(board_1)-1)

        # set the neighbor's value
        neighbor[index] = value

        return neighbor


    def get_Energy(board_1: list, flag: str, board_2: list = None) -> int:
        energy = 0
        # PLACING ONLY KNIGHTS. NO QUEENS EXIST.
        if(flag == "K"):
            # increase energy if K-K conflicts exist
            # Will not cover K-Q conflicts as no Qs exist
            klen = len(board_1)
            for r in range(klen):
                s = board_1[r]
                for t in range(klen):
                    if(t == r):
                        continue
                    u = board_1[t]
                    # can knight (t,u) attack knight (r,s)?
                    if((abs(r-t) == 2 and abs(s-u) == 1) or (abs(r-t) == 1 and abs(s-u) == 2)):
                        # conflict exists
                        energy += 1


        # PLACING ONLY QUEENS. ASSUMES THAT KNIGHTS HAVE BEEN PLACED

        elif(flag == "Q"):
            blen = len(board_2)
            for i in range(blen):
                j = board_2[i]

                # Q-Q CONFLICTS
                # count vertical conflicts
                energy += board_2.count(j)-1
                # count diagonal conflicts
                for p in range(blen):
                    if p == i:
                        continue
                    q = board_2[p]
                    # Checking if other Qs lie on diagonal of current Q
                    # Diagonal condition - > horizontal displacement = vertical displacement
                    if(abs(i-p) == abs(j-q)):
                        energy += 1

                # STOP KNIGHTS FROM attacking queens
                # K-Q conflicts handled below

                # if difference in (horizontal,vertical) dist. is 1,2 or 2,1
                for r in range(len(board_1)):
                    s = board_1[r]
                    # Can any K (r,s) reach this Q (i,j) ?
                    if((abs(r-i) == 2 and abs(s-j) == 1) or (abs(r-i) == 1 and abs(s-j) == 2)):
                        # conflict exists
                        energy += 1
        return energy
    
    
    def count_conflicts(board):
        conflicts = 0
        for i in range(len(board)):
            for j in range(i+1, len(board)):
                if board[i] == board[j]:
                    conflicts += 1
                if abs(board[i] - board[j]) == abs(i - j):
                    conflicts += 1
        return conflicts


    def printBoard(board_1: list, board_2: list = None, board_3: list = None, no_knights: list = None) -> None:
        # loop through each row
        if(board_2):
            # print both queens and knights
            length_queen = len(board_2)
            counter_q = 0
            counter_k = 0
            # loop
            with open(output_file, 'w') as f:
                for i in range(length_queen):
                    for j in range(length_queen):
                        if(j == board_1[i] and counter_k != no_knights):
                            print('K', end=' ')
                            print('K', end=' ',file=f)

                            counter_k += 1
                            continue
                        if(j == board_2[i] and counter_q != board_3):
                            print('Q', end=' ')
                            print('Q', end=' ',file=f)
                            counter_q += 1
                            continue
                        print('E', end=' ')
                        print('E', end=' ',file=f)
                    print()
                    print(file=f)
                print(count_conflicts(board_2), file=f)       
            return

    if __name__ == "__main__":
        main()