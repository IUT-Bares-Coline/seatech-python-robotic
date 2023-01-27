"""my_controller controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot, Motor, DistanceSensor, GPS
import time

# create the Robot instance.
robot = Robot()

# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())

# You should insert a getDevice-like function in order to get the
# instance of a device of the robot. Something like:
#  motor = robot.getDevice('motorname')
#  ds = robot.getDevice('dsname')
#  ds.enable(timestep)

class mon_GPS(GPS):
    def __init__(self):
        super().__init__('gps')
    
    def ex_fonction():
        pass


class Moteurs():
    
    __vitesseGauche = 5
    __vitesseDroit = 5
    __moteurGauche = robot.getDevice('left wheel motor')
    __moteurDroit = robot.getDevice('right wheel motor')

    def __init__(self):
        self.__moteurGauche.setPosition(float('inf'))
        self.__moteurDroit.setPosition(float('inf'))
        self.__moteurGauche.setVelocity(0)
        self.__moteurDroit.setVelocity(0)

    def avancer(self):
        self.__moteurGauche.setVelocity(5)
        self.__moteurDroit.setVelocity(5)
        print("J'avance")

    def reculer(self):
        self.__moteurGauche.setVelocity(-5)
        self.__moteurDroit.setVelocity(-5)
        print("Je recule")

    def turnGauche(self):
        self.__moteurGauche.setVelocity(-5)
        self.__moteurDroit.setVelocity(5)
        print('Je tourne à gauche')
    
    def turnDroite(self):
        self.__moteurGauche.setVelocity(5)
        self.__moteurDroit.setVelocity(-5)
        print('Je tourne à droite')



class Capteurs():

    #Numérotation des capteurs de gauche à droite 
    #en se plaçant à la place du robot (pas en face)
    listeDistances = []
    

    def __init__(self):
        self.Avant1 = DistanceSensor('ds13')
        self.Avant1.enable(timestep) 

        self.Avant2 = DistanceSensor('ds14')
        self.Avant2.enable(timestep) 

        self.Avant3 = DistanceSensor('ds15')
        self.Avant3.enable(timestep) 

        self.Avant4 = DistanceSensor('ds0')
        self.Avant4.enable(timestep) 

        self.Avant5 = DistanceSensor('ds1')
        self.Avant5.enable(timestep) 

        self.Avant6 = DistanceSensor('ds2')
        self.Avant6.enable(timestep) 

        self.GaucheArriere = DistanceSensor('ds10')
        self.GaucheArriere.enable(timestep) 

        self.GaucheAvant = DistanceSensor('ds11')
        self.GaucheAvant.enable(timestep) 

        self.ArriereGauche = DistanceSensor('ds8')
        self.ArriereGauche.enable(timestep) 

        self.ArriereDroit = DistanceSensor('ds7')
        self.ArriereDroit.enable(timestep) 

        self.DroitArriere = DistanceSensor('ds5')
        self.DroitArriere.enable(timestep) 

        self.DroitAvant = DistanceSensor('ds4')
        self.DroitAvant.enable(timestep) 

        self.CoinAvantGauche = DistanceSensor('ds12')
        self.CoinAvantGauche.enable(timestep) 

        self.CoinAvantDroit = DistanceSensor('ds3')
        self.CoinAvantDroit.enable(timestep) 

        self.CoinArriereGauche = DistanceSensor('ds9')
        self.CoinArriereGauche.enable(timestep) 

        self.CoinArriereDroit = DistanceSensor('ds6')
        self.CoinArriereDroit.enable(timestep) 



    def lectureDistances(self):
        self.listeDistances = []
        self.listeDistances.append(self.Avant1.getValue()) #listeDistances[0] //AVANT
        self.listeDistances.append(self.Avant2.getValue()) #listeDistances[1] //AVANT
        self.listeDistances.append(self.Avant3.getValue()) #listeDistances[2] //AVANT
        self.listeDistances.append(self.Avant4.getValue()) #listeDistances[3] //AVANT
        self.listeDistances.append(self.Avant5.getValue()) #listeDistances[4] //AVANT
        self.listeDistances.append(self.Avant6.getValue()) #listeDistances[5] //AVANT
        self.listeDistances.append(self.GaucheArriere.getValue()) #listeDistances[6] //GAUCHE
        self.listeDistances.append(self.GaucheAvant.getValue()) #listeDistances[7] //GAUCHE
        self.listeDistances.append(self.ArriereGauche.getValue()) #listeDistances[8] //ARRIERE
        self.listeDistances.append(self.ArriereDroit.getValue()) #listeDistances[9] //ARRIERE
        self.listeDistances.append(self.DroitArriere.getValue()) #listeDistances[10] //DROIT
        self.listeDistances.append(self.DroitAvant.getValue()) #listeDistances[11] //DROIT
        self.listeDistances.append(self.CoinAvantGauche.getValue()) #listeDistances[12] //AVANT
        self.listeDistances.append(self.CoinAvantDroit.getValue()) #listeDistances[13] //AVANT
        self.listeDistances.append(self.CoinArriereGauche.getValue()) #listeDistances[14] //ARRIERE
        self.listeDistances.append(self.CoinArriereDroit.getValue()) #listeDistances[15] /ARRIERE
        
        
        return self.listeDistances 
        
    
    
    def retourMinDistance(self):
        
        liste = self.lectureDistances()
        valeur_max = 0
        #indice = 0

        for i in range(len(liste)): #+ la distance est petite, + le nombre est grand
            if (liste[i] > valeur_max):
                valeur_max = liste[i]
                indice = i

                
        print('\nindice : ',indice)
        print('\nValeur distance min : ', valeur_max)

        if(indice==0 or indice==1 or indice==2 or indice==3 or indice==4 or indice==5 or indice==12 or indice==13):
           print('je suis censé avancer')
           return "avance"
        else  :
            if(indice==6 or indice==7):
                return "gauche"
            else :
                if(indice==8 or indice==9 or indice==14 or indice==15):
                    return "recule"
                else :
                    if(indice==10 or indice==11):
                        return "droite"

            
    
    
class monRobot(Moteurs) :
    __nom = 'El Destructor'
    
    def __init__(self):
        self.capt = Capteurs()
        self.mot = Moteurs()
        self.avancer()
        
    def run(self):
        retourDist = self.capt.retourMinDistance()
        if(retourDist == "avance"):
            self.avancer()
        else :
            if(retourDist == "recule"):
                self.reculer()
            else :
                if(retourDist == "gauche"):
                    self.turnGauche()
                    time.sleep(5)
                    self.avancer()
                else :
                    if(retourDist == "droite"):
                        self.turnDroite()
                    time.sleep(5)
                    self.avancer()

            
    
    
        

Jean_Marc = monRobot()
# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(timestep) != -1:
    # Read the sensors:
    # Enter here functions to read sensor data, like:
    #  val = ds.getValue()

    # Process sensor data here.

    # Enter here functions to send actuator commands, like:
    #  motor.setPosition(10.0)
    
    
    #monRobot.reculer()
    #monRobot.turnDroite()
    #Jean_Marc.turnGauche()
    
    Jean_Marc.run()
    

    pass

# Enter here exit cleanup code.
