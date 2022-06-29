#12.1

class User:
    "cette classe definit un utilisateur"
    def __init__(self, firstname: str="", lastname: str="", email: str="", newslater: bool=False):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.newslater = newslater

#12.2

user1 = User("Joe", "Dalton", "joe.delton@exemple.com", True)
user2 = User("William", "Dalton", "william.delton@exemple.com", False)
user3 = User("Jack", "Dalton", "jack.delton@exemple.com", False)
user4 = User("Avrel", "Dalton", "Avrel.delton@exemple.com", True)

#12.3

users = [user1, user2, user3, user4]

for use in users:
    if use.newslater:
        print(use.email)

#12.4

class ProductLorem:
    def __init__(self, _name: str="", _price: float=0.0):
        self._name =_name
        self._price = _price

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_price(self):
        return self._price    

    def set_price(self, price):
        self._price = price

#12.5

product1 = ProductLorem()
product1.set_name('foo')
product1.set_price(31.41)

product2 = ProductLorem()
product2.set_name('bar')
product2.set_price(27.18)

product3 = ProductLorem()
product3.set_name('baz')
product3.set_price(16.18)

#12.6

products = [product1 , product2, product3]

for prod in products:
    print(prod.get_name() , prod.get_price())

#12.7

class ProductIpsum:
    def __init__(self, _name: str, price: float=0.0,_tax: float=0.0) -> None:
        self._name = _name
        self.price = price
        self._tax = _tax

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_price(self):
        return self.price

    def set_name(self, newPrice):
        self.price = newPrice

    def get_tax(self):
        return self._tax

    def set_name(self, setTax):
        self._tax = setTax

    def get_tax_fee(self):
        return self.price * (self._tax/100)

    def get_tax_included_price(self):
        return self.get_tax_fee() + self.get_price()


#12.8
# Créez 3 instances de la classe `ProductIpsum` et affectez les valeurs suivantes à ses attributs en utilisant le constructeur :
# - product1
#   - name: Dolor
#   - price: 31,41
#   - tax: 20.0
# - product2
#   - name: Sit
#   - price: 27,18
#   - tax: 10.0
# - product3
#   - name: Amet
#   - price: 16,18
#   - tax: 5.5

# réponse 12.8

product1 = ProductIpsum("Dolor", 31.41, 20.0)
product2 = ProductIpsum("Sit", 27.18, 10.0)
product3 = ProductIpsum("Amet", 16.18, 5.5)




# exo 12.9
# Ajoutez chacune des instances de la classe `ProductIpsum` à une liste nommée `products`
# Utilisez une boucle `for` (type `foreach`) pour afficher le nom, le prix (sans la taxe), la taxe et le prix taxe incluse de chaque produit
# Calculez :
# - la somme du prix des produits sans les taxes
# - la somme du montant des taxes
# - la somme du prix des produits taxes incluses
# Et affichez-en des arrondis à 2 chiffres après la virgule, après la boucle `for`

products = [product1, product2, product3]

somme_price = 0
somme_tax = 0
somme_ttc = 0

for prod in products:
    print(f"name : {prod.get_name()}, prix Ht: {prod.get_price()}, taxe: {prod.get_tax()}, prix TTC: {prod.get_tax_included_price()} ")
    somme_price += prod.get_price()
    somme_tax += (prod.get_tax()*prod.get_price())/100
    somme_ttc += prod.get_tax_included_price()
print("somme prix:",round(somme_price, 2))
print("somme taxe:",round(somme_tax, 2))
print("somme TTC:",round(somme_ttc, 2))
