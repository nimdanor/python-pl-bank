author=Dominique Revuz

doc==

TODO 
pour que cet exercice soit bien il faudrais que l'on vérifie que la syntaxe error a lieux
que l'élève la vois puis que l'on affiche ensuite les explications 

TODO il faudrais le code qui fait erreur soit différent pour plusieurs rappel de ce type de message incompréhensibles

en particulier le manque de : en fin de ligne pour les else 
une chaine de caractère non terminé


==


tag=error|syntaxerror
title= Corrige Moi !
name= Combien de mois
template=/template/soluce.pl
text==

Le programme python si dessous contient une erreur corrigez la pour passer à l'exercice suivant.  

Commencez par lancer la validation et regardez l'erreur.

Bizare comme Erreur Non ?! 
Cette ligne a l'air correcte.  
Et oui c'est une erreur de la ligne au dessus dans laquelle il manque une paranthèse fermante.  

Quand python dit "Syntax Error" c'est que la grammaire de python s'est pris les pieds dans le tapis...  
Et que l'on ne sais pas comment vous aider.  

Dans ce cas la il faut TOUJOURS regarder la ligne audessus. 


==

code==
n=int(input("donnez moi votre age en années :")
mois=12
print("Vous avez plus de "+str(mois*n)+" mois.")
==

showinput=true

plsoluce==
Dix huit ans | 18
Cinquante Six | 56
==

soluce==
n=int(input("donnez moi votre age en années :"))
mois=12
print("Vous avez plus de "+str(mois*n)+" mois.")
==

compilehelp==
Bizare comme Erreur Non ?!
Cette ligne a l'air correcte.
Et oui c'est une erreur de la ligne au dessus dans laquelle il manque une paranthèse fermante.

Quand python dit "Syntax Error" c'est qu'il s'est pris les pieds dans le tapis...
Et qu'il ne sais pas comment vous aider.

Dans ce cas la il faut TOUJOURS regarder la ligne audessus. 
==


