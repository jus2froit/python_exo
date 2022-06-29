#2.1
# Affectez :
# - le nombre 42 à une variable
# - le nombre d'or 1,61 à une variable
# - votre nom et prénom à une variable
# - la valeur booléenne vrai si nous sommes le matin, sinon la valeur booléenne faux, à une variable
# - la valeur nulle `None` à une variable
# Affichez ces variables
a = 42
b = 1.61
prenom = "Julian"
nom = "Devienne"
matin = True
var = False
null = None

print("a =",a)
print("b =",b)
print("prenom :",prenom)
print("nom :",nom)
print("matin :",matin)
print("variable", var)
print(null)


# 2.2
# Stockez les valeurs suivantes dans une variable et transtypez-les :
# - integer 2 en un float
# - float 1,62 en un integer
# - float 1,62 en un float arrondi à zéro chiffre après la virgule, puis en un integer
# - float 1,62 en un float arrondi à un chiffre après la virgule
# À chaque fois stockez le résultat dans une variable et affichez le résultat.
x = 2
print(float(x))

y = 1.62
print(int(y))

print(float(int(y)))

print(int(round(y, 0)))

print(round(y, 1))


