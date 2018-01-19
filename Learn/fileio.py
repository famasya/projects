def Main():
    f = open("file.txt","w")

    word = raw_input("insert any word : ")
    f.write(word)

    f.close()

if __name__ == "__main__":
    Main()
