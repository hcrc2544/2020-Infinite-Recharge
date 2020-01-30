from wpilib.command import Subsystem
from wpilib import Talon, Encoder
from wpilib.drive import DifferentialDrive
from math import pi

from commands.drive_commands.drive_reserve import Drive_Reserve

class Drive(Subsystem):

    def __init__(self):
        super().__init__("Drive")
        ENCODER_CYCLES_PER_REV = 360
        TIRE_DIAMETER = 6
        ENCODER_DIST_PER_PULSE = (TIRE_DIAMETER * pi / ENCODER_CYCLES_PER_REV)

        self.left_motor = Talon(0)
        self.right_motor = Talon(1)
        self.right_encoder = Encoder(aChannel = 0, bChannel = 1, reverseDirection = False, encodingType = Encoder.EncodingType.k4X)
        self.left_encoder = Encoder(aChannel = 2, bChannel = 3, reverseDirection = True, encodingType = Encoder.EncodingType.k4X)
        self.right_encoder.setDistancePerPulse(ENCODER_DIST_PER_PULSE)
        self.left_encoder.setDistancePerPulse(ENCODER_DIST_PER_PULSE)
        self.drive_controller = DifferentialDrive(self.left_motor, self.right_motor)
    
    def arcade_drive(self, Y , X):
        self.drive_controller.arcadeDrive(Y, X)
        print('Right Encoder value:', self.right_encoder.getDistance(), 'Left Encoder value:', self.left_encoder.getDistance())

    def initDefaultCommand(self):
        self.setDefaultCommand(Drive_Reserve(self))