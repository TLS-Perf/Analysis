import json

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
        #import pdb; pdb.set_trace()
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

def parse_csv():
    with open('./top-1m.csv', 'r') as fd:
        lines = fd.readlines()

    dic = {}
    for line in lines:
        rank, website = line.split(',')
        rank = int(rank)
        dic[website] = rank
    
    with open("1m.json", 'w') as fp:
        fp.write(json.dumps(dic))
        
    return dic


if __name__ == "__main__":
    with open("3.txt", 'r') as fp:
        ret = parse(fp.read())
    
    import pdb; pdb.set_trace()