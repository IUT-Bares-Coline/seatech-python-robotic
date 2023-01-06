""" 
Exoooooo 1

    Lorsque je crée mon robot, je veux pouvoir lui attribuer un nom
    Mon robot doit pouvoir s'allumer
    Mon robot doit pouvoir s'éteindre
    Mon robot doit pouvoir charger sa batterie à 100%, allumé ou non
    Le temps de charge ne peut pas être immédiat (10s max)
    Mon robot doit afficher sont % de batterie durant sa charge
    Mon robot doit pouvoir enregistrer une vitesse de déplacement
    Mon robot doit pouvoir me donner sa vitesse de déplacement
    Mon robot doit pouvoir arrêter son déplacement sur commande
    Mon robot doit pouvoir me fournir un résumé de son état global

    Une fois terminé, commitez votre code sur Github
    Je jouerai alors avec votre objet pour interagir avec lui

 """
import time

class Robot():
    __name = "<unnamed>"
    __power = False
    __current_speed = 0
    __battery_level = 10
    __states = ['shutdown', 'running']
    positionX = 0
    positionY = 0
        
    """
      Give your best code here ( •̀ ω •́ )✧
    """
    #__slots__ = ('name', 'power')
	
    def __init__(self, name='Jean_Charles', power=False):
        self.__name = name
        self.__power = power

    def donner_nom(self, nom = 'Jean_Charles'):
        self.__name = nom
        pass

    def allumer(self):
        print('Bonjour ! < O_O >')
        self.__power = True 
        self.__states = 'running'
        pass

    def eteindre(self):
        print('Au revoir ! < -_- >')
        self.__power = False
        self.__states = 'shutdown'
        pass

    def charger(self): 
        Affichage_batt = ['-']
        print('Niveau batterie : ')
        batt_a_remplir = int(( 100 - self.__battery_level) / 10)

        for i in range(batt_a_remplir) :
            self.__battery_level +=10
            Affichage_batt.append('-')
            print(''.join(Affichage_batt), self.__battery_level, '%')
            time.sleep(1)

        if(self.__battery_level!=100):
            self.__battery_level = 100
            print(''.join(Affichage_batt), self.__battery_level, '%')
            time.sleep(1)
        print('\n')
        pass
    
    def deplacement(self, direction = 'droite', vitesse = 15):
        if(self.__power == True): 
            if(self.__battery_level > 15):
                if(direction == 'gauche'):
                    self.positionX -= vitesse
                elif (direction == 'droite'):
                    self.positionX += vitesse
                elif(direction == 'devant'):
                    self.positionY += vitesse
                elif (direction == 'derriere'):
                    self.positionY -= vitesse
                
                self.__current_speed = vitesse
                self.__battery_level -= 0.5*vitesse
            pass
        pass

    def vitesse_actuelle(self):
        print('Vitesse actuelle : ', self.__current_speed) 
        pass

    def etat_global(self):
        print('Nom du robot : ', self.__name)
        print('Vitesse du robot : ', self.__current_speed)
        print('Niveau de batterie du robot : ', self.__battery_level)
        print('Etat du robot : ', self.__states)


#MAIN

	
r = Robot()

print('\n///////////Mise en marche du robot///////////\n')
r.allumer()
nom = input('Entrer le nom que vous souhaitez donner au robot : ')
r.donner_nom(nom)


print('\nAVANT CHARGEMENT ET CONSIGNE DE DEPLACEMENT\n')
print('\n///////////Affichage de l état du robot///////////\n')
r.etat_global()


print('\nAVANT CHARGEMENT ET APRES CONSIGNE DE DEPLACEMENT\n')
print('\n///////////Déplacement du robot (direction = gauche et vitesse = 8m/s (Mais en fait non parce que pas de batterie ! :/  )///////////\n')
r.deplacement('gauche',8)

print('\n///////////Affichage de la vitesse du robot///////////\n')
r.vitesse_actuelle()

print('\n///////////Affichage de l état du robot///////////\n')
r.etat_global()


print('\nAPRES CHARGEMENT ET CONSIGNE DE DEPLACEMENT\n')
r.charger()
print('\n///////////Déplacement du robot (direction = gauche et vitesse = 8m/s (et ouais il est rapide le loulou !))///////////\n')
r.deplacement('gauche',8)

print('\n///////////Affichage de la vitesse du robot///////////\n')
r.vitesse_actuelle()

print('\n///////////Affichage de l état du robot///////////\n')
r.etat_global()

print('\n///////////Mise à l arrêt du robot///////////\n')
r.eteindre()

print('\n///////////END OF LIFE///////////\n')