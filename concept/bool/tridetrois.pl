# Copyright 2017 Dominique Revuz <dr@univ-mlv.fr>
author=Dominique Revuz 
name=Tri de trois
title=Tri de trois
tag= if|else

extends=/template/soluce.pl
text==

### Plus difficile 

Votre programme doit saisir trois entiers puis les afficher dans l'ordre, un par ligne.

==

# Choisir pltest ou soluce ou expectedoutput
code==
# voici trois entiers a afficher dans l'ordre croissant 
a,b,c=input().split(' ')
a,b,c=int(a),int(b),int(c)
# modifier dessous 


print(a)
print(b)
print(c)
==

soluce==
a,b,c=input().split(' ')
a,b,c=int(a),int(b),int(c)
l=[a,b,c]
ss= sorted(l)
for x in ss:
    print(x)
==


plsoluce==
Test1 |1 17 8
Test2 |77 5 6
Test3 |18 17 8
Test4 |1 1 0
Test5 |1 4 8
==




