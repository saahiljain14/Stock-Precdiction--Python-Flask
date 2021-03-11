
data = []

filee = open("a.txt","r")
for line in filee:
    data.append(line[:-1].split("$$"))
    #print line[:-1].split("$$")
#name,pl,Pe,eps,de,cr
#PE, EPS, DE, CR: P match, N match,

global training

training = [
    [0,0,0,0,0,0],
    [0,0,0,1,0,0],
    [0,0,1,0,0,0],
    [0,0,1,1,0,0],
    [0,1,0,0,0,0],
    [0,1,0,1,0,0],
    [0,1,1,0,0,0],
    [0,1,1,1,0,0],
    [1,0,0,0,0,0],
    [1,0,0,1,0,0],
    [1,0,1,0,0,0],
    [1,0,1,1,0,0],
    [1,1,0,0,0,0],
    [1,1,0,1,0,0],
    [1,1,1,0,0,0],
    [1,1,1,1,0,0],
    ]

def train(compDetails):
    try:
        index = 0
        if float(compDetails[2]) < 10.0:        #pe
            index = index + 8
        if float(compDetails[3]) > 7.0:         #eps
            index = index + 4
        if float(compDetails[4]) < 1.0:         #de
            index = index + 2
        if float(compDetails[5]) > 2.0:         #cr
            index = index + 1
        #print index
        if compDetails[1] == "P":          #profit
            training[index][4] = training[index][4] + 1
            
        elif compDetails[1] == "L":          #loss
            training[index][5] = training[index][5] + 1
        else:
            print "error"
    except:
        print "YOYOYOYOYO"
for i in data:
    train(i)
    #print i[1]


for i in training:
    print i

#getResult([pe,eps,de,cr])

def getResult(compDetails = []):
    index = 0
    result = ""
    if float(compDetails[0]) < 10.0:        #pe
        index = index + 8
    if float(compDetails[1]) > 7.0:         #eps
        index = index + 4
    if float(compDetails[2]) < 1.0:         #de
        index = index + 2
    if float(compDetails[3]) > 2.0:         #cr
        index = index + 1



    
    if training[index][4] < training[index][5]:
        result = result + "LOSS, with probability: " + str((training[index][5]+0.0)/(training[index][4] + training[index][5]))
    elif training[index][4] > training[index][5]:
        result = result + "PROFIT, with probability: " + str((training[index][4]+0.0)/(training[index][4] + training[index][5]))
    else:
        result = result + "Result can't be given by training data set" + "\n"
        index = 0
        if float(compDetails[0]) < 10.0:        #pe
            index = index + 1
        if float(compDetails[1]) > 7.0:         #eps
            index = index + 1
        if float(compDetails[2]) < 1.0:         #de
            index = index + 1
        if float(compDetails[3]) > 2.0:         #cr
            index = index + 1
        if index > 2:
            result = result + "PROFIT, by conditional approach"
        else:
            result = result + "LOSS, by conditional approach"






    return result
filee.close()
print getResult([10.0,7.0,4,6])

print "\n\n"

print getResult([9.0,8.0,0.5,6])
