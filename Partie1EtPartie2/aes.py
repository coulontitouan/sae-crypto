from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import dsdes
import random
from sys import exit
from time import time


if __name__ == '__main__':
    # DOUBLE SDES
    texte = b"Ce texte est en clair. Il est vraiment tres clair."
    cle1,cle2 = random.randint(0,2**10),random.randint(0,2**10)
    intervalle = 100
    t1 = time()
    for i in range(intervalle):
        dsdes.double_sdes_decode(cle1,cle2,dsdes.double_sdes_code(cle1,cle2,texte))
    t2 = time()
    print("Temps moyen pour chiffrer et dechiffrer en double SDES la phrase {0}: {1:0.3f}s".format(texte,(t2 - t1)))
    
    # AES
    key = get_random_bytes(32)
    t1 = time()
    for i in range(intervalle):
        cipher = AES.new(key, AES.MODE_EAX)
        ciphertext, tag = cipher.encrypt_and_digest(texte)
        nonce = cipher.nonce
        cipher = AES.new(key, AES.MODE_EAX, nonce)
        data = cipher.decrypt_and_verify(ciphertext, tag)
    t2 = time()
    print("Temps moyen pour chiffrer et dechiffrer en AES la phrase {0}: {1:0.3f}s".format(texte,(t2 - t1)))

    exit()