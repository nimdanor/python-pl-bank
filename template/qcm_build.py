
import random,sys

def testdef(balise):
    # type: (str) ->
    if balise  not in globals():
        print("Pas de balise "+balise+" dans la définition de l'exercice ", file=sys.stderr)
        sys.exit(1)

def randomNfromlist(n,tr,fl, nbtrues):
    if nbtrues:
        random.shuffle(tr)
        if nbtrues > len(fl):
            print(" Not enough True answers nbtrues= ", nbtrues, file=sys.stderr)
            sys.exit(1)
        tr=tr[0:nbtrues]
        n=n-nbtrues
        if n>len(fl):
            print(" Not enough false answers to complete the question ", n,"needed", file=sys.stderr)
            sys.exit(1)
        random.shuffle(fl)
        return tr+fl[0:n]
    else:

        if not 0< n  or  len(tr)+len(fl)< n:
            print(" illegale value of n in function randomNfromlist ", file=sys.stderr)
            sys.exit(1)
        i=tr+fl
        random.shuffle(i)
        return i[0:n]




#testdef("good")
#testdef("bad")

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
    if x:
        goodpairs.append((x,True))
for x in lb:
    if x:
        badpairs.append((x,False))


if "nb" not in globals():
    # si on dit rien on prend tout
    pairs=goopairs + badpairs
else:
    if "nbtrues" not in globals():
        pairs  = randomNfromlist(int(nb), goodpairs, badpairs, 0)
    else:
        pairs = randomNfromlist(int(nb), goodpairs, badpairs, int(dic['nbtrues']))


form = """<div class="input-group"><table>"""
for i,(x,b) in enumerate(pairs):
    form += """<TR><td><input id="form_answer_"""+str(i)+"""\"  type="checkbox"  placeholder="" required>"""+x+"</td></TR>"
form += "</table></div>"


