

def parse(lines):
    
    support_tls13 = 1 if "tls13" in lines[7] else 0
    metric = ["avg", "median", "min", "max", "75", "95", "99"]

    ret = {
        "support3": support_tls13,
        "tls2": {
            
        }
    }

    for i in range(4, 24, 4):
        ## TLS 1.2
        ret["tls2"][lines[i][7:-1]] = {}
        values = map(lambda a: float(a), lines[i+2][7:-1].split(","))
        
        for (index, value) in enumerate(values):
            ret["tls2"][lines[i][7:-1]][metric[index]] = value
        
        ## TLS 1.3
        if support_tls13:
            ret["tls3"] = {}
            ret["tls3"][lines[i][7:-1]] = {}
            values = map(lambda a: float(a), lines[i+3][7:-1].split(","))
            for (index, value) in enumerate(values):
                ret["tls2"][lines[i][7:-1]][metric[index]] = value

    return ret

if __name__ == "__main__":
    with open("3.txt", 'r') as fp:
        ret = parse(fp.readlines())