from wpilib.command import Subsystem
from ctre import WPI_TalonSRX
from wpilib import SpeedControllerGroup

class Climber(Subsystem):
    def __init__(self):
        super().__init__("Climber")


    