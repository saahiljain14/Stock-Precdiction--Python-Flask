from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D

data = []

filee = open("a.txt","r")
for line in filee:
    data.append(line[:-1].split("$$"))
    #print line[:-1].split("$$")
#name,pl,Pe,eps,de,cr
#PE, EPS, DE, CR: P match, N match,



fig = pyplot.figure()
ax = Axes3D(fig)

xxx=[]
yyy=[]
zzz=[]

for i in data:
    try:
        if (float(i[2]) > 0) and (float(i[3]) > 0) and (float(i[4]) > 0):
            xxx.append(float(i[2]))
            yyy.append(float(i[3]))
            zzz.append(float(i[4]))
    except:
        print "Do"
        

ax.scatter(xxx, yyy, zzz)
pyplot.show()
