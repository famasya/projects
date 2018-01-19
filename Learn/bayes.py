from __future__ import division
import operator

training = [["cerah","normal","pelan","ya"],["cerah","normal","pelan","ya"],["hujan","tinggi","pelan","tidak"],["cerah","normal","kencang","ya"],["hujan","tinggi","kencang","tidak"],["cerah","normal","pelan","ya"]]

cuaca = raw_input("cuaca : ")
temperatur = raw_input("temperatur : ")
angin = raw_input("angin : ")

olahraga = {}
decision_index = len(training[0])-1
decision = {}

# training phase
for i in range(len(training)):
    current = training[i][decision_index]
    # push each desicion to dictionary
    if(current not in olahraga):
        olahraga[current] = {"sum":1, "cuaca":0, "temperatur":0, "angin":0}
        decision[current] = 1
    else:
        olahraga[current]["sum"] += 1

    # push to precreated dictionary for each matching criteria
    if((cuaca == training[i][0]) & (cuaca != "?")):
        olahraga[training[i][decision_index]]["cuaca"] += 1
    if((temperatur == training[i][1]) & (temperatur != "?")):
        olahraga[training[i][decision_index]]["temperatur"] += 1
    if((angin == training[i][2]) & (angin != "?")):
        olahraga[training[i][decision_index]]["angin"] += 1

# count the probability
for k, v in olahraga.iteritems():
    for k2, v2 in v.iteritems():
        if(k2 != "sum"):
            v[k2] = v2/v["sum"]
        else:
            v["sum"] = v2/len(training)

print olahraga

# make the decision
for k, v in olahraga.iteritems():
    for k2, v2 in v.iteritems():
        if(k2 == "sum"):
            decision[k] *= v2
        if((cuaca != "?") & (k2 == "cuaca")):
            decision[k] *= v2
        if((temperatur != "?") & (k2 == "temperatur")):
            decision[k] *= v2
        if((angin != "?") & (k2 == "angin")):
            decision[k] *= v2

decision = sorted(decision.items(), key=operator.itemgetter(1), reverse=True)
print "Olahraga :",decision[0][0]
