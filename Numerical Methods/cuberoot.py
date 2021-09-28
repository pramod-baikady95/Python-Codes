"""
Cube Root Program
"""

cube = float (input ("Enter the number to find it's cube root : "))
eps = 0.001
increment = 0.0001
num_guess = 0
guess = float (input ("Enter the initial guess for the cube root : "))

#while abs(guess**3 - cube)>= eps and guess<= cube :
#    guess += increment
#    num_guess +=1
#print ("Number of guesses = ", num_guess)
#
#if abs(guess**3 - cube)>= eps : 
#    print ("Failed on Cube root of", cube)
#else:
#    print (guess,"is the close value of cube root for", cube) 
    
    
test = cube/(1.2*guess*guess)
print ("init_guess =", guess)
print ("init_test =", test)


if (guess >= test ):
    while (guess >= test ): 
        print ("Enter the lesser value of guess !!")
        guess = float (input ("Enter the new guess for the cube root : "))
        test = cube/(1.2*guess*guess)
        print ("guess =", guess)
        print ("test =", test)
        
        if (guess < test):
            print ("Guess value is acceptable")
            break
else:   
    while abs(guess**3 - cube)>= eps and guess<= cube :
        guess += increment
        num_guess +=1
    print ("Number of guesses = ", num_guess)

    if abs(guess**3 - cube)>= eps : 
        print ("Failed on Cube root of", cube)
    else:
        print (guess,"is the close value of cube root for", cube)


        