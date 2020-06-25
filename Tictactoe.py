# ### Window management and display

# Liste de cases à tester
lignes =   [[(0, 0), (0, 1), (0, 2)],  # ligne 0
            [(1, 0), (1, 1), (1, 2)],  # ligne 1
            [(2, 0), (2, 1), (2, 2)]]  # ligne 2
#Drawing the grid :
def grid_initializtion():
    tab = []

    for i in range(3):
        tab.append(["","",""])
    return tab


colonnes = [[(0, 0), (1, 0), (2, 0)],  # colonne 0
            [(0, 1), (1, 1), (2, 1)],  # colonne 1
            [(0, 2), (1, 2), (2, 2)]]  # colonne 2
def grid_drawing(tab):
    print(" A/  B/  C/")
    print("-------------")
    print("A/")
    s = ""
    for i in range(3):
        s = s + " | " + str(tab[i])
    s = s + "|"
    print("-------------")
    print("B/")
    for i in range(3):
        s = s + " | " + str(tab[i + 3])
    s = s + "|"
    print("-------------")
    print("C/")
    for i in range(3):
        s = s + " | " + str(tab[i + 6])
    s = s + "|"
    print("-------------")
    print(s)


# ### Logic of the game

# List of boxes to be tested
rows =   [[(0, 0), (0, 1), (0, 2)],  # row 0
            [(1, 0), (1, 1), (1, 2)],  # row 1
            [(2, 0), (2, 1), (2, 2)]]  # row 2

columns = [[(0, 0), (1, 0), (2, 0)],  # column 0
            [(0, 1), (1, 1), (2, 1)],  # column 1
            [(0, 2), (1, 2), (2, 2)]]  # column 2

diag1 =     [(0, 0), (1, 1), (2, 2)]

diag2 =     [(0, 2), (1, 1), (2, 0)]


