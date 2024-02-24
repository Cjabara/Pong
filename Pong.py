import turtle 
screen=turtle.Screen()
screen.title("Pong")
screen.setup(500, 500)
screen.bgcolor("black")
paddleL = 30
paddleW = 5
pointsLeft = 0
pointsRight = 0 
pongstart = 150
t = turtle.Turtle()
t.shape("square")
t.color("white")
t.speed(10)
t.penup()
t.hideturtle()

def paddlemake(l, w, turt,localx,localy):
  turt.goto(localx,localy)
  turt.fillcolor("white")
  t.pendown()
  turt.begin_fill()
  turt.setheading(0)
  turt.forward(w)
  turt.left(90)
  turt.forward(l)
  turt.left(90)
  turt.forward(w)
  turt.left(90)
  turt.forward(l)
  turt.end_fill()
  turt.penup()
  pongrange = []
  for i in range(0,l+1):
    pongrange.append(localy+i)
  return pongrange
  
  
def up(LoR):
  t.clear()
  if LoR == "L":
    localy = currentpongL
    localx = 10
  if LoR == "R":
    localx = 790
    localy = currentpongR
  else:
    return 
  t.goto(localx, 250)
  t.pendown()
  paddlemake(paddleL, paddleW, t, localx, localy)
  t.penup()
  pongrange = localy + paddleL
  print("up")
  return pongrange
  

def createmap():
  #Create left paddle
  global currentrangeL
  currentrangeL = paddlemake(paddleL, paddleW, t, 10, pongstart)
  global currentpongL
  currentpongL = pongstart
  #Create right paddle
  global currentrangeR
  currentrangeR = paddlemake(paddleL, paddleW, t, 90, pongstart)
  global currentpongR
  currentpongR = pongstart
  makedot(50, 50)

def makedot(x,y):
  t.penup()
  t.goto(x,y)
  t.pendown()
  t.dot(2)
  t.penup()

def checkdot():
  touch = False

def update():
  screen.listen()
  screen.onkey(lambda: up("L"), "w")
createmap()
while True:
  update()
