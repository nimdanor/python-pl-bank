# Copyright 2017 Dominique Revuz <dr@univ-mlv.fr>
author=Dominique Revuz 
name=sisi004.pl
title= Si  Sinon  
tag= input|else|if|elif|bool|and|or|paranthesis
template=/python/0PLG/template.pl
text==
## IF ELIF ELSE
Ecrire un programme qui demande à l’utilisateur trois entiers a,b et c par exemple:
	31
	14
	17

Et qui utilise un seul test if et affiche **OUI** si
	a > 12 et b >12
	ou bien si
	 c <20
Sinon affiche **NON**

==



input0==
12
66
23
==

input1==
12
12
12
==
input2==
66
12
700
==


soluce==
a=int(input())
b=int(input())
c=int(input())
if (a<12 and b <12) or c<20 :
    print("NON")
else:
    print("OUI")
==



