"""
    Un Cyborg est un mélange d'humain et de robot
    Un humain doit posséder un sexe (H / F)
    Un humain doit pouvoir manger un ou plusieurs aliments
    Un humain doit pouvoir digérer ce qu'il a mangé pas très important, faire en dernier si vous avez le temps
    Réutiliser la class Robot faite dans l'exo 1. Sans copier/coller dans le fichier please ;)
    Bonus : ajouter une méthode fun au Cyborg
"""

from exo1 import Robot

class Human():   
    # Human class content here
    __sexe = ''
    __nourriture = []
    __nourriture_digeree = 0

    def __init__(self, sexe = 'femme', nourriture = ['pomme de terre', 'fromage', 'charcuterie'] ):
      self.__sexe = sexe
      self.__nourriture = nourriture
      self.__nourriture_digeree = 10-len(nourriture)

    def manger(self,nourriture):
        self.__nourriture.extend(nourriture) 
        self.__nourriture_digeree -= len(nourriture)
    
    def digerer(self, digestion):
        if(self.__nourriture_digeree + digestion < 10):
            self.__nourriture_digeree += digestion
            for i in range(digestion):
                del self.__nourriture[0]
        else :
            self.__nourriture_digeree = 10
            self.__nourriture = []
        pass
    
    def affiche_etat(self):
        print("sexe : ", self.__sexe, "\nnourriture : ", self.__nourriture, "\nnourriture_digeree (/10): ", self.__nourriture_digeree,'')


class Cyborg(Robot, Human):   #name = 'gertrude', power = 'False')

    def __init__(self, name = 'Martin', sexe = 'homme'):   
        Robot.__init__(self, name)
        Human.__init__(self, sexe)
        #super().__init__(name, power)

    def methode_fun(self):
        print("Retour fun de la methode fun")

    def etat_global(self):
        Robot.etat_global(self)
        Human.affiche_etat(self)

"""
cyborg = Cyborg('Deux Ex Machina', 'M')

print(cyborg.name, 'sexe', cyborg.sexe)
print('Charging battery...')
cyborg.charger()
cyborg.etat_global()
cyborg.manger('banana')
cyborg.manger(['coca', 'chips'])
cyborg.digerer(10)
print('teeeeeeeeest')
"""


humain = Human()
print('------------------------------\nNOUVEL HUMAIN CREE : \n')
humain.affiche_etat()
print('------------------------------')
humain.digerer(2)
humain.affiche_etat()
print('------------------------------')
humain.manger(['carotte'])
humain.affiche_etat()


cyborg = Cyborg()
print('\n------------------------------\nNOUVEAU CYBORG CREE : \n')
cyborg.affiche_etat()
print('------------------------------')
cyborg.etat_global()
