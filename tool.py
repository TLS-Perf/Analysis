import subprocess
import os
from parse import parse, parse_csv
import json
import random

from threading import Thread

num = 10 #number of websites
step = 10000 #step size
stepNum = 30 #step number
newwebsites = ['google.com\n', 'youtube.com\n', 'facebook.com\n', 'baidu.com\n', 'wikipedia.org\n', 'yahoo.com\n', 'google.co.in\n', 'reddit.com\n', 'qq.com\n', 'amazon.com\n', 'kapanlagi.com\n', 'secureserver.net\n', 'kissmanga.com\n', 'onliner.by\n', 'navyfederal.org\n', 'fobshanghai.com\n', 'idope.se\n', 'panzoid.com\n', 'pku.edu.cn\n', 'picocurl.com\n', 'startlap.hu\n', 'tvbok.com\n', 'leral.net\n', 'wmflabs.org\n', 'doujins.com\n', 'lexigram.gr\n', 'voyeur-villa.com\n', 'edreams.fr\n', 'spicybigtits.com\n', 'sh.gov.cn\n', 'mutaz.net\n', 'kuwaitairways.com\n', 'jlpt.jp\n', 'shuaijiao.com\n', 'kit.com\n', 'mgu.ac.in\n', '550909.com\n', 'ellegirl.ru\n', 'video9.in\n', 'thenewboston.com\n', 'papy-streaming.org\n', 'verybeaut.com\n', 'meter.net\n', 'caib.es\n', 'sexscenemovies.net\n', 'ipindiaonline.gov.in\n', 'champion.com\n', 'gta5cheats.com\n', 'realestate.co.nz\n', 'avanquest.com\n', 'way2pay.ir\n', 'insidethegames.biz\n', 'info-retraite.fr\n', 'arlo.com\n', 'portalangop.co.ao\n', 'commvault.com\n', 'voobly.com\n', 'kimblegroup.com\n', 'apronus.com\n', 'kenhub.com\n', 'pizzabottle.com\n', 'radiocloud.jp\n', 'kmdevantagens.com.br\n', 'hilive.tv\n', '4cd.edu\n', 'sdelaicomp.ru\n', 'cedynamall.com\n', 'manbang.tmall.com\n', 'technologycraze.org\n', 'mlmgateway.com\n', 'renater.fr\n', 'oshiete-kun.net\n', 'themeum.com\n', 'tubesexworld.com\n', 'grafana.org\n', 'mmm.dk\n', 'tele-envivo.com\n', 'changepw.com\n', 'aviakassa.ru\n', 'faptorrent.com\n', 'leaguelane.com\n', 'rics.org\n', 'insightexpressai.com\n', 'manetama.jp\n', 'toptarif.de\n', 'metageek.com\n', 'www.police.uk\n', 'innogy.pl\n', 'famethemes.com\n', 'onlinewebfonts.com\n', 'serialkeysoftware.com\n', 'kagoya.com\n', 'vandahost.net\n', 'robvanderwoude.com\n', 'directemploi.com\n', 'stofa.dk\n', 'fermilon.ru\n', 'gamebrott.com\n', 'non-stop-people.com\n', 'quickbooks.co.uk\n', 'siliconangle.com\n', 'charter.ir\n', 'moemaka.com\n', 'incomeon.com\n', 'zazozu.com\n', 'projectlombok.org\n', 'magltk.com\n', 'marklines.com\n', 'odessa1.com\n', 'drone-world.com\n', 'aim400kg.com\n', 'flot.com\n', 'teleborsa.it\n', 'biosom.com.br\n', 'sajhapage.com\n', 'outofmilk.com\n', 'housebrand.com\n', 'pac.ru\n', 'diletant-ik.ru\n', 'ra9.jp\n', 'multichannel.com\n', 'eppointmentsplus.com\n', 'iccwbo.org\n', 'beautyanal.tumblr.com\n', 'semuanyabola.com\n', 'ellinair.com\n', 'sf.co.ua\n', 'welingkaronline.org\n', 'sexy-beauties.com\n', 'studyadda.com\n', 'rencontre-ados.net\n', 'airportrentals.com\n', 'protabletpc.ru\n', '33le.com\n', 'odalys-vacances.com\n', 'poshgay.com\n', 'sing365.com\n', 'jackpot.com\n', 'cssz.cz\n', 'avavav3.com\n', 'comprecar.com.br\n', 'uatx.mx\n', 'argolikeseidhseis.gr\n', 'luxup2.ru\n', 'cetesdirecto.com\n', 'sinoquebec.com\n', 'wbrc.com\n', 'fetsm.org\n', 'world-machine.com\n', 'metricstream.com\n', 'videomakerfx.com\n', 'imgsay.com\n', 'dart.org\n', 'tuts4you.com\n', 'vecinabellax.com\n', 'icovia.com\n', 'chien.fr\n', 'laborator.co\n', 'myitforum.com\n', 'xliby.ru\n', 'wklken.me\n', 'it-jobbank.dk\n', 'caseih.com\n', 'onlinevarsity.com\n', 'tribebyamrapali.com\n', 'jockfootfantasy.com\n', 'uvdesk.com\n', 'kaise-kare.com\n', 'megapixl.com\n', 'harald-nyborg.se\n', 'aliasdmc.fr\n', 'transdirect.com.au\n', 'healthrangerstore.com\n', 'job-room.ch\n', 'anypay.jp\n', 'brazzers-girls.com\n', 'cricshots.com\n', 'maccms.com\n', 'designsandcode.com\n', 'hudeem99.ru\n', 'consumerinsight.co.kr\n', 'kacgun.com\n', 'bzsou.cn\n', 'borimed.com\n', 'fromgeek.com\n', 'f-fans.in\n', 'it-innovation.co.jp\n', 'ac3j.fr\n', 'penguin.com.au\n', 'profi.travel\n', 'dafangya.net\n', 'dinosaurgames.me\n', 'dylianmeng18.info\n', 'deals.bg\n', 'kamera-express.be\n', 'a3da.online\n', 'myclub8.com\n', 'etelka.cz\n', 'smelchi.com\n', 'ikyaglobal.com\n', 'tindinthad2.pw\n', 'genflix.co.id\n', 'i-d.co\n', 'skorks.com\n', 'vkblog.ru\n', 'myp30movie.ir\n', 'droidfirmware.com\n', 'gettransfer.com\n', 'travelsort.com\n', 'freefavicon.com\n', 'kinotime.org\n', 'lepdan.si\n', 'supremacysounds.com\n', 'thaixdoujin.com\n', 'dairymary.com\n', 'bacstmg.net\n', 'bankjerusalem.co.il\n', 'boriko.com\n', 'fran.si\n', 'videoklinika.hu\n', 'irwebspace.com\n', 'healthyfocus.org\n', 'guideguide.me\n', 'hardresetandroid.com\n', 'hapmm.com\n', 'sgc.gov.co\n', 'alliance-healthcare.com.tr\n', 'workingclassheroes.co.uk\n', 'mxone.net\n', 'amazinggrass.com\n', 'printwhatyoulike.com\n', 'ukcat.ac.uk\n', 'ibibo.com\n', 'camicianista.com\n', 'lospollos.com\n', 'lagunaclub.ru\n', 'snting134.com\n', 'techtoday.in.ua\n', 'arduino-ua.com\n', 'toosurtoo.com\n', 'van.vn\n', 'birdsnow.com\n', 'larsson.es\n', 'listaatollo.altervista.org\n', 'dhlparcel.be\n', 'jobandplacement.com\n', 'zcar.com\n', 'debugmode.com\n', 'mir921.ru\n', 'ip-score.com\n', 'proverki.gov.ru\n', 'spacefucker.com\n', 'nashanyanya.com.ua\n', 'bitcoin2048.com\n', 'miyaji.co.jp\n', 'infomedia.dk\n', 'grandtechno.ru\n', 'pixmania.it\n', 'comac.cc\n', 'enavi-salary.net\n', 'momenty.org\n', 'almomento.mx\n', 'tcrinrvfejjh.com\n', 'nmn.jp\n', 'quiksilver.ru\n', '1ua.com.ua\n', 'alrajhibank.com.kw\n', 'vanillaandbean.com\n', 'martinsbonus.com\n', 'pet4u.gr\n', 'sagestart.com.br\n', 'peepsamurai.com\n', 'jimikeji.tmall.com\n', 'suiyang.cn\n', 'megatnt.com.br\n', 'ranktank.org\n', 'mindmaple.com\n', 'gala-navi.com\n', 'binaural.es\n', 'motopreview.com\n', 'thecutekid.com\n', 'radiointernetowe.com.pl\n', 'lengalia.com\n', 'freddiesville.com\n', 'zetacad.com\n', 'guichetunique.cm\n', 'persianseven.ir\n', 'srmu.ac.in\n', 'atlink.jp\n', 'mygcww.org\n', 'dwbooster.com\n', 'thawratalweb.com\n']
#websites = ['google.com\n', 'amazon.com\n', 'twitter.com\n', 'youtube.com\n', 'taobao.com\n', 'yahoo.com\n', 'google.co.in\n', 'reddit.com\n', 'qq.com\n', 'facebook.com\n', 'baidu.com\n', 'wikipedia.org\n', 'sociaplus.com\n', 'deliveroo.co.uk\n', 'bet365.it\n', 'wallpaperscraft.ru\n', 'calciomercato.it\n', 'sejda.com\n', 'sexart.com\n', '123netflix.com\n', 'villanova.edu\n', 'overcart.com\n', 'tiava.com\n', 'dsogaming.com\n', 'itver.cc\n', 'traktrafficflow.com\n', 'seoreviewtools.com\n', 'wtvr.com\n', 'mplstudios.com\n', 'filminstan.pw\n', 'tuho.tv\n', 'santongit.com\n', 'coastal.com\n', 'blindstogo.com\n', 'piaotian.cc\n', 'gimoo.net\n', 'sotmarket.ru\n', 'remedio-caseiro.com\n', 'e-korepetycje.net\n', 'viralpatel.net\n', 'cclonline.com\n', 'airows.com\n', 'doc4web.ru\n', 'kunisawa.net\n', 'movableink.com\n', 'newside.gr\n', 'favcars.net\n', 'tvpadtalk.ca\n', 'magvision.com\n', 'srt2sub.xyz\n', 'anyvan.com\n', 'abradio.cz\n', 'snipplr.com\n', 'chinesemenu.com\n', 'music-create.org\n', 'antikleidi.com\n', 'mobills.com.br\n', 'kellerisd.net\n', 'memorado.com\n', 'mycelium.com\n', 'xzf.in\n', 'technosotnya.com\n', 'forexdailypips.com\n', 'haahtela.fi\n', 'oshoworld.com\n', 'novostroy.su\n', 'sib.fm\n', 'brandytube.com\n', 'koopjeskrant.be\n', 'impresaediritto.com\n', 'puntal.com.ar\n', 'chicorei.com\n', 'gourmetsleuth.com\n', 'zdravoe.com\n', 'reliancesmart.in\n', 'rxtv.ru\n', 'jeju.go.kr\n', 'meteoservices.be\n', 'manganetworks.co\n', 'xn--42cah7d0cxcvbbb9x.com\n', 'foli.fi\n', 'kylebrush.com\n', 'bankoftexas.com\n', 'chinaautoweb.com\n', 'profitstars.com\n', 'celebmix.com\n', 'weandy.com\n', 'houra.fr\n', 'hukukmedeniyeti.org\n', 'appsgames.ru\n', 'theeagleonline.com.ng\n', 'spenceclothing.com\n', 'wsceshi.com\n', 'techni-contact.com\n', 'fizzip.com\n', 'momonayama.net\n', 'webyar.net\n', 'feral-heart.com\n', 'kauffman.org\n', 'iboard.ws\n']
def readrandcsv(websites):
    file1 = open('./top-1m.csv', 'r')
    lines = file1.readlines()
    for i in range (num):
        split = lines[i].split(',')
        websites.append(split[1])
    for i in range (stepNum):
        randomlist = random.sample(range(i*step, (i+1)*step), num)
        randomlist.sort()
        print(randomlist)
        for index in randomlist:
            split = lines[index].split(',')
            websites.append(split[1])

