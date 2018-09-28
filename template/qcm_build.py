import balise

import random

def testdef(balise):
    # type: (str) ->
    if balise  not in globals():
        print("Pas de balise "+balise+" dans la définition de l'exercice ", file=sys.stderr)
        sys.exit(1)

def randomNfromlist(n,l):
    if not 0< n < 100 or  len(l)< n::
        print(" illegale value of n in function randomNfromlist ", file=sys.stderr)
        sys.exit(1)
    if len(l)== n :
        return l
    random.shuffle(l)
    return l[0:n]




testdef("good")
testdef("bad")

if good.endswith("\n\n"):
    good=good[0:-1]
    print(" trailing \n")
if bad.endswith("\n\n"):
    bad=bad[0:-1]
    print(" trailing \n")

lg= good.split("\n")
lb= bad.split("\n")

lpairs=[]
for x in lg:
    lpairs.append((x,True))
for x in lb:
    lpairs.append((x,False))


if "nb" not in globals():
    pairs=lpairs
else:
    pairs  = randomNfromlist(nb,lpairs)

form = """<div class="input-group">"""
for x,b in pairs:
    form += """<input id="form_answer" name="""" +x+""" type="checkbox"  placeholder="" required>"""+x+"<br>"
form += "</div>"
