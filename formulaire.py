class formulaire:
    def __init__(self,nom,prenom,naissance):
        self.nom = nom.upper()
        self.prenom = prenom.upper()
        self.naissance = naissance

    def age(self):
        return 2017-self.naissance

    def majeur(self):
        return self.age() >= 18
    
    def memefamille(self,formulaire):
        return self.nom == formulaire.nom
    
    def memepersonne(self, formulaire):
        return (self.nom == formulaire.nom) & (self.prenom == formulaire.prenom) & (self.naissance == formulaire.naissance)

jd = formulaire ('doe', 'john', 2000)
ad = formulaire ('doe','alice', 1996)
cd = formulaire ('doe','connor', 20011)
pd = formulaire ('doe','patrick', 2010)

my_list = [jd,ad, cd, pd]
#print(jd.majeur())
#print(ad.majeur())
#print(jd.memefamille(ad))
#print(jd.memepersonne(jd))
for i in range(len(my_list)): 
    print(f"{my_list[i].nom}  {my_list[i].prenom}  {my_list[i].naissance}")


#sort by birthdate decroissant
new_list = sorted(my_list, key = lambda formulaire :formulaire.naissance)
#sort by birthdate croissant
#new_list = sorted(my_list, key = lambda formulaire :formulaire.naissance, reverse= True)
print("\nNouveau Formulaire : \n")
for i in range(len(new_list)): 
    print(f"{new_list[i].nom}  {new_list[i].prenom}  {new_list[i].naissance}")

print("Please review my code")