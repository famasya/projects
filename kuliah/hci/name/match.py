import re

def dist(a,b):
    n = len(a)
    m = len(b)
    
    if(n == 0):
        return m
    if(m == 0):
        return n
    
    row = 0
    col = 0
    d = []
    for i in range(n+1):
        d_row = []
        for j in range(m+1):
            d_row.append(0)
        d.append(d_row)
    
    for i in range(m+1):
        d[0][i] = i
        
    for i in range(n+1):
        d[i][0] = i
        
    for i in range(1,n+1):
        c = []
        for j in range(1,m+1):
            if(a[i-1] == b[j-1]):
                cost = 0
            else:
                cost = 1
            
            val = min(d[i-1][j]+1,d[i][j-1]+1,d[i-1][j-1]+cost)
            d[i][j] = val
        
    return d[n][m]
def main():
    name = []
    with open("name.txt") as f:
        name = f.read().splitlines()
       
    a = raw_input("nama: ").split(" ")

    nm = 0
    minimal = 99999
    regex = re.compile('[^a-z ]')
    
    for a in a:
        a = regex.sub(' ',a)
        for k,v in enumerate(name):
            splitted = regex.sub(' ',v.lower()).split(" ")

            for w in splitted:
                x = dist(a,w)
                if(x < minimal):
                    minimal = x
                    nm = k
    print name[nm]
    
if __name__ == "__main__":
    main()