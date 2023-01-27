"""my_controller controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot, Motor, DistanceSensor
import time

# You should insert a getDevice-like function in order to get the
# instance of a device of the robot. Something like:
#  motor = robot.getDevice('motorname')
#  ds = robot.getDevice('dsname')
#  ds.enable(timestep)



class MoteurG(Motor):
    
    __moteurGauche = super().__init__('left wheel motor')
    
    
    def moteurGauche(self, vitesse):
        __moteurGauche.setPosition(vitesse)
        
    

class MoteurD(Motor):
    
    __moteurDroit = super().__init__('right wheel motor')
    
    
    def moteurDroit(self, vitesse):
        __moteurDroit.setPosition(vitesse)
        
        

class Moteurs(MoteurG,MoteurD):
    
    __vitesseGauche = 5
    __vitesseDroit = 5
    
    

    def __init__(self):
        self.motG = MoteurG()
        self.motD = MoteurD()
        
        moteurGauche(float('inf'))
        moteurDroit(float('inf'))
        moteurGauche(0)
        moteurDroit(0)

    def avancer(self):
        moteurGauche(5)
        moteurDroit(5)
        print("J'avance")

    def reculer(self):
        moteurGauche(-5)
        moteurDroit(-5)
        print("Je recule")

    def turnGauche(self):
        moteurGauche(-5)
        moteurDroit(5)
        print('Je tourne à gauche')
    
    def turnDroite(self):
        moteurGauche(5)
        moteurDroit(-5)
        print('Je tourne à droite')



class Capteurs():

    #Numérotation des capteurs de gauche à droite 
    #en se plaçant à la place du robot (pas en face)
    
    def __init__(self):
        Avant1 = robot.getDevice('ds13')
        Avant2 = robot.getDevice('ds14')
        Avant3 = robot.getDevice('ds15')
        Avant4 = robot.getDevice('ds0')
        Avant5 = robot.getDevice('ds1')
        Avant6 = robot.getDevice('ds2')
    
        GaucheArriere = robot.getDevice('ds10')
        GaucheAvant = robot.getDevice('ds11')
    
        ArriereGauche = robot.getDevice('ds8')
        ArriereDroit = robot.getDevice('ds7')
    
        DroitArriere = robot.getDevice('ds5')
        DroitAvant = robot.getDevice('ds4')
    
        CoinAvantGauche = robot.getDevice('ds12')
        CoinAvantDroit = robot.getDevice('ds3')
    
        CoinArriereGauche = robot.getDevice('ds9')
        CoinArriereDroit = robot.getDevice('ds6')


class monRobot():
    __nom = 'El Destructor'
    
    def __init__(self):
        self.capt = Capteurs()
        self.mot = Moteurs()
    

# create the Robot instance.
Jean_Marc = monRobot()
timestep = int(Jean_Marc.getBasicTimeStep())


# Main loop:

# - perform simulation steps until Webots is stopping the controller
while Jean_Marc.step(timestep) != -1:
    # Read the sensors:
    # Enter here functions to read sensor data, like:
    #  val = ds.getValue()

    # Process sensor data here.

    # Enter here functions to send actuator commands, like:
    #  motor.setPosition(10.0)
    
    #monRobot.avancer()
    #monRobot.reculer()
    #monRobot.turnDroite()
    #Jean_Marc.turnGauche()
    #time.sleep(5)
    Jean_Marc.avancer()
    #time.sleep(5)

    pass

# Enter here exit cleanup code.
