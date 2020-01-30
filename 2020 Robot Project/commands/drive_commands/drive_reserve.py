from wpilib.command import Command


class Drive_Reserve(Command):
    def __init__(self, drive_subsystem):
        super().__init__("drive_reserve", subsystem=drive_subsystem)
        self.drive_subsystem = drive_subsystem

    def execute(self):
        self.drive_subsystem.arcade_drive(0,0)

    def isFinished(self):
        return False