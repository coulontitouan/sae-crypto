from scapy.all import *
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import binascii


def transformer_cle(cle_binaire):
    cle_binaire = cle_binaire*4
    hex_string = '{:x}'.format(int(cle_binaire, 2)) #convertit la clé binaire en hexadécimal
    hex = (binascii.unhexlify(hex_string).hex()).upper() #convertit la clé hexadécimal en bytes
    return bytes.fromhex(hex) #convertit la clé en bytes

def filtrer_packets(trace):
    packets = rdpcap(trace) #lit le fichier trace
    udp_packets = [] #liste des paquets UDP
    for packet in packets: #parcours des paquets
        if UDP in packet and packet[UDP].dport == 9999: #si le paquet est UDP et que le port de destination est 9999
            udp_packets.append(packet) #ajout du paquet à la liste
    return udp_packets

def charger_messages(trace):
    packets = filtrer_packets(trace) #récupération des paquets UDP
    messages = [] #liste des messages
    for packet in packets: #parcours des paquets
        data = packet[Raw].load #récupération des données
        if isinstance(data, list): #si les données sont une liste
            data = b''.join(data) #on les concatène
        messages.append(data) #ajout du message à la liste
    return messages

def decrypt_message(key, trace):
    #Extraction des messages
    messages = charger_messages(trace) 
    # Extraire l'IV du début du message chiffré
    for msg in messages: #parcours des messages
        iv = msg[:16] #récupération de l'IV
        ciphertext = msg[16:] #récupération du message chiffré
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend()) #création du déchiffreur
        decryptor = cipher.decryptor() #initialisation du déchiffreur
        print((decryptor.update(ciphertext) + decryptor.finalize()).decode("utf-8")) #déchiffrement et affichage du message
    return "Fin du déchiffrement"


CLE_BINAIRE = "1110011101101101001100010011111110010010101110011001000001001100"

print(decrypt_message(transformer_cle(CLE_BINAIRE), "trace_sae.cap"))