x=int(input('Enter an integer:'))
ans=0
while ans*ans*ans <abs(x):
    ans=ans+
    print('current guess ='+str(ans))
if ans*ans*ans!=abs(x):
    print(str(x)+'is not a perfect cube')
elif x<0:
    ans=-ans
    print('cube root of'+str(x)+' is '+str(ans))
