import random

def main():
    bias = 1
    x1 = [0,0,1,1]
    x2 = [0,1,0,1]
    w = []
    output = []
    desired = [0,1,1,0]
    iterasi = 0

    # lr = float(input("learning rate : "))
    lr = 0.01
    # epoch = int(input("epoch : "))
    epoch = 4

    for i in range(3):
        w.append(random.uniform(-1,1))

    while iterasi < epoch:
        out = []
        rawout = []
        for i in range(4):
            calc = bias*w[0]+x1[i]*w[1]+x2[i]*w[2]
            # if(calc>0):
            #     calc = 1
            # else:
            #     calc = 0
            out.append(calc)
        for j, val in enumerate(out):
            if ((val > 0 and desired[j] == 0) or (val <= 0 and desired[j] == 1)):
                print "corrected",j,desired[j],val
                err = desired[j]-val
                print "err",err
                if (err > 0):
                    print "before",w
                    w[0] += lr*val*err
                    w[1] += lr*val*err
                    w[2] += lr*val*err
                    print "after",w
            # else:
                # print "true",desired[j],val
        # output.append(out)
        print "epoch",(iterasi+1)," :",out
        iterasi += 1

    # print output[len(output)-1]

if __name__ == '__main__':
    main()
