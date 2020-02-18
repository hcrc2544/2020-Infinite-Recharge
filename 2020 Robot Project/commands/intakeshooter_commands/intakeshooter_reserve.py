from wpilib.command import Command
from wpilib import DoubleSolenoid, Timer

class Intake_Shooter_Reserve(Command):
    def __init__(self, init_intakeshooter_subsystem):
        super().__init__("intake_shooter_reserve", subsystem =init_intakeshooter_subsystem)
        self.intake_shooter_subsystem = init_intakeshooter_subsystem
        self.command_timer = Timer()
    def initialize(self):
        #set timers
        self.command_timer.reset()
        self.command_timer.start()

    def execute(self):
        #set front roller motors and belt system to 0
        self.intake_shooter_subsystem.set_intake_speeds(0, 0)

        #set front roller to reverse
        if self.command_timer.get() < 0.5:
            self.intake_shooter_subsystem.set_front_roller_posistion(DoubleSolenoid.Value.kReverse)
        #turn off solenoid signal after a second
        else:
            self.intake_shooter_subsystem.set_front_roller_posistion(DoubleSolenoid.Value.kOff)

    def end(self):
        #double check solenoid is off before exiting command
        self.intake_shooter_subsystem.set_front_roller_posistion(DoubleSolenoid.Value.kOff)
   
    def isFinished(self):
        return False


