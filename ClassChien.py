class Chien:
    def __init__(self, race, couleur, poids):
        self.race = race
        self.couleur=couleur
        self.poids=poids

    def Bark(self):
        return 'WOOOF'

c1= Chien('Husky', 'Blanc','20Kg')
print("La race du chien: "+c1.race,"\nLa couleur du chien: "+c1.couleur, "\nLe poids du chien: "+c1.poids)
print(c1.Bark())