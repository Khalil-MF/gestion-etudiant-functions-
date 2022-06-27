#declaration des variables
n= int(input("Entrer le nombre des etudiants: "))
T=[]    
#definition des fonctions   
def show_menu():
    print ("\n------Gestion des Etudiants-------")
    print ("------------------------------")
    print ("1.ajouter un etudiant")
    print ("2.afficher etudiant par element")
    print ("3.supprimer un etudiant")
    print ("4.sauvegarder")
    print ("5.Exit\n")

def ajouterEtudiant():
    etudiant={}  
    etudiant["numero"]= int(input("numero :"))   
    etudiant["nom"]=input("nom :")
    etudiant["note"]=float(input("note :"))
    T.append(etudiant)
def afficherEtudiantIndex():
    for i in range(n):
        print("numero: ", T[i]["numero"])
        print("nom: ", T[i]["nom"])
        print("note: ", T[i]["note"])
def afficherEtudiantElement():
    for etudiant in T:
        print("numero: ", etudiant["numero"])
        print("nom: ", etudiant["nom"])
        print("note: ", etudiant["note"])       
def supprimerEtudiant():
    num = int(input("numero a supprimer: "))
    for etudiant in T:
        if etudiant["numero"]==num :
            T.remove(etudiant)
            break
def sauvegarder():
    fichier = open('D:/etudiant.txt', 'a')
    for etudiant in T:
        s= "numero: "+str(T[i]["numero"])+"nom: "+str(T[i]["nom"])+"\n"
        fichier.write(s)
    fichier.close()
def menu():   
    while True:
        show_menu()
        choice = input('Votre choix: ').lower()
        if choice == '1':
            ajouterEtudiant()            
        elif choice == '2':
            afficherEtudiantElement()
        elif choice == '3':
            supprimerEtudiant()
        elif choice == '4':
            sauvegarder()
        elif choice == '5':
            return
        else:
            print("valeur incorrecte, reessayer!!")
        
    
menu()
