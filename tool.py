def readcsv(website):
    # Using readline() 
    file1 = open('./top-1m.csv', 'r') 
    count = 0
    
    while True: 
        count += 1
    
        # Get next line from file 
        line = file1.readline() 
    
        # if line is empty 
        # end of file is reached 
        if not line: 
            break
        print("Line{}: {}".format(count, line.strip())) 
    
    file1.close() 

def main():
    print("Tool Started!!!")
    websites = []
    readcsv(websites)

if __name__ == "__main__":
    # execute only if run as a script
    main()
