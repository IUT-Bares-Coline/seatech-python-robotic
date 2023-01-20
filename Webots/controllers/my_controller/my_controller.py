"""my_controller controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot, Motor, DistanceSensor

# create the Robot instance.
robot = Robot()

# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())

# You should insert a getDevice-like function in order to get the
# instance of a device of the robot. Something like:
#  motor = robot.getDevice('motorname')
#  ds = robot.getDevice('dsname')
#  ds.enable(timestep)

class Moteurs(Motor):
    
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
        self.__moteurGauche.setVelocity(5)
        self.__moteurDroit.setVelocity(-3)
        print('Je tourne à gauche')
    
    def turnDroite(self):
        self.__moteurGauche.setVelocity(-3)
        self.__moteurDroit.setVelocity(5)
        print('Je tourne à droite')



class Capteurs():

    #Numérotation des capteurs de gauche à droite 
    #en se plaçant à la place du robot (pas en face)
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

    print('lecture distance', Avant1)

    def lectureDistance():
        #print('lecture distance', Avant1)
        pass

    


class monRobot(Moteurs, Capteurs) :
    __nom = 'El Destructor'


# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(timestep) != -1:
    # Read the sensors:
    # Enter here functions to read sensor data, like:
    #  val = ds.getValue()

    # Process sensor data here.

    # Enter here functions to send actuator commands, like:
    #  motor.setPosition(10.0)



    Jean_Marc = monRobot()
    Jean_Marc.avancer()
    #Jean_Marc.reculer()
    #Jean_Marc.turnDroite()
    #Jean_Marc.turnGauche()

    pass

# Enter here exit cleanup code.
