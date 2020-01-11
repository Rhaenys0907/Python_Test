#INPUT/WRITING IN A FILE
f= open('Test.txt', 'a')
f.write("\n"+input("Entrez votre nom: "))
f.write("\n"+input("Entrez votre prénom: "))
f.write("\n"+input("Entrez votre age: "))
f.close()