"""Ball emitter controller."""

from controller import Robot

# create the Robot instance.
robot = Robot()

# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())
ball_emitter = robot.getDevice("ball-emitter")

# Main loop:
while robot.step(timestep) != -1:
    # Send a placeholder signal
    ball_emitter.send("x")