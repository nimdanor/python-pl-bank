# Copyright 2017 Dominique Revuz <dr@univ-mlv.fr>
author=Dominique Revuz 
name=condbool.pl
title= Condition booléenne  # N'oubliez pas de remplir ce champs svp
tag= input|boolean|if # N'oubliez pas de remplir ce champs svp
template=/template/coding.pl
text==
# Super Fly 
Super Fly est une compagnie aerienne a bas cout qui fait payer un supplement
en cas de bagages trops lourds.

Ecrire un programme qui demande à l’utilisateur le poids de son bagage en kilos.  
```
{{prompt}}
```

Si son bagage pèse plus de {{poid}} kilos, le programme affichera le message :  
```
Il y a un supplément de {{supplement}} euros pour un bagage de plus de {{poid}} kilos.
```

Tests: {{input0}},{{input1}},{{input2}}
==

before==
import random 

prompt="Entrez le poid entier du bagage :"
poid=random.choice([10,20,30,40])
supplement=random.choice([10,20,30,40])
code = '''entree= int(input(\"{}\"))'''.format(prompt)
affiche="Il y a un supplément de {} euros pour un bagage de plus de {} kilos.".format(supplement,poid)



soluce='''
{}
if entree> {}:
    print("{}")

'''.format(code, poid, affiche)


input0=poid+5
input1=poid-5
input2=poid*poid

==
# Choisir pltest ou soluce ou expectedoutput

expectedoutput=Il y a un supplément de 30 euros pour un bagage de plus de 20 kilos.







