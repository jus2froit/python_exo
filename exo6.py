import random



# #6.1
# my_list= [5, 3.3, "abc", True]

# #6.2
# print(my_list[2])

# #6.3
# my_list.append("xyz")
# print(my_list)

# #6.4
# del my_list[1]
# print(my_list)

# #6.5
# my_list[1] = random.randint(0,99)
# print(my_list)

# #6.6
# print(len(my_list))

#6.7
my_list = ['foo', 'bar', 'baz', 'lorem', 'ipsum']


#6.8

my_list = [2.71, 42]
somme =0
for i in my_list:
    somme += i
print (somme)

#6.9

my_list = [2.71, 42, 123, 2, 3.14, 1.61]
somme =0
for i in my_list:
    somme += i
print (somme)

#6.10

#je reprend la somme de l'exo precedent

moyenne = somme / len ( my_list)
print("moyenne liste:" ,moyenne)

#6.11

print(my_list.index(3.14))

#6.12

nombre_inf_10 = 0
for i in my_list:
    if i <= 10:
        nombre_inf_10 +=1
print(nombre_inf_10)

#6.13

for i in my_list:
    my_list[my_list.index(i)]=i*2
print(my_list)

#6.14

my_list_int = []
my_list = [2.71, 42, 123, 2, 3.14, 1.61]

for i in my_list:
    if i == int(i):
        my_list_int.append(i)

print(my_list_int)

#6.15

my_list = [2.71, 42, 123, 2, 3.14, 1.61]


for i in range (len(my_list)):
    if i%2 == 0:
        my_list[i], my_list[i+1]=my_list[i+1], my_list[i]


print(my_list)

#6.16

my_list = [2.71, 42, 123, 2, 3.14, 1.61]
taille = len(my_list)

for i in range (taille):
    for j in range (i,taille-1):
        if my_list[i]>my_list[j]:
            my_list[j], my_list[i] = my_list[i], my_list[j]


print(my_list)

#6.17

size = 5
matrix = []

for _ in range(0, size):
    row = [random.randint(40, 100) for _ in range(0, size)]
    matrix.append(row)

print(matrix)

ligne_3 = matrix[2]

print(ligne_3[3])

#6.18

# for i in range (len (matrix)):
#     lig = matrix[i]
#     for j in range (len(lig)):
#         nb = lig[j]
#         if nb<=50:
#             print(nb, "colonne =", j+1, "ligne =", i+1)



for i in range (len (matrix)):
    lig = matrix[i]
    for j in range (len(lig)):
        nb = lig[j]
        if nb<=50:
            print(f"{nb}, colonne = {j+1} ligne = {i+1}")