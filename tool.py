import os
from parse import parse
import json

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

def runcurl(websites, outmaps):
    for website in websites:
        try:
            print(website)
            stream = os.popen('./curltimes.sh compare https://' + website)
            output = stream.read()
            outmap = parse(output)
            print(outmap)
            outmaps[website] = outmap
        except Exception as e:
            print ("Error")

        with open("result.json", 'w') as fp:
            fp.write(json.dumps(outmaps))
    




def main():
    print("Tool Started!!!")
    websites = []
    outmaps = {}
    readcsv(websites)
    print(websites) #websites
    runcurl(websites,outmaps)


if __name__ == "__main__":
    # execute only if run as a script
    main()
