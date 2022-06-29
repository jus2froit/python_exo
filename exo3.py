#3.1

from audioop import avg


birthyear = 1988
year = 2022

age = year - birthyear
print(age)

#3.2

candies = 15
chocolates = 17
friends = 3

candies_rest = 15 % 3
chocolates_rest = 17 % 3
print("bonbons restant:",candies_rest)
print("chocolats restant:",chocolates_rest)

#3.3
candies_per_person = int((candies - candies_rest) / 3)
chocolates_per_person = int((chocolates - chocolates_rest) / 3)
print("chaque personne aura", chocolates_per_person, "chocolats")
print("chaque personne aura", candies_per_person, "bonbons")

#3.4
nombre = [1, 1, 2, 3, 5, 8 ,13]
somme = 0
for i in nombre:
    somme += i

moyenne = somme / len(nombre)
print("moyenne =", moyenne)


#6.5

day1 = 26.82
day2 = 42.00
day3 = 31.41
day4 = 63.7
day5 = 32
days = 5
total= day1 + day2 + day3 + day4 + day5
average = total / days
print("nb de jours", 5)
print("total depense:", total)
print("moyenne depenser par jour:",average)


#3.6
miles = 3
meters = miles * 1609.344

km = meters / 1000

print(round(km, 1))

#3.7
price = 214
tax_rate = 20
tax_fee = price * tax_rate / 100
print("TVA:", tax_fee)

#3.8
price = 271
tax_rate = 20
tax_included_price = price * (1 + tax_rate / 100)

print("prix TTC", tax_included_price)

#3.9

price1 = 1.79
price2 = 1.7
poids1 = 120
poids2 = 100

price_kilo_1 = (price1 / poids1) * 1000
price_kilo_2 = (price2 / poids2) * 1000

print(price_kilo_2 > price_kilo_1)