global data
data = []

filee = open("a.txt","r")
for line in filee:
    data.append(line[:-1].split("$$"))
    #print line[:-1].split("$$")
#name,pl,Pe,eps,de,cr

filee.close()

global neighbour
neighbour = []

global limit
limit = 11

global removal
removal = 0

def distance(data1, data2):
    diff = 0
    diff = (float(data1[0])-float(data2[0]))**2 + (float(data1[1])-float(data2[1]))**2 + (float(data1[2])-float(data2[2]))**2 + (float(data1[3])-float(data2[3]))**2
    
    return diff

def neighbours(diff,compData):
    global neighbour
    if len(neighbour) < limit:
        neighbour.append([diff,compData])
        neighbour = sorted(neighbour)
    else:
        neighbour.append([diff,compData])
        neighbour = sorted(neighbour)
        neighbour.pop(len(neighbour)-1)
        
    


def kNeighbour(inputData):
    global neighbour
    neighbour = []
    global removal
    for i in data:
        try:                
            diff = distance(i[2:],inputData)
            #print diff
            if diff >= 0:
                #for j in neighbour:
                #    print ""
                #    print j[0]
                #print ""
                #print ""
                neighbours(diff,i)
            else:
                removal = removal + 1
        except:
            removal = removal + 1
    yes = 0
    no = 0
    for i in neighbour:
        if i[1][1] == 'L':
            no = no+1
        elif i[1][1] == 'P':
            yes = yes + 1
        else:
            print "SOMETHING IS WRONG!!!"
    if yes > no:
        return "PURCHASE IT"
    elif no > yes:
        return "DON'T PURCHASE IT"
    else:
        return "SOMETHING REALLY WENT WRONG!!!"


