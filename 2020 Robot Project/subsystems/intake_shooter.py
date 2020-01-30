from wpilib.command import Subsystem
from ctre import WPI_TalonSRX
from wpilib import SpeedControllerGroup, DoubleSolenoid


class IntakeShooter(Subsystem): 

    def __init__(self):
        super().__init__("IntakeShooter")

        #motor reference may need inverted 
        self.front_roller_motor = WPI_TalonSRX(0)

        self.left_horizontal_motor = WPI_TalonSRX(1)
        self.right_horizontal_motor = WPI_TalonSRX(2)

        self.left_vertical_motor = WPI_TalonSRX(3)
        self.right_vertical_motor = WPI_TalonSRX(4)
        
        self.front_roller_solenoid = DoubleSolenoid(0, 1)
      

        self.horizontal_belts = SpeedControllerGroup(self.left_horizontal_motor, 
            self.right_horizontal_motor)
        self.vertical_belts = SpeedControllerGroup(self.left_vertical_motor,
            self.right_vertical_motor)



    def set_intake_speeds(self, front_roller_speed, belt_speed):
        self.front_roller_motor.set(front_roller_speed)
        self.horizontal_belts.set(belt_speed)
        self.vertical_belts.set(belt_speed)
        
    def set_front_roller_posistion(self, solenoid_state: DoubleSolenoid.Value):
        self.front_roller_solenoid.set(solenoid_state)

    
    



    '''
    def initDefaultCommand(self):
    '''

