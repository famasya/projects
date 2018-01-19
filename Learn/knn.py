import numpy as np

training = [['muda','gemuk','tidak'],\
            ['muda','sangat gemuk','tidak'],\
            ['paruh baya','gemuk','tidak'],\
            ['paruh baya','terlalu gemuk','ya'],\
            ['tua','terlalu gemuk','ya'],\
            ]

index_x = {'muda':1,'paruh baya':2,'tua':3}
index_y = {'gemuk':1,'sangat gemuk':2, 'terlalu gemuk':3}
c_result = []
c = []

umur = 'tua'
kegemukan = 'sangat gemuk'
n = 3

umur = index_x[umur]
kegemukan = index_y[kegemukan]

for i in training:
    for j,k in enumerate(i):
        if(j == 0):
            x = index_x[i[j]]
        elif(j == 1):
            y = index_y[i[j]]
    count = np.sqrt((umur-x)**2+(kegemukan-y)**2)
    c.append(count)
    c_result.append(i[2])

c, c_result = zip(*sorted(zip(c,c_result)))

yes = 0
no = 0

for i in range(n):
    if (c_result[i] == 'ya'):
        yes += 1
    else:
        no += 1

if (yes > no):
    print 'ya'
else:
    print 'no'
