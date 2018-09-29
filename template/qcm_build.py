
import random,sys

def testdef(balise):
    # type: (str) ->
    if balise  not in globals():
        print("Pas de balise "+balise+" dans la définition de l'exercice ", file=sys.stderr)
        sys.exit(1)

def randomNfromlist(n,l):
    if not 0< n < 100 or  len(l)< n:
        print(" illegale value of n in function randomNfromlist ", file=sys.stderr)
        sys.exit(1)
    i=l[:]
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
        lpairs.append((x,True))
for x in lb:
    if x:
        lpairs.append((x,False))


if "nb" not in globals():
    pairs=lpairs[:]
else:
    pairs  = randomNfromlist(int(nb),lpairs)

form = """<div class="input-group"><table>"""
for i,(x,b) in enumerate(pairs):
    form += """<TR><td><input id="form_answer_"""+str(i)+"""\"  type="checkbox"  placeholder="" required>"""+x+"</td></TR>"
form += "</table></div>"


