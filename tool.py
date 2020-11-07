import os

num = 100 #number of websites

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

def runcurl(websites, outputs):
    for website in websites:
        print(website)
        stream = os.popen('./curltimes.sh compare https://' + website)
        outputs.append(stream.read())

def main():
    print("Tool Started!!!")
    websites = []
    outputs = []
    readcsv(websites)
    print(websites) #websites
    runcurl(websites,outputs)
    print(outputs) #output of curl

if __name__ == "__main__":
    # execute only if run as a script
    main()
