
author=DR
title= Initialisation d'une variable.
tag=variable
text==


Intialisez les variables jour, mois, annee avec la date du jour

==

build==
def build(dic):
    import datetime
    d=datetime.datetime.now()
    dic['pltest']=""">>> jour
%d
>>> mois
%d
>>> annee
%d
>>>
""" % (d.day, d.month, d.year)
    return dic
==

code==

==

# comme ca cela se passera bien
pltest==
>>> import datetime
>>> date=datetime.datetime.now()
>> jour==date.day
True
>> mois==date.month
True
>> annee == date.year
True
==

template=/template/coding.pl


pltest==
>>> import datetime
>>> d=datetime.datetime.now()
>>> j=d.day
>>> m=d.month
>>> a=d.year
>>> j==jour
True
>>> m==mois
True
>>> a==annee
True
==




