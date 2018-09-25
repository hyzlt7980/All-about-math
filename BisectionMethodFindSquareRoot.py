x=float(input('Enter a number to find the squre root: '))
epsilon=0.01
numGuess=0
low=0.0
high=x
ans=(low+high)/2.0
while abs(ans**2-x)>=epsilon and ans<=x:
    print('low: '+str(low))
    print('high: '+str(high))
    print('ans: '+str(ans))
    print()
    numGuess+=1
    if ans**2>x:
        high=ans
    elif ans**2<x:
        low=ans
    ans=(low+high)/2
print('the guess is: '+str(ans))
