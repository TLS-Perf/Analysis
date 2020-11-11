import os
from parse import parse, parse_csv
import json

from threading import Thread

num = 5 #number of websites
step = 10000 #step size
stepNum = 20 #step number

websites = ['google.com\n', 'amazon.com\n', 'twitter.com\n', 'youtube.com\n', 'taobao.com\n', 'yahoo.com\n', 'google.co.in\n', 'reddit.com\n', 'qq.com\n', 'facebook.com\n', 'baidu.com\n', 'wikipedia.org\n', 'sociaplus.com\n', 'deliveroo.co.uk\n', 'bet365.it\n', 'wallpaperscraft.ru\n', 'calciomercato.it\n', 'sejda.com\n', 'sexart.com\n', '123netflix.com\n', 'villanova.edu\n', 'overcart.com\n', 'tiava.com\n', 'dsogaming.com\n', 'itver.cc\n', 'traktrafficflow.com\n', 'seoreviewtools.com\n', 'wtvr.com\n', 'mplstudios.com\n', 'filminstan.pw\n', 'tuho.tv\n', 'santongit.com\n', 'coastal.com\n', 'blindstogo.com\n', 'piaotian.cc\n', 'gimoo.net\n', 'sotmarket.ru\n', 'remedio-caseiro.com\n', 'e-korepetycje.net\n', 'viralpatel.net\n', 'cclonline.com\n', 'airows.com\n', 'doc4web.ru\n', 'kunisawa.net\n', 'movableink.com\n', 'newside.gr\n', 'favcars.net\n', 'tvpadtalk.ca\n', 'magvision.com\n', 'srt2sub.xyz\n', 'anyvan.com\n', 'abradio.cz\n', 'snipplr.com\n', 'chinesemenu.com\n', 'music-create.org\n', 'antikleidi.com\n', 'mobills.com.br\n', 'kellerisd.net\n', 'memorado.com\n', 'mycelium.com\n', 'xzf.in\n', 'technosotnya.com\n', 'forexdailypips.com\n', 'haahtela.fi\n', 'oshoworld.com\n', 'novostroy.su\n', 'sib.fm\n', 'brandytube.com\n', 'koopjeskrant.be\n', 'impresaediritto.com\n', 'puntal.com.ar\n', 'chicorei.com\n', 'gourmetsleuth.com\n', 'zdravoe.com\n', 'reliancesmart.in\n', 'rxtv.ru\n', 'jeju.go.kr\n', 'meteoservices.be\n', 'manganetworks.co\n', 'xn--42cah7d0cxcvbbb9x.com\n', 'foli.fi\n', 'kylebrush.com\n', 'bankoftexas.com\n', 'chinaautoweb.com\n', 'profitstars.com\n', 'celebmix.com\n', 'weandy.com\n', 'houra.fr\n', 'hukukmedeniyeti.org\n', 'appsgames.ru\n', 'theeagleonline.com.ng\n', 'spenceclothing.com\n', 'wsceshi.com\n', 'techni-contact.com\n', 'fizzip.com\n', 'momonayama.net\n', 'webyar.net\n', 'feral-heart.com\n', 'kauffman.org\n', 'iboard.ws\n']

'''
threads = []
for th in range(num_threads):
    threads.append(Thread(
'''
'''
def readcsv(website, rank):
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
            rank.append(lineSplit[0])
        for j in range (step - num):
            file1.readline()
            if not line: 
                break
        countStep += 1
    file1.close()
'''
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
    
def analysis():

    with open("result.json", 'r') as fd:
        result = json.loads(fd.read())

    with open("1m.json", 'r') as fd:
        ranking = json.loads(fd.read())


def main():
    print("Tool Started!!!")
    outmaps = {}
    #readcsv(websites,ranks)
    #print(websites,ranks) #websites
    print("Num Websites: ", len(websites))
    runcurl(websites,outmaps)


if __name__ == "__main__":
    # execute only if run as a script
    main()
    #readcsv()