import os
from parse import parse

num = 3 #number of websites
step = 100000 #step size
stepNum = 10 #step number
def readcsv(website):
    # Using readline() 
    file1 = open('./top-1m.csv', 'r') 
    countStep = 0
    
    while countStep < stepNum:
        for i in range (num):
            # Get next line from file 
            line = file1.readline() 
            # if line is empty 
            # end of file is reached 
            if not line: 
                break
            lineSplit = line.split(',')
            website.append(lineSplit[1])
        for j in range (step - num):
            file1.readline()
            if not line: 
                break
        countStep += 1
    file1.close()
'''
def readcsv(website):
    # Using readline() 
    file1 = open('./top-1m.csv', 'r') 
    count = 0
    
    while count < num:
        # Get next line from file 
        line = file1.readline() 
        # if line is empty 
        # end of file is reached 
        if not line: 
            break
        lineSplit = line.split(',')
        website.append(lineSplit[1])
        count += 1
    file1.close()
'''
def runcurl(websites, outmaps):
    for website in websites:
        print(website)
        stream = os.popen('./curltimes.sh compare https://' + website)
        output = stream.read()
        outmap = parse(output)
        print(outmap)
        outmaps.append(outmap)
'''
def parse(str):
    lines = str.split("\n")
    support_tls13 = 1 if "tls13" in lines[7] else 0
    metric = ["avg", "median", "min", "max", "75", "95", "99"]

    ret = {
        "support3": support_tls13,
        "tls2": {
            
        },
        "tls3": {

        }
    }

    for i in range(4, 24, 4):
        ## TLS 1.2
        ret["tls2"][lines[i][7:]] = {}
        values = map(lambda a: float(a), lines[i+2][7:].split(","))
        
        for (index, value) in enumerate(values):
            ret["tls2"][lines[i][7:]][metric[index]] = value
        
        ## TLS 1.3
        if support_tls13:
            ret["tls3"][lines[i][7:]] = {}
            values = map(lambda a: float(a), lines[i+3][7:].split(","))
            for (index, value) in enumerate(values):
                ret["tls3"][lines[i][7:]][metric[index]] = value
    return ret
'''
def main():
    print("Tool Started!!!")
    websites = []
    outmaps = []
    readcsv(websites)
    print(websites) #websites
    runcurl(websites,outmaps)

if __name__ == "__main__":
    # execute only if run as a script
    main()
