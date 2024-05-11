from controller import Robot, Keyboard
# Create an instance of the robot
robot = Robot()
keyboard = Keyboard()

# Get the time step of the current world.
timestep = 64
keyboard.enable(timestep)

# Set up motor devices for the wheels
left_motor = robot.getDevice('motor_1') 
right_motor = robot.getDevice('motor_2')

left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))

left_motor.setVelocity(0.0)
right_motor.setVelocity(0.0)

# Set up the maximum motor speed
max_speed = 10  # Adjust as needed

while robot.step(32) != -1:
    key = keyboard.getKey()
    
    if key == 32:  # Check if the spacebar is pressed
        break

# Main loop
while robot.step(timestep) != -1:
    # Read keyboard input
    key = keyboard.getKey()

    if key == ord('W'):
        left_speed = max_speed
        right_speed = max_speed
    elif key == ord('S'):
        left_speed = -max_speed
        right_speed = -max_speed
    elif key == ord('A'):
        left_speed = 0.5 * max_speed
        right_speed = max_speed
    elif key == ord('D'):
        left_speed = max_speed
        right_speed = 0.5 * max_speed
    else:
        left_speed = 0
        right_speed = 0
    
    
    # Set motor speeds
    left_motor.setVelocity(left_speed)
    right_motor.setVelocity(right_speed)