
template=/template/qcm_template.pl

title=  Toto ?? 


mybuild==
import random
t1="""
    def f(n):
        print(n)
        return n
        print("titi")

    print(f("toto"))
"""
t2="""
    def f(n):
        print("toto")
        return n
        print(n)

    print(f("toto"))
"""

t3="""
    def f(n):
        return n

    print(f("toto")*2)
"""



lt=[t1,t2,t3]
chaine= random.choice(lt)

text=""" Qu'affiche le programme suivant :

    {}""".format(chaine)

good="totototo"
bad="""
tototiti
tititoto
toto
n'affiche rien
"""




==

text=" geenreated" 

nb=4
nbtrues=1
uncrosedfalse=
good==
# Ceci est un commentaire 
==

bad==
==

feedback=show

