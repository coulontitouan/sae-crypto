# SAE Crypto - Partie 2
## Partie 1: premières tentatives

1) En supposant que RSA soit utilisé correctement, Eve peut-elle espérer en venir à bout? En vous appuyant sur votre cours, justifiez votre réponse.  
On suppose que RSA est bien utilisé, donc que `p` et `q` soient d'une longueur suffisante et que la clé privée ne soit pas divulguée, Eve ne devrait pas compter sur le crackage brutal de RSA car ça lui bien trop de temps ( x millions d'années ) car elle devrait décomposer `n` en facteurs premiers.  

2) En quoi l’algorithme SDES est-il peu sécurisé? Vous justifierez votre réponse en analysant le nombre d’essai nécessaire à une méthode “force brute” pour retrouver la clé.  
L'algorithme SDES utilise des clés de 10 bits de longueur donc 2^10 = 1024 clés disponibles, il faut faudrait donc 512 essais en moyenne pour "brute-forcer" le SDES, donc pour le double SDES

3) Est-ce que double SDES est-il vraiment plus sur? Quelle(s) information(s) supplémentaire(s) Eve doit-elle récupérer afin de pouvoir espérer venir à bout du double DES plus rapidement qu’avec un algorithme brutal ? Décrivez cette méthode astucieuse et précisez le nombre d’essai pour trouver la clé
 

## Partie 2: Un peu d’aide

## Partie 3: Analyse des messages

## Partie 4: Un peu de recul