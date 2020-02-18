from wpilib.command import Subsystem
from wpilib import Talon, Encoder, SpeedControllerGroup
from wpilib.drive import DifferentialDrive
from math import pi
from rev import CANSparkMax, MotorType, CANEncoder

from commands.drive_commands.drive_reserve import Drive_Reserve

class Drive(Subsystem):

    def __init__(self):
        super().__init__("Drive")
        GEAR_RATIO = 10.71
        ENCODER_CYCLES_PER_REV = 1
        TIRE_DIAMETER = 6

        ENCODER_DIST_PER_PULSE = (TIRE_DIAMETER * pi / (ENCODER_CYCLES_PER_REV* GEAR_RATIO))
        

        self.frontLeft = CANSparkMax(1, MotorType.kBrushless)
        self.rearLeft = CANSparkMax(2, MotorType.kBrushless)
        self.left_drive = SpeedControllerGroup(self.frontLeft, self.rearLeft)
        
        self.frontRight = CANSparkMax(3, MotorType.kBrushless)
        self.rearRight = CANSparkMax(4, MotorType.kBrushless)
        self.right_drive = SpeedControllerGroup(self.frontRight, self.rearRight)

        self.right_encoder: CANEncoder = self.frontRight.getEncoder()
        self.left_encoder: CANEncoder = self.frontLeft.getEncoder() 
        self.right_encoder.setPositionConversionFactor(ENCODER_DIST_PER_PULSE)
        self.left_encoder.setPositionConversionFactor(ENCODER_DIST_PER_PULSE)

        self.drive_controller = DifferentialDrive(self.left_drive, self.right_drive)
    
    def arcade_drive(self, Y , X):
        self.drive_controller.arcadeDrive(Y, X)
        #print('Right Encoder value:', self.right_encoder.getDistance(), 'Left Encoder value:', self.left_encoder.getDistance())

    def initDefaultCommand(self):
        self.setDefaultCommand(Drive_Reserve(self))