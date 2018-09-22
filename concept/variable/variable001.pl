
author=DR
title= Initialisation d'une variable.
tag=variable

template=/template/pltest.pl

text==

Créer trois variables pim pam et pom contenant respectivement 1 2 et 3.

==

code==
pim,pam,pom=0,0,0
==

# comme ca cela se passera bien
pltest==
>>> pim
1
>>> pam
2
>>> pom
3
==

editor.fontsize=24

@ /utils/sandboxio.py

