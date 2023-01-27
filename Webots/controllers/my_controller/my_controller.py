"""my_controller controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot, Motor, DistanceSensor
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
        self.Avant1 = self.getDevice('ds13') #DistanceSensor('ds13') 
        self.Avant1.enable(timestep) 

    def lectureDistances(self):
        self.listeDistances.append(self.Avant1.getValue())
        print(self.Avant1.getValue())
        """
        self.Avant2 = DistanceSensor('ds14')
        self.listeDistances.append(self.Avant2.getValue())

        self.Avant3 = DistanceSensor('ds15')
        self.listeDistances.append(self.Avant3.getValue())
        
        self.Avant4 = DistanceSensor('ds0')
        self.listeDistances[3] = self.Avant4.getValue()

        self.Avant5 = DistanceSensor('ds1')
        self.listeDistances[4] = self.Avant5.getValue()

        self.Avant6 = DistanceSensor('ds2')
        self.listeDistances[5] = self.Avant6.getValue()
    
        self.GaucheArriere = DistanceSensor('ds10')
        self.listeDistances[6] = self.GaucheArriere.getValue()

        self.GaucheAvant = DistanceSensor('ds11')
        self.listeDistances[7] = self.GaucheAvant.getValue()        
    
        self.ArriereGauche = DistanceSensor('ds8')
        self.listeDistances[8] = self.ArriereGauche.getValue()

        self.ArriereDroit = DistanceSensor('ds7')
        self.listeDistances[9] = self.ArriereDroit.getValue()
    
        self.DroitArriere = DistanceSensor('ds5')
        self.listeDistances[10] = self.DroitArriere.getValue()

        self.DroitAvant = DistanceSensor('ds4')
        self.listeDistances[11] = self.DroitAvant.getValue()
    
        self.CoinAvantGauche = DistanceSensor('ds12')
        self.listeDistances[12] = self.CoinAvantGauche.getValue()

        self.CoinAvantDroit = DistanceSensor('ds3')
        self.listeDistances[13] = self.CoinAvantDroit.getValue()
    
        self.CoinArriereGauche = DistanceSensor('ds9')
        self.listeDistances[14] = self.CoinArriereGauche.getValue()

        self.CoinArriereDroit = DistanceSensor('ds6')
        self.listeDistances[15] = self.CoinArriereDroit.getValue()
        """
        
        
        
        return self.listeDistances 
        
    
    
    def retourMinDistance(self):
        
        liste = self.lectureDistances()
        #print(liste)
        #distMax = min(liste)
            
    
    
class monRobot(Moteurs) :
    __nom = 'El Destructor'
    
    def __init__(self):
        self.capt = Capteurs()
        self.mot = Moteurs()
        
    def run(self):
        #self.avancer()
        self.capt.retourMinDistance()
            
    
    
        

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
