x = 10
epsilon = 0.01
step = 0.1
guess = 0.0

while guess <= x:
     print("guess: " + str(guess))
     print("calculated : " + str(abs(guess**2 -x)))
     if abs(guess**2 -x) < epsilon:
         break
     else:
         guess += step

if abs(guess**2 - x) >= epsilon:
     print("failed")
else:
     print("succeeded: "+ str(guess))