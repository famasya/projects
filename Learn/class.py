class Kelas:
    number = 0
    name = "lorem ipsum"

def Main():
    kelas = Kelas()
    kelas.name = "Kelas memasak"
    kelas.number = 20

    print "Kelas : " + kelas.name + ", jumlah : " + str(kelas.number)

if __name__ == '__main__':
    Main()