def filterWebs(websites,filteredWebs):
    for website in websites:
        print(website)
        flag = True
        p = subprocess.Popen('./curltimes.sh compare https://' + website, shell = True)
        try:
            p.wait(20)
        except subprocess.TimeoutExpired:
            p.kill()
            print("killed")
            flag = False
        if flag:
            filteredWebs.append(website)

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
'''
def runcurl(websites, outmaps):
    for website in websites:
        try:
            print(website)
            stream = os.popen('./curltimes.sh compare https://' + website)
            output = stream.read()
            #outmap = parse(output)
            #print(outmap)
            #outmaps[website] = outmap
        except Exception as e:
            print ("Error")

        with open("result.json", 'w') as fp:
            fp.write(json.dumps(outmaps))
'''   
def analysis():

    with open("result.json", 'r') as fd:
        result = json.loads(fd.read())

    with open("1m.json", 'r') as fd:
        ranking = json.loads(fd.read())


def main():
    print("Tool Started!!!")
    print(len(newwebsites))
    websites = []
    filteredWebs = []
    readrandcsv(websites)
    print(websites)
    filterWebs(websites,filteredWebs)
    print(filteredWebs)
    #outmaps = {}
    #readcsv(websites,ranks)
    #print(websites,ranks) #websites
    #print("Num Websites: ", len(websites))
    #runcurl(websites,outmaps)


if __name__ == "__main__":
    # execute only if run as a script
    main()
    #readcsv()