# This program draws the stars of the Orion constellation,
# the names of the stars, and the constellation lines.
import turtle

# Set the window size.
turtle.setup(500,600)

# setup the turtle.
turtle.penup()
turtle.hideturtle()

# Create named constants for the star coordinates.
LEFT_SHOULDER_X = -70
LEFT_SHOULDER_Y = 200

RIGHT_SHOULDER_X = 80
RIGHT_SHOULDER_Y = 180

LEFT_BELTSTAR_X = -40
LEFT_BELTSTAR_Y = -20

MIDDLE_BELSTAR_X = 0
MIDDLE_BELTSTAR_Y = 0

RIGHT_BELTSTAR_X = 40
RIGHT_BELTSTAR_Y = 20

LEFT_KNEE_X = -90
LEFT_KNEE_Y = -180

RIGHT_KNEE_X = 120
RIGHT_KNEE_Y = -140

# Draw the stars
turtle.goto(LEFT_SHOULDER_X, LEFT_SHOULDER_Y) # Left shoulder
turtle.dot()
turtle.goto(RIGHT_SHOULDER_X, RIGHT_SHOULDER_Y) #Right shoulder
turtle.dot()
turtle.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y) # Left belt star
turtle.dot()
turtle.goto(MIDDLE_BELSTAR_X, MIDDLE_BELTSTAR_Y) # Middle belt star
turtle.dot()
turtle.goto(RIGHT_BELTSTAR_X, RIGHT_BELTSTAR_Y) # Right belt star
turtle.dot()
turtle.goto(LEFT_KNEE_X, LEFT_KNEE_Y) # Left knee
turtle.dot()
turtle.goto(RIGHT_KNEE_X, RIGHT_KNEE_Y) # Right knee
turtle.dot()

# Display the star names
turtle.goto(LEFT_SHOULDER_X, LEFT_SHOULDER_Y) # Left shoulder
turtle.write('Betegeuse')
turtle.goto(RIGHT_SHOULDER_X, RIGHT_SHOULDER_Y) # Right shoulder
turtle.write('Meissa')
turtle.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y) # Left belt star
turtle.write('Alnitik')
turtle.goto(MIDDLE_BELSTAR_X, MIDDLE_BELTSTAR_Y) # Middle belt star
turtle.write('Alnilm')
turtle.goto(RIGHT_BELTSTAR_X, RIGHT_BELTSTAR_Y) # Right belt star
turtle.write('Mintaka')
turtle.goto(LEFT_KNEE_X, LEFT_KNEE_Y) # Left knee
turtle.write('Saiph')
turtle. goto(RIGHT_KNEE_X, RIGHT_KNEE_Y) # Right knee
turtle.write('Rigel')

# Draw a line from the left shoulder to left belt star
turtle.goto(LEFT_SHOULDER_X, LEFT_SHOULDER_Y)
turtle.pendown()
turtle.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y)
turtle.penup()