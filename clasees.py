#####################################
# NAME: SEAN GAROFAL-HEAVNER        #
# DATE: 04/10/22                    #
# DISTINCT WAYS TO TILE A 4xN GRID  #
#####################################


def d(n):
    A = [0] * (n + 1)
    A[0] = 1
    A[1] = 0
    dp = 0
    if n == 1:
        return print(f'1 1')
    print(f'1 1')
    for i in range(2, n+1):
        ## reccurence relation equation for 4xn dominoe grid
        A[i] = A[i-1]+5*A[i-2]+A[i-3]-A[i-4]
        dp = A[i] + A[i-1]
        print(f'{i} {dp}')
        '''if dp >= 2147483647:
            return print("32 Bit Integer Threshold Exceeded")'''
    return dp

n = int(input("Enter Grid Width(1-1000): "))

## Checks Constraints
if n >= 1000 or n <= 1 or type(n) != int:
    print('Please Enter A Valid Input')
    n = int(input("Enter Grid Width(1-1000): "))
else:
    x = d(n)
    print(x)

