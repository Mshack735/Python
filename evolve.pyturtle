import turtle
import random
import time


turtle = turtle
turtle.speed('fastest')



degrees=random.randint(0,360)


  
directions=[turtle.forward,turtle.left,turtle.right]


attemptThis= (turtle.pos() == (0.00, 0.00))

  
target=(0,0)



def attemptNext():
  for x in range(100):
    random.choice(directions)(degrees)

completed = False

generation = 0

while completed == False:
  attemptNext()
  completed = True
  if attemptThis != target:
    completed = False
    generation += 1
    turtle.reset()
    time.sleep(1)
    print (attemptThis)


print('Hit target!')
 
  
  
  
  
  
