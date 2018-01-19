import random

w = []
c = 0.1

def ff(inputs):
    j = 0
    for i,val in enumerate(inputs):
        j += val*w[i]
    return activate(j)

def activate(j):
    if j > 0:
        return 1
    else:
        return 0

def train(inputs, desired, w):
    guess = ff(inputs)
    error = desired-guess
    for i,val in enumerate(w):
        w[i] += c*error*inputs[i]

def epoch(w):
    test = [[0,0,1],[1,0,1],[0,1,1],[1,1,1]]
    desired = [0,1,1,0]
    for i,val in enumerate(test):
        train(val,desired[i],w)
        # print w

def main():
    test = [[0,0,1],[1,0,1],[0,1,1],[1,1,1]]

    for i in range(3):
        w.append(random.uniform(-1,1))

    for i in range(2000):
        epoch(w)

if __name__ == '__main__':
    main()
