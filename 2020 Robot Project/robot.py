from commandbased import CommandBasedRobot
from subsystems import drive, intake_shooter, climber
from oi import Operator_Interface
from wpilib import run
import ptvsd

class Robot(CommandBasedRobot):
    def __init__(self):
        super().__init__()
        ptvsd.enable_attach(address=('0.0.0.0', 5678), redirect_output = True)
        # ptvsd.wait_for_attach()

        #define subsystems
        self.drive_subsystem = drive.Drive()
        self.intake_shooter_subsystem = intake_shooter.IntakeShooter()
        self.climber_subsystem = climber.Climber()

        self.oi = Operator_Interface(self)

    def teleopPeriodic(self):
        self.oi.teleop_update()
        super().teleopPeriodic()

if __name__ == "__main__":
    run(Robot)