import random
# code 4.1
# la fonction `random.randint()` permet de tirer un nombre entier au hasard
# affectaction d'un nombre entier entre 0 et 99 à la variable number
number = random.randint(0, 99)
print(number)


# exo 4.1
# écrivez un bloc if qui affiche
# - "le nombre est égale à 1" si la variable number contient un 1
# - "le nombre est différent de 1" si la variable number ne contient pas de 1

# affectaction du nombre 0 ou 1 à la variable number
if number == 1:
    print("la variable number est égale a 1")
else:
    print("la variable est différente de 1")

#4.2
if number % 2 == 0:
    print("le nombre est pair")
else:
    print("le nombre est impaire")

#4.3
if number % 3 == 0:
    print("le nombre est divisible par 3")
else:
    print("le nombre n'est pas divisible par 3")

#4.4
if number>=5:
    print("la variable est superieur à 5")
else:
    print("le nombre est inférieur à 5")

# exo 4.5
# écrivez un bloc if qui affiche
# - "le nombre est compris entre 0 et 49 inclus" si la variable number contient une valeur comprise entre 0 et 49
# - "le nombre n'est pas compris entre 0 et 49 inclus" si la variable number ne contient pas de valeur comprise entre 0 et 49

# affectaction d'un nombre entier entre 0 et 99 à la variable number
number = random.randint(0, 99)
print(number)

if number <= 49:
    print("le nombre est compris entre 0 et 49 inclus")
elif number <= 66:
    print("le nombre n'est pas compris entre 0 et 49 inclus")


#4.6
number = random.randint(0,99)
print (number)

if number <= 33:
    print("le nombre est compris entre 0 et 33 inclus")
elif number <= 66:
    print("le nombre est compris entre 34 et 66 inclus")
else:
    print("le nombre n'est pas compris entre 0 et 66 inclus")

# # 4.7
a = random.randint(0,99)
b = random.randint(0,99)
print("a =",a)
print("b =",b)

if a < b:
    print("b superieur à a")
elif b < a:
    print("a superieur à b")
else:
    print("a et b sont égaux")

# 4.8
mails = random.randint(0, 5)
print(mails)

if mails==0:
    print("il n' y pas de nouveaux mail")
elif mails==1:
    print("il y a un nouveau mail")
else:
    print("il y a ",mails ,"nouveaux mails")




