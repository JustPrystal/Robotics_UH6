"""supervisor controller."""


# Import necessary libraries
from controller import Robot, Supervisor
import math

supervisor = Supervisor()

# Get all nodes
robot_node = supervisor.getFromDef("PlayerBody")
ball_node = supervisor.getFromDef("Ball")
line_node = supervisor.getFromDef("GoalLine")

# Main loop
while supervisor.step(64) != -1:
    # Get the position of the robot
    robot_position = robot_node.getPosition()
    # Get the position of the ball
    ball_position = ball_node.getPosition()
    
    line_position = line_node.getPosition()
    
    # Calculate distance between robot and ball
    distance_robot_ball = round(math.sqrt((robot_position[0] - ball_position[0])**2 + (robot_position[1] - ball_position[1])**2 + (robot_position[2] - ball_position[2])**2),2)
    
    # Subtract sum of radii to account for touching
    robot_half_size = 0.3 / 2  # Half of robot size along any dimension
    ball_radius = 0.05  # Radius of the ball
    distance_robot_ball -= (robot_half_size + ball_radius)
   
    #ensure distance is non negative
    distance_robot_ball = max(0, distance_robot_ball)
   
    # Calculate distance between ball and goal post
    distance_ball_goal_line = round(math.sqrt((ball_position[0] - line_position[0])**2 + (ball_position[1] - line_position[1])**2 + (ball_position[2] - line_position[2])**2),2)
    
    #only X matters when y = 0 
    goal_post_half_x = 0.53 / 2
    goal_post_half_y = 1.5 / 2
    
    #apply pythagoras theorem to get hypotneuse for when y != 0
    goal_calculated_diff = goal_post_half_x
    
    if ball_position[1] != 0:
        goal_calculated_diff = math.sqrt(ball_position[1]**2 + goal_post_half_x**2) #Hypotneuse
    
    distance_ball_goal_line -= (ball_radius + goal_calculated_diff)
    
    #ensure distance is non negative
    distance_ball_goal_line = max(0, distance_ball_goal_line)

    
    # Print the distance between robot and ball
    print("Distance between robot and ball:", distance_robot_ball, " meters")
    # Print the distance between ball and goal line
    print("Distance between ball and goal line:", distance_ball_goal_line, " meters")

    