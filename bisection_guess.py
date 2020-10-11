#Program to find a close sqaure root value of number with guess
x = 470
epsilon = 0.01
numOfGuesses = 0
low = 0.0
high = x
ans = (high + low)/2.0
while abs(ans**2 - x) >= epsilon:
    print('low = ' + str(low) + '; high = ' + str(high) + '; ans = ' + str(ans))
    numOfGuesses += 1
    if ans**2 > x:
        high = ans
    else:
        low = ans
    ans = (high + low)/2.0

print('Total No of guesses: ' + str(numOfGuesses))
print(str(ans) + ' is close to the square root of ' + str(x))

