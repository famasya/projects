def Main():
    for i in range(10):
        print "Hello"
    # words()
    # ask()
    ask2()

def words():
    words = ["lorem","ipsum","dolor","sit","amet"]
    for word in words:
        print word

def ask():
    num = 0
    while (num<=0):
        num = int(input("input your number : "))

def ask2():
    while True:
        num = input("input any number : ")
        print num

if __name__ == "__main__":
    Main()
