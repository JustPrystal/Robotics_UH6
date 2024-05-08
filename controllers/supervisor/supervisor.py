"""supervisor controller."""

# Assuming you are using Python controller in Webots

# Import necessary libraries
from controller import Robot, Supervisor
import math

# Initialize the supervisor to control the simulation
supervisor = Supervisor()

# Get the robot node
robot_node = supervisor.getFromDef("GOALIE")

# Get the ball node
ball_node = supervisor.getFromDef("Ball")

# Get the position of the robot
# robot_position = robot_node.getPosition()
# # Get the position of the ball
# ball_position = ball_node.getPosition()



# Main loop
while supervisor.step(32) != -1:
    # Get the position of the robot
    robot_position = robot_node.getPosition()
    
    # Get the position of the ball
    ball_position = ball_node.getPosition()
    
    # Calculate distance between robot and ball
    distance = math.sqrt((robot_position[0] - ball_position[0])**2 + (robot_position[1] - ball_position[1])**2 + (robot_position[2] - ball_position[2])**2)
    
    # round the distance to 2 decimal places
    distance = round(distance, 2)

    print("Distance between robot and ball:", distance, " meters")

    