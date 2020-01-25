from wpilib import Joystick
from commands.drive_immediate import Drive_Immediate
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


