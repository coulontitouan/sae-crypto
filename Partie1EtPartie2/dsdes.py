import random
import sdes
from sys import exit
from time import time
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def code(cle, texte):
    result = bytearray()
    cle1, cle2 = sdes.keyGen(cle)

    for octet in texte:
        octet_crypte = sdes.encrypt(cle1, octet)
        result.append(octet_crypte)

    return bytes(result)

def decode(cle, texte): # Decode avec la clé
    result = bytearray()
    cle1, cle2 = sdes.keyGen(cle)

    for octet in texte:
        octet_crypte = sdes.decrypt(cle1, octet)
        result.append(octet_crypte)

    return bytes(result)

def double_sdes_code(cle1, cle2, message_clair):
    cryptage1 = code(cle1, message_clair)
    cryptage2 = code(cle2, cryptage1)
    return cryptage2

def double_sdes_decode(cle1, cle2, message_chiffre):
    decryptage1 = decode(cle2, message_chiffre)
    decryptage2 = decode(cle1, decryptage1)
    return decryptage2

def cassage_brutal_simple_sdes(message_clair, message_chiffre):
    for cle in range(2**10):
        message_dechiffre = decode(cle, message_chiffre)
        if message_dechiffre == message_clair:
            return (cle,decode(cle, message_chiffre))

def cassage_brutal(message_clair, message_chiffre):
    for cle1 in range(2**10):
        for cle2 in range(2**10):
            message_dechiffre = double_sdes_decode(cle1, cle2, message_chiffre)
            if message_dechiffre == message_clair:
                return ((cle1, cle2), double_sdes_decode(cle1, cle2, message_chiffre))

def cassage_astucieux(message_clair, message_chiffre):
    dico_resultats = {}

    for cle1 in range(2**10):
        resulat = double_sdes_code(cle1, 0, message_clair)
        dico_resultats[resulat] = cle1

    for cle2 in range(2**10):
        message_dechiffre = double_sdes_decode(0, cle2, message_chiffre)
        if message_dechiffre in dico_resultats.keys():
            cle1 = dico_resultats[message_dechiffre]
            return ((cle1, cle2), double_sdes_decode(cle1, cle2, message_chiffre))

if __name__ == '__main__':
    lettres_persanes = open("Partie1EtPartie2/lettres_persanes.txt", "rb").read()
    arsene_lupin = open("Partie1EtPartie2/arsene_lupin_extrait.txt", "rb").read()
    intervalle = 10

    for texte in [lettres_persanes, arsene_lupin]:
        nom = "Lettres persanes" if texte == lettres_persanes else "Arsene Lupin"

        # CRYPTAGE DECRYPTAGE
        for i in range(intervalle):
            cle1,cle2 = random.randint(0,2**10),random.randint(0,2**10)

            t1 = time()
            double_sdes_code(cle1,cle2,texte)
            t2 = time()

        print("Temps moyen pour encrypter {0} : {1:0.3f}s".format(nom,(t2 - t1)/intervalle))

        # CASSAGE ASTUCIEUX
        essais = 0
        for i in range(intervalle):
            cle1,cle2 = random.randint(0,2**10),random.randint(0,2**10)
            
            t1 = time()
            res = cassage_astucieux(texte,double_sdes_code(cle1,cle2,texte))
            essais += res[0][0] + res[0][1]
            t2 = time()

        print("Temps moyen pour casser astucieusement {0} : {1:0.3f}s ({2} essais)".format(nom,(t2 - t1)/intervalle, essais/intervalle))
        
        # CASSAGE BRUTAL
        essais = 0
        for i in range(intervalle):
            cle1,cle2 = random.randint(0,2**10),random.randint(0,2**10)
            
            t1 = time()
            res = cassage_brutal(texte,double_sdes_code(cle1,cle2,texte))
            essais += res[0][0] + res[0][1]

        t2 = time()
        print("Temps moyen pour casser brutalement {0} : {1:0.3f}s ({2} essais)".format(nom,(t2 - t1)/intervalle, essais/intervalle))
        
    exit()
