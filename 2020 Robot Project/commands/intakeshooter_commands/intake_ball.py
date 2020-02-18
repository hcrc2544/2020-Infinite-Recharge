from wpilib.command import Command
from wpilib import DoubleSolenoid, Timer

class Intake_Ball(Command):
    def __init__(self, init_intakeshooter_subsystem):
        super().__init__("intake_ball", subsystem =init_intakeshooter_subsystem)
        self.intake_shooter_subsystem = init_intakeshooter_subsystem
        self.command_timer = Timer()

    def initialize(self):
        #set timers
        self.command_timer.reset()
        self.command_timer.start()

    def execute(self):
        #setting front roller speed to 100%, belt system to 25%
        self.intake_shooter_subsystem.set_intake_speeds(1, 0.25)

        #set front roller to forward
        if self.command_timer.get() < 0.5:
            self.intake_shooter_subsystem.set_front_roller_posistion(DoubleSolenoid.Value.kForward)
        #turn off solenoid signal after a second
        else:
            self.intake_shooter_subsystem.set_front_roller_posistion(DoubleSolenoid.Value.kOff)

        
    def end(self):
        #double check solenoid is off before exiting command
        self.intake_shooter_subsystem.set_front_roller_posistion(DoubleSolenoid.Value.kOff)

    def isFinished(self):
        return False