from socket import *

def Scan(targetHost,targetPort):
    try:
        connskt= socket(AF_INET, SOCK_STREAM)
        connskt.connect((targetHost, targetPort))
        print('[+]%d/tcp open'% targetPort)
        connskt.close()
    except:
        print('[-]%d/tcp closed'% targetPort)

def portScan(targetHost, targetPorts):
    try:
        targetIP = gethostbyname(targetHost)
    except:
        print('[-] Cannot resolve %s' % targetHost)
        return

    try:
        targetName = gethostbyaddr(targetIP)
        print('\n[+] Scan result of: %s' % targetName[0])
    except:
        print('\n[+] Scan result of: %s' % targetIP)

    setdefaulttimeout(1)
    for targetPort in targetPorts:
        print('Scanning Port: %d'% targetPort)
        Scan(targetHost,int(targetPort))

if __name__ == '__main__':
 portScan('google.com',[7,	
20,	
21,	
22,	
23,	
25,	
53,	
69,	
80,
88,
102,	
110,
135,	
137,	
139,	
143,	
381,
383,
443,	
464,
554,	
465,
587,
593,	
636,	
691,	
902,	
989,	
990,
993,	
995,
1025,
1024,
1194,
1337,	
1589,	
1725,
2082,	
2083,	
2483,
1521,
2484,	
2967,
3074,	
3306,	
3724,	
4664,	
5432,	
5900,	
6665,
6669,	
6881,	
6999,
6970,
8086,	
8087,
8222,
9100,
10000,
12345,
27374,
31337,	])
 Scan("142.251.33.78",80)