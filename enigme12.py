# Un artilleur dispose de boulets de canon répartis dans un carré parfait. Pour
# réduire l'encombrement au sol, l'artilleur réussit à empiler ses boulets pour former
# une belle pyramide à base carrée.
# Quel est le plus petit nombre de boulets possible dont dispose l'artilleur ?

def boulet_pyramide():
    # carre avec ttes les boules au sol
    for i in [n ** 2 for n in range(3000)]:
        boulet_restant = i
        # soustrait le nb de boulet par etage
        for couche in range(1, i):
            boulet_restant -= couche ** 2
            if boulet_restant == 0:
                print(couche, "carre empiler")
                print("carre de début ", i ** (1/2), "^2")
                return i
            if boulet_restant < 0:
                # quitte la boucle "for couche in range(1, i):" lorsque les boulets restant sont negatif
                break

print(boulet_pyramide())