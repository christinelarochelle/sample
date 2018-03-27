#Christine LaRochelle
#Exercise02
#This program will check if the number you entered is divisible by 5
#It will be able to ensure that you typed an integer, a number divisible by 5, as well as quit if done is typed 

while True: 
    
#Request for a number from user which is divisible by 5
    number = raw_input( "Enter a price in cents divisible by 5 and I will tell you the solution. If done, type done : ")
 
#Checking if they typed done, if so: end program   
    if number == "done": 
        print
        print "Goodbye!"
        
        break
        
#Checking if the number is an integer        
    try:
        number = int(number)
        
#If not rerun loop     
    except:
        print
        print "That number is not a valid # of cents... Please try again! "
        
        continue
    
#Checking to see if the number is not divisible by 5, if not: rerun loop
    if number %5 != 0:
        print
        print "You did not enter a multiple of 5 sadly, please try again!"
        
        continue
        
#Print statement if they entered an integer that was divisible by 5
    print
    print "You entered %s cents and it is divisible by 5." %(number)