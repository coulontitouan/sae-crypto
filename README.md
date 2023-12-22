# Execution du programme

## Installation générale

```bash
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
```

## Partie1

```bash
python3 ./Partie1EtPartie2/dsdes.py
```

Résultats : 
```
Temps moyen pour encrypter Lettres persanes : <temps>s
Temps moyen pour casser astucieusement Lettres persanes : <temps>s
Temps moyen pour casser brutalement Lettres persanes : <temps>s
Temps moyen pour encrypter Arsene Lupin : <temps>s
Temps moyen pour casser astucieusement Arsene Lupin : <temps>s
Temps moyen pour casser brutalement Arsene Lupin : <temps>s
```

Le programme est beacoup trop long du aux 10 cassages brutaux sur chaque texte.

## Partie 2

```bash
python3 ./Partie1EtPartie2/aes.py
```

Résultats : 
```
Temps moyen pour chiffrer et dechiffrer en double SDES la phrase b'Ce texte est en clair. Il est vraiment tres clair.': 0.350s
Temps moyen pour chiffrer et dechiffrer en AES la phrase b'Ce texte est en clair. Il est vraiment tres clair.': 0.038s
```

## Partie3

```bash
python3 ./Partie3/programmeTraceRéseau.py
```

Résultats : 
```
La crypto c'est trop bien!♠♠♠♠♠♠
Je suis complètement d'accord!☺
Fin du déchiffrement
```

## Partie4


