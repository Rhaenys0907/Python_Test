class RemplirInfo:
    def info(self):
        myfile = open('info.txt', 'w')
        nom = input("Votre nom: ")
        prénom = input("Votre prénom: ")
        age = input("Votre age: ")
        myfile.write(nom)
        myfile.write("\n"+prénom)
        myfile.write("\n"+age)
        myfile.close()
    def modif(self, x , y):
        myfile = open('info.txt', 'r')
        data = myfile.read()
        data = data.replace(x, y)
        myfile.close()
        myfile = open('info.txt', 'w')
        myfile.write(data)
        myfile.close()
    def lire(self):
        myfile = open('info.txt', 'r')
        print(myfile.read())
        myfile.close()


R1 = RemplirInfo()
print(R1.info())
R1.modif("Luke", "Annakin")
R1.lire()

