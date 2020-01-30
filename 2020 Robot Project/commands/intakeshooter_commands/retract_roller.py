from wpilib.command import Command
from wpilib import DoubleSolenoid
class Retract_Roller(Command):
    def __init__(self, init_intakeshooter_subsystem):
        self.intake_shooter_subsystem = init_intakeshooter_subsystem

    def execute(self):
        self.intake_shooter_subsystem.set_front_roller_posistion(DoubleSolenoid.Value.kReverse)
    def isFinished(self):
        return False