
author=DR
title= Initialisation d'une variable.
tag=variable
text==


Intialisez les variables jour, mois, annee avec la date du jour

==

@ /builder/before.py [builder.py]

before==
import datetime
d=datetime.datetime.now()
pltest="""
>>> jour #  le jour 
%d
>>> mois # le mois
%d
>>> annee # l'année 
%d
>>>
""" % (d.day, d.month, d.year)
==

code==

==



template=/template/pltest.pl





