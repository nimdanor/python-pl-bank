# Copyright 2017 Dominique Revuz <dr@univ-mlv.fr>
author=Dominique Revuz 
name=sisi01.pl
title= Si et seulement si
tag= input|boolean|if # N'oubliez pas de remplir ce champs svp
template=/template/soluce.pl
text==
Ecrire un programme qui demande à l’utilisateur un entier grace au texte:
	Saisissez un entier?
Et qui si il est **strictement positif** affiche 
	Strictement Positif.
==

plsoluce==
Positif | 14
Nul | 0
Négatif | -3
==

soluce==
n=int(input("Saisissez un entier?"))
if n >0:
	print("Strictement Positif.")
==




