#10.1

def my_sum(a,b) ->int:
    '''
    cette fonction additionne les 2 parametres
    a,b: int 
    retour int somme des deux parametre
    '''
    return a+b

#10.2

def my_diff(a,b) ->int:
    '''
    cette fonction soustrait b de a
    a: int
    b: int
    retour int soustraction de a par b
    '''
    return a-b

print(my_diff(5, 6))

#10.3

def oui_non(bo) ->str:
    '''
    cette fonction renvoie oui si le booleen est True et non si False
    bo: bool
    retour str oui si True, non si False
    '''
    if bo:
        return ("oui")
    return ("non")

#10.4

def is_greater(a,b) ->bool:
    ''''
    cette fonction renvoie True si a est plus grand que b
    a,b: float
    retour: bool renvoie True si a>b sinon False
    '''
    if a>b:
        return True
    return False

#10.5

def compare(a,b) ->int:
    '''
    cette fonction qui compare a et b
    a,b: float
    retour: int renvoie 1 si a >b, 0 si a=b et -1 si a<b
    '''
    if a == b:
        return 0
    elif a>b:
        return 1
    return -1

#10.6

# miles = meters / 1609.344
# meters = miles * 1609.344

def meters_to_miles(meters) -> float:
    miles = meters / 1609.344
    return miles

def miles_to_meters(miles) -> float:
    meters = miles * 1609.344
    return meters

print( meters_to_miles(1000))
print(miles_to_meters(10))

# 10.7

def compute_tax(price, tax_type) ->float:
    '''
    cette fonction calcul le prix TTC
    price: float correspond au prix du produit
    tax_type: int cirrespond au type de taxe 
    retour: float renvoie le prix TTC
    '''
    if tax_type == 1:
        return price *(1+(2.1/100))
    elif tax_type == 2:
        return price *(1+(5.5/100))
    elif tax_type == 3:
        return price *(1+(10/100))
    elif tax_type == 4:
        return price *(1+(20/100))
    else:
        return price

for i in range(0, 5):
    print(compute_tax(100, i))

