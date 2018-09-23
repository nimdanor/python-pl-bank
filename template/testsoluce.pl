

# ceci est un exercice pour les tests qui permet de verifier le template soluce.pl
template=/template/soluce.pl


text==
ecrire un script qui lit une string 
et qui recopie  la string sur la sortie standard 

le test triche cela ne fonctionne que pour la chaine success 
pour la chainei cela fait une failure et pour error cela fait une erreur  
==


soluce==
x=input()
if x=="success":
   print(x)
if x=="failure":
   print("NON c'est pas ca")
if x=="error":
   print(x/0)
==

code==
# ne pas modifier ce code il permet le test
x=input()
print(x)
==

plsoluce==
un success|success
ce test iproduit une failure|failure
ce test produit une erreur |error
==
