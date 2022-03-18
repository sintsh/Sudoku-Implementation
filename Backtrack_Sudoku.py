import time
# An helper function used to find the next empty value in the puzzle.
# If an empty value is found, we return "c", a list coordinate (row, col).

def next_empty(p):
    for row in range(len(p)):
        for col in range(len(p[0])):
            if p[row][col] == 0:
                return (row, col)
    return None


# Looks to see whether or not a number (n) can be placed at a certain 
# coordinate (c). Returns True if we can place "n" on "c", otherwise
# we return False. Note that here "c" is a list coordinate (row, col). 

def is_available(p, c, n):
    row = c[0]
    col = c[1]
    
    # We first check to see if "n" is in the row we wish to set it in
    if n in p[row]:
            return False
    
    # Then, we check to see if "n" is in the given collumn
    for i in range(len(p)):
        if n == p[i][col]:
            return False
        
    # Lastly we check to see whether or not "n" is in the cell where "c" 
    # is located. Note that in order to perform this method on a greater
    # puzzle (more than 9x9), this is the sub-method we should modify.
    row = (row//3)*3
    col = (col//3)*3 
    for i in range(3):
        for j in range(3):
            if p[row+i][col+j]==n:
                return False
    
    # Else, "n" was not found is thus available at "c".
    return True


    # Core function used in this algorithm. It starts by looking for an empty
# value, if none are found, we completed the puzzle (base case). Otherwise,
# we will use backtracking (a form of recursion) to solve the puzzle.

def backtrack(p):    
    c = next_empty(p)
    if c == None:
        return True
    else:
        row = c[0]
        col = c[1]
    
    # For each digit (0-9), we check to see if this digit (n) is available at said
    # location. If so, we set it to be (n) and then make a recursive call. If the call
    # ends up returning False, we set the location to be empty and go on with the loop.

    for n in range(1,10):
        if is_available(p, c, n):
            p[row][col] = n
            if backtrack(p):
                return True
            else:
                p[row][col] = 0
    return False



def Backtrack_solve(board):
    print ("\nSolving with Bactrack...")
    is_solved = False

    start_time = time.time()
    if backtrack(board):
        is_solved = True
    else:
        is_solved = False

    elapsed_time = time.time() - start_time
    
    if is_solved:
        
        print ("Found solution")
        for row in board:
            print (row)
    else:
        print ("No possible solutions") 
        
    print ("Elapsed time: " + str(elapsed_time) + " seconds")

    return   elapsed_time, is_solved