import os

def jouer_coup(plateau:dict, joueur:str, coup:str) -> None:
    """Fonction qui joue un coup (Ne vérifie pas si le coup est valide)

    Args:
        plateau (dict): Le plateau de jeu
        joueur (str): "O" ou "X"
        coup (str): Coordonnées de la forme "A1"
    """
    plateau[coup[0].upper()][int(coup[1])] = joueurs
    

def afficher_grille(plateau:dict) -> None:
    """Fonction qui affiche la grille du morpion

    Args:
        plateau (dict): Un plateau de jeu
    """
    os.system("clear")
    print(" \t|\t0\t|\t1\t|\t2\t|")
    print("---------------------------------------------------------")
    for cle in plateau:
        print(cle, end="\t|\t")
        for elt in plateau[cle]:
            if elt == None:
                print(" ", end="\t|\t")
            else:
                print(elt, end="\t|\t")
        print("\n---------------------------------------------------------")
        
def est_gagnante(plateau:dict) -> bool:
    """Fonction qui vérifie si la grille est gagnante

    Args:
        plateau (dict): Le plateau de jeu

    Returns:
        bool: True si la grille est gagnante, False sinon
    """
    
    # Vérification des lignes
    for cle in plateau:
        if plateau[cle][0] == plateau[cle][1] == plateau[cle][2] and plateau[cle][0] != None:
            return True
        
    # Vérification des colonnes
    for i in range(3):
        if plateau["A"][i] == plateau["B"][i] == plateau["C"][i] and plateau["A"][i] != None:
            return True
    
    # Vérification des diagonales
    if plateau["A"][0] == plateau["B"][1] == plateau["C"][2] and plateau["A"][0] != None:
            return True
    
    if plateau["A"][2] == plateau["B"][1] == plateau["C"][0] and plateau["A"][2] != None:
            return True
    
    return False