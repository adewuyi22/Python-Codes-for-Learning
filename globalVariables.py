#This is global variables
x="I like apples - Global variables" 

#creating a function
def myfood():

    #This is local variables
    food ="My best food is Yam"
    print(x)
    print(food)
    
def mycolor():
    #Declaring a Global variable inside a function to be 
    #accesible by other functions using the 'Global' keyword
    global color 
    color="My best color is Blue"
    print(x)
    print(color)
   
def grantAccess():
    print("accessing global variable for color: "+color)


myfood()
mycolor()
grantAccess()
