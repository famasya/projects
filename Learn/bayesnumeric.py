from __future__ import division
import numpy
import math

def calc(w,mean,std):
    calc = (1/(math.sqrt(2*math.pi)*std))*math.exp(-1*pow((w-mean),2)/(2*pow(std,2)))
    return calc

def main():
    training = {"outlook":["sunny","sunny","overcast","rain","rain","rain","overcast","sunny","sunny","rain","sunny","overcast","overcast","rain"],\
                "temperature":[85,80,83,70,68,65,64,72,69,75,75,72,81,71],\
                "humidity":[85,90,86,96,80,70,65,95,70,80,70,90,75,91],\
                "wind":["weak","strong","weak","weak","weak","strong","strong","weak","weak","weak","strong","strong","weak","strong"],\
                "play":["no","no","yes","yes","yes","no","yes","no","yes","yes","yes","yes","yes","no"]}

    q = {"outlook":0, "temperature":0, "humidity":0, "wind":0}
    # q = {"outlook":"sunny", "temperature":66, "humidity":90, "wind":"strong"}
    count = {}
    c_yes = 0
    c_no = 0
    p_yes = 1
    p_no = 1
    for k,v in q.iteritems():
        if((k == "temperature") | (k == "humidity")):
            a = int(raw_input(k+" : "))
        else:
            a = raw_input(k+" : ")
        q[k] = a

    for v in training["play"]:
        if(v == "yes"):
            c_yes += 1
        else:
            c_no += 1

    for k,v in training.iteritems():
        temp_yes = 0
        temp_no = 0
        if (k != "play"):
            if (not isinstance(v[0], int)):
                count[k] = {q[k]:{"yes":0,"no":0}}
                for idx,val in enumerate(v):
                    if (val == q[k]):
                        states = training["play"][idx]
                        count[k][val][states] += 1
                print 'yes',k,p_yes,count[k][q[k]]["yes"]/c_yes
                p_yes *= (count[k][q[k]]["yes"]/c_yes)
                print 'no',k,p_no,count[k][q[k]]["yes"]/c_no
                p_no *= (count[k][q[k]]["no"]/c_no)
            else:
                y = []
                n = []
                for idx,val in enumerate(v):
                    states = training["play"][idx]
                    if(states == "yes"):
                        y.append(val)
                    else:
                        n.append(val)
                count[k] = {"yes":{"mean":numpy.mean(y),"std":numpy.std(y,ddof=1)},"no":{"mean":numpy.mean(n),"std":numpy.std(n,ddof=1)}}
                print 'yes',k,p_yes,calc(q[k],count[k]["yes"]["mean"],count[k]["yes"]["std"])
                p_yes *= calc(q[k],count[k]["yes"]["mean"],count[k]["yes"]["std"])
                print 'no',k,p_no,calc(q[k],count[k]["no"]["mean"],count[k]["no"]["std"])
                p_no *= calc(q[k],count[k]["no"]["mean"],count[k]["no"]["std"])
        else:
            print 'yes',p_yes
            p_yes *= (c_yes/(c_yes+c_no))
            print 'no',p_no
            p_no *= (c_no/(c_yes+c_no))

    print '----------------'
    print 'yes',p_yes,'no',p_no
    if p_yes > p_no:
        print "play : yes"
    else:
        print "play : no"

if __name__ == '__main__':
    main()
