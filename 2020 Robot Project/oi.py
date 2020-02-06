from wpilib import Joystick
from commands.drive_commands.drive_immediate import Drive_Immediate
from commands.intakeshooter_commands import intake_ball, intakeshooter_reserve
from wpilib.command import Scheduler
from wpilib.buttons import JoystickButton



class Operator_Interface():
    def __init__(self, init_robot):
        self.robot = init_robot

        #define joysticks
        self.joystick_left = Joystick(0)
        self.joystick_right = Joystick(1)

        #define joystick buttons
        self.left_trigger = JoystickButton(self.joystick_left, 1)


    
        self.button_intake = intake_ball.Intake_Ball(self.robot.intake_shooter_subsystem)
        self.button_reserve = intakeshooter_reserve.Intake_Shooter_Reserve(self.robot.intake_shooter_subsystem)
    

        #define button commands
        self.left_trigger.whenPressed(self.button_intake)
        self.left_trigger.whenReleased(self.button_reserve)
        
        

    def teleop_update(self):
        #y value is negated to drive in the desired direction
        new_command = Drive_Immediate(self.robot.drive_subsystem, -self.joystick_left.getY(), self.joystick_right.getX())
        Scheduler.getInstance().addCommand(new_command)

        """
        if self.joystick_left.getRawButtonPressed(1):
            self.test_command = Extend_Roller(self.robot.intake_shooter_subsystem)
            Scheduler.getInstance().addCommand(self.test_command)
        elif self.joystick_left.getRawButtonReleased(1):
            self.newtest_command = Retract_Roller(self.robot.intake_shooter_subsystem)
            Scheduler.getInstance().addCommand(self.newtest_command)
        else:
            pass
        """


        
      
    

