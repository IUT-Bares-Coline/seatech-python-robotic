from abc import ABCMeta, abstractmethod

""" You can use classes below or create your own 👍️"""

class UnmannedVehicle(metaclass=ABCMeta):
    """ 
        An autonomous vehicle have to do his mission automatically.
        This mission can be configured by an operator.
    """

    @abstractmethod
    def avancer(self):
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
    def Demarrer(self):
        pass

    @abstractmethod
    def Rouler(self):
        pass

    @abstractmethod
    def Arreter(self):
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
    def avancer(self):
        print('L UAV avance')

    def mission(self):
        print('L UAV effectue sa mission automatiquement')    
    
    def config_mission(self):
        print('Configuration de la mission de l UAV')

    def decoller(self):
        print('Decollage de l UAV')

    def voler(self):
        print('Vol en cours de l UAV')

    def atterir(self):
        print('Atterissage du l UAV')

    pass


class UUV(UnderseaVehicle, UnmannedVehicle):
    """Unmanned Undersea Vehicle"""

    def avancer(self):
        print('L UUV avance')

    def mission(self):
        print('L UUV effectue sa mission automatiquement')    
    
    def config_mission(self):
        print('Configuration de la mission de l UUV')

    pass


class UGV(GroundVehicle, UnmannedVehicle):
    """Unmanned Ground Vehicle"""

    def avancer(self):
        print('L UGV avance')

    def mission(self):
        print('L UGV effectue sa mission automatiquement')    
    
    def config_mission(self):
        print('Configuration de la mission de l UUGV')

    pass


uav = UAV(UnmannedVehicle)
uav.do_something_interesting()
uav.do_something_aerial_specific()

ugv = UGV()
ugv.do_something_interesting()
ugv.do_something_ground_specific()

uuv = UUV()
uuv.do_something_interesting()
uuv.do_something_undersea_specific()
