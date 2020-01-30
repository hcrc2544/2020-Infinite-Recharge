from wpilib.command import Command


class Intake_Ball(Command):
    def __init__(self, init_intakeshooter_subsystem):
        self.intake_shooter_subsystem = init_intakeshooter_subsystem

    def execute(self):
        #setting front roller speed to 100%, belt system to 25%
        self.intake_shooter_subsystem.set_intake_speeds(1, 0.25)
    
    def isFinished(self):
        return False