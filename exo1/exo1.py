"""my_controller controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot, Motor, DistanceSensor


# get the time step of the current world.
#

# You should insert a getDevice-like function in order to get the
# instance of a device of the robot. Something like:
#  motor = DistanceSensor('motorname')
#  ds = DistanceSensor('dsname')
#  ds.enable(timestep)
    

class Moteurs():
    
    __vitesseGauche = 5
    __vitesseDroit = 5
    __moteurGauche = Motor('left wheel motor')
    __moteurDroit = Motor('right wheel motor')

    def __init__(self):
        self.__moteurGauche.setPosition(float('inf'))
        self.__moteurDroit.setPosition(float('inf'))
        self.__moteurGauche.setVelocity(0)
        self.__moteurDroit.setVelocity(0)

    def avancer(self):
        self.__moteurGauche.setVelocity(15)
        self.__moteurDroit.setVelocity(15)
        print("J'avance")

    def reculer(self):
        self.__moteurGauche.setVelocity(-15)
        self.__moteurDroit.setVelocity(-15)
        print("Je recule")

    def turnGauche(self):
        self.__moteurGauche.setVelocity(15)
        self.__moteurDroit.setVelocity(-10)
        print('Je tourne à gauche')
    
    def turnDroite(self):
        self.__moteurGauche.setVelocity(-10)
        self.__moteurDroit.setVelocity(15)
        print('Je tourne à droite')



class Capteurs():

    #Numérotation des capteurs de gauche à droite 
    #en se plaçant à la place du robot (pas en face)
    
    def __init__(self):
        self.Avant1 = DistanceSensor('ds13')
        self.Avant2 = DistanceSensor('ds14')
        self.Avant3 = DistanceSensor('ds15')
        self.Avant4 = DistanceSensor('ds0')
        self.Avant5 = DistanceSensor('ds1')
        self.Avant6 = DistanceSensor('ds2')

        self.GaucheArriere = DistanceSensor('ds10')
        self.GaucheAvant = DistanceSensor('ds11')

        self.ArriereGauche = DistanceSensor('ds8')
        self.ArriereDroit = DistanceSensor('ds7')

        self.DroitArriere = DistanceSensor('ds5')
        self.DroitAvant = DistanceSensor('ds4')

        self.CoinAvantGauche = DistanceSensor('ds12')
        self.CoinAvantDroit = DistanceSensor('ds3')

        self.CoinArriereGauche = DistanceSensor('ds9')
        self.CoinArriereDroit = DistanceSensor('ds6')

        self.print('lecture distance', self.Avant1)



    def plusCourteDistance():
        
        #retourne le capteur avec la distance la plus courte / la direction
        pass

    


class monRobot(Robot) :
    __nom = 'El Destructor'

    def __init__(self):
        self.__motors = Moteurs()

    def AvancerVersAdversaire(self):
        #recuperer distance la plus courte des capteurs et avancer dans cette direction 
        """
        if(gauche 1 ou gauche 2 plus court) :
            self.__motors.turnGauche()
        else:
            if(////droit 1 ou droit2 plus court):
                self.__motors.turnDroite()
        else:
            if(////avant 1 ou avant2 ou avant3 etc plus court):
                self.__motors.avancer()
        """
        pass





# Main loop:
# - perform simulation steps until Webots is stopping the controller

Jean_Marc = monRobot()
timestep = int(Jean_Marc.getBasicTimeStep())

while Jean_Marc.step(timestep) != -1:
    # Read the sensors:
    # Enter here functions to read sensor data, like:
    #  val = ds.getValue()

    # Process sensor data here.

    # Enter here functions to send actuator commands, like:
    #  motor.setPosition(10.0)



    
    Jean_Marc.jouer()
    #Jean_Marc.reculer()
    #Jean_Marc.turnDroite()
    #Jean_Marc.turnGauche()

    pass

# Enter here exit cleanup code.
