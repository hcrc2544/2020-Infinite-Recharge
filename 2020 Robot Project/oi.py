from wpilib import Joystick
from commands.drive_commands.drive_immediate import Drive_Immediate
from commands.intakeshooter_commands.extend_roller import Extend_Roller
from commands.intakeshooter_commands.retract_roller import Retract_Roller
from wpilib.command import Scheduler



class Operator_Interface():
    def __init__(self, init_robot):
        self.robot = init_robot
        self.joystick_left = Joystick(0)
        self.joystick_right = Joystick(1)

    def teleop_update(self):
        #y value is negated to drive in the desired direction
        new_command = Drive_Immediate(self.robot.drive_subsystem, -self.joystick_left.getY(), self.joystick_right.getX())
        Scheduler.getInstance().addCommand(new_command)
        '''
        if self.joystick_left.getRawButton(2):
           Extend_Roller(self.robot.intake_shooter_subsystem)

        elif self.joystick_left.getRawButton(3):
            Retract_Roller(self.robot.intake_shooter_subsystem)
    
        else:
            pass
        '''

