from __future__ import division
import numpy
import pprint
import math

training = {"outlook":{"sunny":{"yes":2,"no":3},"overcast":{"yes":4,"no":0},"rainy":{"yes":3,"no":2}},\
            "temperature":{"yes":[83,70,68,64,69,75,75,72,81],"no":[85,80,65,72,71]},\
            "humidity":{"yes":[86,96,80,65,70,80,70,90,75],"no":[85,90,70,95,91]},\
            "windy":{"false":{"yes":6,"no":2},"true":{"yes":3,"no":3}},\
            "play":{"yes":9,"no":5}}
processed = {}
total_yes = training["play"]["yes"]
total_no = training["play"]["no"]
total_all = training["play"]["no"]+training["play"]["yes"]

def _find(obj,key):
    if key in obj:
        return obj[key]
    for k,v in obj.items():
        if isinstance(v,dict):
            item = _find(v,key)
            if item is not None:
                return item

def _calc(w,mean,std):
    calc = (1/(math.sqrt(2*math.pi)*std))*math.exp(-1*pow((w-mean),2)/(2*pow(std,2)))
    return calc

def _decision(outlook,temperature,humidity,windy):
    outlook = _find(processed,outlook)
    windy = _find(processed,windy)
    play = processed["play"]
    t = processed["temperature"]
    h = processed["humidity"]
    p_yes = outlook["yes"]*windy["yes"]*play["yes"]*_calc(temperature,t["yes"]["mean"],t["yes"]["std"])*_calc(humidity,h["yes"]["mean"],h["yes"]["std"])
    p_no = outlook["no"]*windy["no"]*play["no"]*_calc(temperature,t["no"]["mean"],t["no"]["std"])*_calc(humidity,h["no"]["mean"],h["no"]["std"])
    print {"yes":p_yes,"no":p_no}
    if(p_yes>p_no):
        return "yes"
    else:
        return "no"


def main():
    for k,v in training.iteritems():
        if(k != "play"):
            for k2,v2 in v.iteritems():
                if((k2 == "yes") & isinstance(v2,list)):
                    processed[k] = {"yes":{"mean":numpy.mean(v2),"std":numpy.std(v2,ddof=1)}}
                elif((k2 == "no") & isinstance(v2,list)):
                    processed[k].update({"no":{"mean":numpy.mean(v2),"std":numpy.std(v2,ddof=1)}})
                else:
                    for i,j in v2.iteritems():
                        if(i == "yes"):
                            p_yes = j/total_yes
                            p_no = v2["no"]/total_no
                            if k not in processed:
                                processed[k] = {k2:{"yes":p_yes,"no":p_no}}
                            else:
                                processed[k][k2] = {"yes":p_yes,"no":p_no}

        else:
            processed[k] = {"yes":total_yes/total_all,"no":total_no/total_all}

    pp = pprint.PrettyPrinter(indent=3)
    pp.pprint(processed)

    # print _calc(90,86.2,9.7)
    outlook = raw_input('outlook : ')
    temperature = int(raw_input('temperature : '))
    humidity = int(raw_input('humidity : '))
    windy = raw_input('windy : ')
    print "playing :",_decision(outlook, temperature, humidity, windy)

if __name__ == '__main__':
    main()
