import math

def Main():
    try:
        number = float(input("input float number : "))
        number = math.pi*number**2
        print "Area :",number
    except:
        print "You didnt enter any number"

if __name__ == "__main__":
    Main()
