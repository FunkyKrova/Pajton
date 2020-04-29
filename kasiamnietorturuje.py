def greet(name):
    print("Hello " + name + ". Ruple is it?")

def i_ate(food):
    print("I ate too much " + food)

def multiply(a,b):
    return a*b

def i_ate(food,a):
    #not correct/not complete solution
    #print("I ate too much " + food + ", should have eaten ")
    #print(a/2)

    #without rounding - str
    ammount = str(a / 2)
    print("I ate too much " + food + ", should have eaten " + ammount)
    
    #wih rounding - change to int
    #ammount = str(int(a / 2))
    #print("I ate too much " + food + ", should have eaten " + ammount)
