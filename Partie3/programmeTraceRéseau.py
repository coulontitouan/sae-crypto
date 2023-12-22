from scapy.all import *
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import binascii


def obtenir_cle_hexa(cle_binaire):
    cle_binaire = cle_binaire*4
    hex_string = '{:x}'.format(int(cle_binaire, 2)) #convertit la clé binaire en hexadécimal
    hex = (binascii.unhexlify(hex_string).hex()).upper() #convertit la clé hexadécimal en bytes
    return bytes.fromhex(hex) #convertit la clé en bytes

def filtrer_paquets(trace):
    paquets = rdpcap(trace) #lit le fichier trace
    paquets_udp = [] #liste des paquets UDP
    for paquet in paquets: #parcours des paquets
        if UDP in paquet and paquet[UDP].dport == 9999: #si le paquet est UDP et que le port de destination est 9999
            paquets_udp.append(paquet) #ajout du paquet à la liste
    return paquets_udp

def charger_messages(trace):
    paquets = filtrer_paquets(trace) #récupération des paquets UDP
    messages = [] #liste des messages
    for paquet in paquets: #parcours des paquets
        data = paquet[Raw].load #récupération des données
        if isinstance(data, list): #si les données sont une liste
            data = b''.join(data) #on les concatène
        messages.append(data) #ajout du message à la liste
    return messages

def decrypter_message(cle, trace):
    #Extraction des messages
    messages = charger_messages(trace) 
    # Extraire l'ale du début du message chiffré
    for msg in messages: #parcours des messages
        ale = msg[:16] #récupération de l'ale, inutile
        ciphertext = msg[16:] #récupération du message chiffré
        cipher = Cipher(algorithms.AES(cle), modes.CBC(ale), backend=default_backend()) #création du déchiffreur
        decryptor = cipher.decryptor() #initialisation du déchiffreur
        print((decryptor.update(ciphertext) + decryptor.finalize()).decode("utf-8")) #déchiffrement et affichage du message
    return "Fin du déchiffrement"


CLE_BINAIRE = "1110011101101101001100010011111110010010101110011001000001001100"

print(decrypter_message(obtenir_cle_hexa(CLE_BINAIRE), "Partie3/trace_sae.cap"))