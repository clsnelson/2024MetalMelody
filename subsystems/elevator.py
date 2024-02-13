import phoenix6
from constants import * 
from commands2 import Subsystem
import wpilib

class Elevator(Subsystem):
    
    def __init__(self):
        super().__init__()
        self.elevatorMotor = phoenix6.hardware.TalonFX(MotorIDs.ELEVATORMOTOR)
        elevator_config = phoenix6.configs.TalonFXConfiguration()
        elevator_config.slot0.with_k_p(ElevatorConstants.kP)
        elevator_config.motion_magic.with_motion_magic_acceleration(ElevatorConstants.MOTIONMAGICACCELERATION).with_motion_magic_cruise_velocity(ElevatorConstants.MOTIONMAGICVELOCITY).with_motion_magic_jerk(ElevatorConstants.MOTIONMAGICJERK)
        elevator_config.current_limits.supply_current_limit = ElevatorConstants.CURRENTSUPPLYLIMIT
        elevator_config.current_limits.supply_current_limit_enable = ElevatorConstants.CURRENTSUPPLYLIMIT
        self.elevatorMotor.configurator.apply(elevator_config)
        
        self.stage = 0

    def periodic(self) -> None:
        wpilib.SmartDashboard.putNumber("Stage", self.stage)
        self.elevatorMotor.set_control(phoenix6.controls.MotionMagicDutyCycle(ElevatorConstants.ELEVATORPOS[self.stage]))

    def togglePosition(self) -> None:
        self.setStage((self.stage + 1) % 3)
        
    def setStage(self, stage: int) -> None:
        self.stage = stage
    