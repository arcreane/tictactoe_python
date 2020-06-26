# ## Window management and display

# 1. :

def grid_initialization():
    tab = []
    for i in range(3):
        tab.append(['_','_','_|'])
    return tab
        

def drawing_grid(tab):
    s = ""
    for i in range(3):
        for j in range(3):
            s = s + "|" + str(tab[i][j])
        s = s + "\n"
    print(s)
    


# 2. :


def drawing_shot(player, i, j, tab):
    """Draw a cross or circle in the 
    box (i, j), depending on the player indicated."""
    if player == 'X':
        tab[i][j] = 'X'
    else:
        tab[i][j] = 'O'
    drawing_grid(tab)


# 3. :


def final_message(message,player):
    
    print(message + player)


# ## Event management

# 5. :

def data_entry():
    
    x=input("Saisie la ligne ")
    if(int(x)<0 or int(x)>2):
        x=input("Saisie la ligne ")
        
    y=input("Saisie la colonne ")
    if(int(y)<0 or int(y)>2):
        y=input("Saisie la colonne ")
    return (int(x),int(y))





# ## Game Logic

# 6. :

lines =   [[(0, 0), (0, 1), (0, 2)],  # line 0
            [(1, 0), (1, 1), (1, 2)],  # line 1
            [(2, 0), (2, 1), (2, 2)]]  # line 2

columns = [[(0, 0), (1, 0), (2, 0)],  # column 0
            [(0, 1), (1, 1), (2, 1)],  # column 1
            [(0, 2), (1, 2), (2, 2)]]  # column 2

diag1 =     [(0, 0), (1, 1), (2, 2)]

diag2 =     [(0, 2), (1, 1), (2, 0)]


# 7. All equal :


def all_equal(plateau, player, boxes):
    """Returns True ssi all data boxes 
    were played by the indicated player."""
    for boxe in boxes:
        if boxe not in plateau:
            return False
        if plateau[boxe] != player:
            return False
    return True
            


# 8. :


def win_shot (plateau, player, i, j):
    """Returns True if the hit (i, j) is winning 
    for the indicated player."""      

    if all_equal(plateau,player,lines[i]):
            return True
    if all_equal(plateau,player,columns[j]):
            return True
    if i == j:
        if all_equal(plateau,player,diag1):
            return True
    if i+j == 2: #the click is in the 2nd diagonal if i+j == 2
        if all_equal(plateau,player,diag2):
            return True
    return False


# 9. :


def next_player (player):
    """Returns the name of the next player."""
    if player == 'X':
        return 'Y'
    return 'X'


# 10. :


def completed(plateau):
    """Returns True if the tray is full, False otherwise."""
    return len(plateau) == 9


# ## Game launch function

# 11. :


def game():   
    """Game launch."""
    
    # Creating the window and displaying the grid
    tab=grid_initialization()
    drawing_grid(tab)

    # Initial Game Status
    plateau = {}
    player = 'X'  # the "cross" player plays first
    
    # Main loop
    while not completed(plateau):
        i, j = data_entry()
        drawing_shot(player, i, j,tab)
        plateau[(i, j)] = player
        if win_shot(plateau, player, i, j):
            final_message(player + " A GAGNÉ !")
            break
        player = next_player(player)
    else:  # Only executed in the absence of break
        final_message("MATCH NUL !",' ')
        

# Game's launch
game()
