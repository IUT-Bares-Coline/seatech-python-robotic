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


class Robot():
    __name = "<unnamed>"
    __power = False
    __current_speed = 0
    __battery_level = 0
    __states = ['shutdown', 'running']
    
        
    """
      Give your best code here ( •̀ ω •́ )✧
    """

    def donner_nom(self, nom):
        __name = nom
        pass

    def allumer(self):
        print('Bonjour ! < O_O >')
        __power = True 
        #__states =
        pass

    def eteindre(self):
        print('Au revoir ! < -_- >')
        __power = False
        #__states =
        pass

    def charger(self): 
        for i in 10 :
            __battery_level +=1
            print('Niveau batterie : ', __battery_level)
            #attendre 1s
        pass

    def deplacement(self, direction):
        if(direction == 'gauche'):
            positionX -= 15
        elif (direction == 'droite'):
            positionX += 15
        elif(direction == 'devant'):
            positionY += 15
        elif (direction == 'derriere'):
            positionY -= 15