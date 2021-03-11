from bs4 import BeautifulSoup
import requests
import re
import urllib2
import urllib

url = "https://economictimes.indiatimes.com/markets/stocks/stock-quotes?ticker="
compLinks = []
k = 0
for j in range(97,123):
    r = requests.get(url+chr(j))
    soup = BeautifulSoup(r.content,"html.parser")
    comp = soup.find("ul",{"class":"companyList"}).find_all("a",{"target":"_blank"})
    for i in comp:
        compLinks.append("https://economictimes.indiatimes.com"+i.get("href"))
        #print "https://economictimes.indiatimes.com"+i.get("href")
    #print chr(j)

for j in range(1,9):
    r = requests.get(url+str(j))
    soup = BeautifulSoup(r.content,"html.parser")
    comp = soup.find("ul",{"class":"companyList"}).find_all("a",{"target":"_blank"})
    for i in comp:
        compLinks.append("https://economictimes.indiatimes.com"+i.get("href"))
        #print "https://economictimes.indiatimes.com"+i.get("href")
    #print str(j)

filee = open("stocks.txt","w")

for i in compLinks:
    comName = ""
    comPE = ""
    comEPS = ""
    comDE = ""
    comCR = ""
    comPL = ""
    r = requests.get(i)
    soup = BeautifulSoup(r.content,"html.parser")
    nameComp = soup.find("h1",{"class":"no_newline"})
    comName = nameComp.get("title")                 #company name
    print comName
    peComp = soup.find("span",{"class":"p_e tar"})
    comPE = peComp.text                           #P/E ratio

    epsComp = soup.find_all("div")
    #print epsComp1
    #print epsComp1.get(text)
    for i in range(0,len(epsComp)):
        #print epsComp1
        if epsComp[i].text :
            if epsComp[i].text[:2] == "EPS"[:2]:
                comEPS = epsComp[i+4].text        #EPS
                print comEPS
                break

    

    deComp = soup.find_all("div",{"class":"flt quartName w250"})
    deComp1 = soup.find_all("div",{"class":"flt quartYear w100"})
    for i in range(0,len(deComp)):
        if deComp[i].text :
            if deComp[i].text[:10] == "Debt Equity Ratio (x)"[:10]:
                comDE = deComp1[i-1].text         #D/E ratio
    
    crComp = soup.find_all("div",{"class":"flt quartName w250"})
    crComp1 = soup.find_all("div",{"class":"flt quartYear w100"})
    for i in range(0,len(crComp)):
        if crComp[i].text :
            if crComp[i].text[:8] == "Current Ratio (x)"[:8]:
                comCR = crComp1[i-1].text         #current ratio

#    netChange1 = soup.find("div",{"class":"netChange"}).find_all("span")
#    for netChange in netChange1:
#        if netChange.get("class") != None:
#            if netChange.get("class")[1] == "upArrow":
#                print "profit"
#            elif netChange.get("class")[1] == "downArrow":
#                print "Loss"

    netChange1 = soup.find("span",{"id":"nseNetchange"})
    try:
        netChange = ""
        netChange = float(netChange1.text)
    except:
        print "Error "+comName
        netChange = ""
        netChange1 = soup.find("span",{"id":"bseNetchange"})
        netChange = float(netChange1.text)
        print netChange
    if netChange < 0.0:
        comPL = "L"
    elif netChange > 0.0:
        comPL = "P"
    elif netChange == 0.0:
        comPL = "P"
    else:
        comPL = ""

    
    if comName != "" and comPL  != "" and comPE != "" and comEPS != "" and comDE != "" and comCR != "":
        filee.write(comName+"$$"+comPL+"$$"+comPE+"$$"+comEPS+"$$"+comDE+"$$"+comCR+"\n")
        print 1
    else:
        print comName
    #print epsComp[10].text
filee.close()
