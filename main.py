'''
Estimates pi using Monte Carlo simulation

Virtual Dartboard has area 2 X 2 to accommodate unit circle
Total area is 4
Therefore, since area of unit circle = pi * radius^2 (and radius of 1 squared
  is 1), ratio of area of unit circle to area of board should be pi/4
  Theoretically, if you fill the entire board with darts, counting
  the number of darts that fall within the circle divided by the
  total number of darts thrown should give us that ratio (i.e., 1/4 * pi)
  Therefore, multiplying that result by 4 should give us an approx. of pi

Output to monitor:
  approximation of pi (float)
Output to window:
  colored dots that simulate unit circle on 2x2 square
Functions you must implement:
  drawSquare(myturtle=None, width=0, top_left_x=0, top_left_y=0) - to outline dartboard
  drawLine(myturtle=None, x_start=0, y_start=0, x_end=0, y_end=0) - to draw axes
  drawCircle(myturtle=None, radius=0) - to draw the circle
  setUpDartboard(myscreen=None, myturtle=None) - to set up the board using the above functions
  isInCircle(myturtle=None, circle_center_x=0, circle_center_y=0, radius=0) - determine if dot is in circle
  throwDart(myturtle=None)
  playDarts(myturtle=None) - a simulated game of darts between two players
  montePi(myturtle=None, num_darts=0) - simulation algorithm returns the approximation of pi
'''
import turtle
import random
import time

#########################################################
#                   Your Code Goes Below                #
#########################################################
"""
drawSquare(myturtle=None, width=0, top_left_x=0, top_left_y=0)  
drawLine(myturtle=None, x_start=0, y_start=0, x_end=0, y_end=0)
drawCircle(myturtle=None, radius=0)
setUpDartboard(myscreen=None, myturtle=None) 
isInCircle(myturtle=None, circle_center_x=0, circle_center_y=0, radius=0)
throwDart(myturtle=None)
playDarts(myturtle=None) 
montePi(myturtle=None, num_darts=0) 
"""
def drawSquare(myturtle=None, width=0, top_left_x=0, top_left_y=0):
  right_angle=90
  myturtle.pu()
  myturtle.goto(top_left_x, top_left_y)
  for i in range(4):
    myturtle.pd()
    myturtle.fd(width)
    myturtle.rt(right_angle)
def drawLine(myturtle=None, x_start=0, y_start=0, x_end=0, y_end=0):
  myturtle.pu()
  myturtle.goto(x_start, y_start)
  myturtle.pd()
  myturtle.goto(x_end, y_end)
def drawCircle(myturtle=None, radius=0):
  myturtle.pd()
  myturtle.circle(radius, None, 100)
def setUpDartboard(myscreen=None, myturtle=None):
  myscreen.setworldcoordinates(-1,-1,1,1)
  drawSquare(myturtle, 2, -1, 1)
  drawLine(myturtle, -1,0,1,0)
  drawLine(myturtle,0,1,0,-1)
  drawCircle(myturtle, 1)
def isInCircle(myturtle=None, circle_center_x=0, circle_center_y=0, radius=0):
  if myturtle.distance(circle_center_x, circle_center_y)<radius:
    myturtle.dot(None, "green")
    return True
  else:
    myturtle.dot(None, "red")
    return False
def throwDart(myturtle=None):
  dart_landing_x= random.uniform(-1,1)
  dart_landing_y= random.uniform(-1,1)
  myturtle.pu()
  myturtle.goto(dart_landing_x, dart_landing_y)
  myturtle.pd()
  myturtle.dot()
  isInCircle(myturtle,0,0,1)
def playDarts(myturtle=None):
  player1_score=0
  player2_score=0
  for games in range(10):
    if throwDart(myturtle)==True:
    #if isInCircle(myturtle,0,0,1)==True:
      player1_score +=1
    if throwDart(myturtle)==True:
    #if isInCircle(myturtle,0,0,1)==True:
      player2_score+=1
  if player1_score==player2_score:
    print("Draw!")
  elif player1_score>player2_score:
    print("player 1 wins!")
  elif player1_score<player2_score:
    print("player 2 wins!")
def montePi(myturtle=None, num_darts=0):
  inside_count=0
  for throws in range(num_darts):
    if throwDart(myturtle)==True:
      inside_count+=1
  return (inside_count/num_darts)*4
  
#########################################################
#         Do not alter any code below here              #
#       Your code must work with the main proivided     #
#########################################################
def main():
    # Get number of darts for simulation from user
    # Note continuation character <\> so we don't go over 78 columns:
    print("This is a program that simulates throwing darts at a dartboard\n" \
        "in order to approximate pi: The ratio of darts in a unit circle\n"\
        "to the total number of darts in a 2X2 square should be\n"\
        "approximately  equal to pi/4")
    print("=========== Part A ===========")

    #Create window, turtle, set up window as dartboard
    window = turtle.Screen()
    darty = turtle.Turtle()
    darty.speed(0) # as fast as it will go!
    setUpDartboard(window, darty)

    # Loop for 10 darts to test your code
    for i in range(10):
        throwDart(darty)
    print("\tPart A Complete...")
    print("=========== Part B ===========")
    darty.clear()
    setUpDartboard(window, darty)
    playDarts(darty)
    print("\tPart B Complete...")
    # Keep the window up until dismissed
    print("=========== Part C ===========")
    darty.clear()
    setUpDartboard(window, darty)
    
    # Includes the following code in order to update animation periodically
    # instead of for each throw (saves LOTS of time):
    BATCH_OF_DARTS = 5000
    window.tracer(BATCH_OF_DARTS)

    # Conduct simulation and print result
    number_darts = int(input("\nPlease input the number of darts to be thrown in the simulation:  "))
    approx_pi = montePi(darty, number_darts)
    print("\nThe estimation of pi using "+str(number_darts)+" virtual darts is " + str(approx_pi))
    print("\tPart C Complete...")
    # Don't hide or mess with window while it's 'working'
    window.exitonclick()

main()
