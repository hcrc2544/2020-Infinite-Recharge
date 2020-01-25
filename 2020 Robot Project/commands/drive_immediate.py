from wpilib.command import Command

class Drive_Immediate(Command):
    def __init__(self, init_drive_subsystem, Y, X):
        super().__init__("drive_immediate", timeout=0.05, subsystem=init_drive_subsystem)
        self.drive_subsystem = init_drive_subsystem
        self.y_speed = Y
        self.x_speed = X

    def _execute(self):
        self.drive_subsystem.arcade_drive(self.y_speed, self.x_speed)
    
    def _isFinished(self):
        return False