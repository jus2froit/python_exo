
# carre_2_chiffre = []

# for i in range(4,10):
#     carre_2_chiffre.append(i*i)

# print(carre_2_chiffre)

# 2. Carré formé de deux nombres consécutifs

# 183 184 est le carre a six chiffres de 42S. On remarque que ses trois
# premiers chiffres et ses trois derniers forment deux nombres consécutifs
# 183 et 184.
# Trouver 1'unique carré a huit chiffres tel que ses quatre premiers
# chiffres et ses quatre derniers représentent deux nombres consécutifs.

print(3163*3163)

print(9999**2)

l1=[n**2 for n in range(3163, 9999)]

l2 = []
for i in l1:
    a = str(i)[0:4] 
    b = str(i)[4:9]
    if int(a) +1 == int(b):
        l2.append(i)

print(l2)


l2 = []
for i in range(3163,9999):
    carre = i ** 2
    premier_nombre = carre // 10000
    second_nombre = carre % 10000
    if premier_nombre +1 == second_nombre :
        l2.append(carre)


print(l2)

