import random
from hashlib import sha256
def generer_cle(longueur):
    lettre_min = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
                  'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                  'u', 'v', 'w', 'x', 'y', 'z']

    lettre_maj = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
                  'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                  'U', 'V', 'W', 'X', 'Y', 'Z']

    chiffre = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    caract_spe = ['&', '#', '@', '$', '%', '.', '?', '!']
    tout_caract = lettre_min + lettre_maj + chiffre + caract_spe
    cle = ''.join(random.choice(tout_caract) for _ in range(longueur))
    print(cle)
    return cle

def brut_froce(cle):
    lettre_min = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
                  'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                  'u', 'v', 'w', 'x', 'y', 'z']

    lettre_maj = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
                  'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                  'U', 'V', 'W', 'X', 'Y', 'Z']

    chiffre = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    caract_spe = ['&', '#', '@', '$', '%', '.', '?', '!']

    combinaisons = [lettre_min, lettre_maj, chiffre, caract_spe]
    longueur = 5  # Longueur de la clé

    trouve = False
    indices = [0] * longueur

    while not trouve:
        cle_brute_forcee = ''.join(combinaisons[i][indices[i]] for i in range(longueur))
        print(cle_brute_forcee)

        if cle_brute_forcee == cle:
            print("Clé trouvée :", cle_brute_forcee)
            trouve = True
        else:
            # Mettez à jour les indices
            i = longueur - 1
            while i >= 0 and indices[i] == len(combinaisons[i]) - 1:
                indices[i] = 0
                i -= 1
            if i == -1:
                break
            indices[i] += 1


#def substitution_cle(cle):
    #lettre_maj = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
     #             'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
      #            'U', 'V', 'W', 'X', 'Y', 'Z']
    #chiffre = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    #longueur_cle = len(cle)
    #for indice in cle:
     #   print(indice)


def hash_cle_hexa (cle):
    hash_cle = sha256(cle.encode('utf-8')).hexdigest()
    return hash_cle

def hash_cle_bite(cle):
    bite_cle = sha256(cle.encode('utf-8')).digest()
    return bite_cle

def chiffrement (fichier_input,fichier_output,cle):
    with open(fichier_input,'rb') as fichier_i:
        with open(fichier_output,'wb') as fichier_o:
            compteur_bite = 0
            while fichier_i.peek():
                octet = ord(fichier_i.read(1))
                calcul = compteur_bite % len(hash_cle_bite(cle))
                calcul_chiffrement = bytes([octet^hash_cle_bite(cle)[calcul]])
                fichier_o.write(calcul_chiffrement)
                compteur_bite = compteur_bite + 1


cle =  generer_cle(5)
brut_froce(cle)

#print(hash_cle_hexa(cle))

#hash_cle_bite(cle)

#chiffrement("test.txt","test_crypt",cle)