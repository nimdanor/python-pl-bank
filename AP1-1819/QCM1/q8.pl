
template=/template/qcm_template.pl

title=Question 5


mybuild==
import random
chaine= random.choice(['pomme','banana','bannane','poire'])
entier= random.randint(5,8)

text=""" Qu'affiche le programme suivant :

    print(len('{}')*{})""".format(chaine,entier)

good=str(len(chaine)*entier)
bad=chaine*entier
bad+='\n'
bad += chaine+str(entier)
bad += '\n0'
==
text= Indiquez les lignes qui sont des commentaires en python :



nb=4
nbtrues=1
uncrosedfalse=
good==
# Ceci est un commentaire 
==

bad==
[*  Ceci est un commentaire  *]
/*  Ceci est un commentaire */
//  Ceci est un commentaire 
@  Ceci est un commentaire 
@@  Ceci est un commentaire  @@
:param  Ceci est un commentaire 
REM  Ceci est un commentaire 
COMMENT:  Ceci est un commentaire 
==

feedback=show

