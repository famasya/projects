def Main():
    try:
        f = open("foo.txt","r")
        for line in f:
            print line.strip("\n")
        f.close()
    except:
        print "File not found"
    finally:
        print "Exiting..."

if __name__ == "__main__":
    Main()
