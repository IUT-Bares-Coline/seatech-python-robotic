from abc import ABCMeta, abstractmethod
import time

""" You can use classes below or create your own 👍️"""

class UnmannedVehicle(metaclass=ABCMeta):
    """ 
        An autonomous vehicle have to do his mission automatically.
        This mission can be configured by an operator.
    """

    @abstractmethod
    def demarrer(self):
        pass

    @abstractmethod
    def mission(self):
        pass    
    
    @abstractmethod
    def config_mission(self):
        pass

    pass


class AerialVehicle(metaclass=ABCMeta):
    """ A vehicle made for ground fields."""

    @abstractmethod
    def decoller(self):
        pass

    @abstractmethod
    def voler(self):
        pass

    @abstractmethod
    def atterir(self):
        pass
          
    pass


class GroundVehicle(metaclass=ABCMeta):
    """ A vehicle made for ground fields."""

    @abstractmethod
    def demarrer2(self):
        pass

    @abstractmethod
    def rouler(self):
        pass

    @abstractmethod
    def arreter(self):
        pass

    pass


class UnderseaVehicle(metaclass=ABCMeta):
    """ A vehicle made for ground fields."""

    @abstractmethod
    def plonger(self):
        pass

    @abstractmethod
    def nager(self):
        pass

    @abstractmethod
    def sortir_eau(self):
        pass

    pass


class UAV(AerialVehicle, UnmannedVehicle):
    """Unmanned Aerial Vehicle"""
    altitude = 0
    destination = 'La Réunion'

    def demarrer(self):
        print("Mise en marche des moteurs de l'UAV.")

    def mission(self):
        print("L'UAV effectue sa mission automatiquement jusqu'à ", self.destination)  
   
    def config_mission(self):
        self.destination = input("Configuration de la mission de l'UAV : \n   Entrer une destination : ")

    def decoller(self):
        self.altitude = 10
        print("Decollage de l'UAV")

    def voler(self):
        if(self.altitude != 10):
            print("Il faut d'abord décoller avant de voler !!!")
        else :
            print("Vol en cours de l'UAV")
            print('----', end='')
            time.sleep(1)
            print('----')
            time.sleep(1)
            print('       |')
            time.sleep(1)
            print('       |')
            time.sleep(1)
            print('       ----')
            time.sleep(1)
            print('           |')
            time.sleep(1)
            print('            ----[o_o]  |> ', self.destination)
            time.sleep(1)

    def atterir(self):
        self.altitude = 0
        print("Atterissage du l'UAV")

    pass


class UUV(UnderseaVehicle, UnmannedVehicle):
    """Unmanned Undersea Vehicle"""
    altitude = 0
    destination = 'La Réunion'

    def demarrer(self):
        print("Mise en marche des moteurs de l'UUV.")

    def mission(self):
        print("L'UUV effectue sa mission automatiquement jusqu'à ", self.destination)    
    
    def config_mission(self):
        self.destination = input("Configuration de la mission de l'UUV : \n   Entrer une destination : ")

    def plonger(self):
        self.altitude = -10
        print("Plongeon de l'UUV")

    def nager(self):
        if(self.altitude != -10):
            print("Il faut d'abord plonger avant de nager !!!")
        else :
            print('L UUV nage')
            print('----', end='')
            time.sleep(1)
            print('----')
            time.sleep(1)
            print('       |')
            time.sleep(1)
            print('       |')
            time.sleep(1)
            print('       ----')
            time.sleep(1)
            print('           |')
            time.sleep(1)
            print('            ----[o_o]  |> ', self.destination)
            time.sleep(1)

    def sortir_eau(self):
        print('Sortie de l eau de l UUV')


class UGV(GroundVehicle, UnmannedVehicle):
    """Unmanned Ground Vehicle"""

    def demarrer(self):
        print("Mise en marche des moteurs de l'UGV.")

    def mission(self):
        print("L'UGV effectue sa mission automatiquement")    
    
    def config_mission(self):
        print('Configuration de la mission de l UGV')

    def demarrer2(self):
        print('Demarrage de l UGV')

    def rouler(self):
        print('L UGV roule')

    def arreter(self):
        print('Arrêt de l UGV')

    pass



if __name__ == "__main__" :
    
    print('///////CREATION DE L UAV/////// \n')
    """
    print ('...', end='')
    time.sleep(1)
    print('CRE', end='')
    time.sleep(1)
    print('ATION', end='')
    time.sleep(1)
    print(' DE ', end='')
    time.sleep(1)
    print("L'UAV", end='')
    time.sleep(1)
    print('...')
    """

    uav = UAV()
    uav.demarrer()
    uav.config_mission()
    uav.mission()
    uav.decoller()
    uav.voler()
    uav.atterir()

    print('\n\n///////CREATION DE L UUV/////// \n')
    uuv = UUV()
    uuv.demarrer()
    uuv.config_mission()
    uuv.mission()
    uuv.plonger()
    uuv.nager()
    uuv.sortir_eau()

    print('\n\n///////CREATION DE L UGV/////// \n')
    ugv = UGV()
    ugv.demarrer()
    ugv.config_mission()
    ugv.mission()
    ugv.demarrer()
    ugv.rouler()
    ugv.arreter()


