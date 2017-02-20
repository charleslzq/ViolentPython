from socket import *
from threading import Thread, Semaphore

screen_lock = Semaphore(value=1)


def conn_scan(tgt_host, tgt_port):
    try:
        conn_skt = socket(AF_INET, SOCK_STREAM)
        conn_skt.connect((tgt_host, tgt_port))
        conn_skt.send('ViolentPython\r\n')
        results = conn_skt.recv(100)
        screen_lock.acquire()
        print('[+]%d/tcp open' % tgt_port)
        print('[+] ' + str(results))
        conn_skt.close()
    except:
        screen_lock.acquire()
        print('[-]%d/tcp closed' % tgt_port)
    finally:
        screen_lock.release()
        conn_skt.close()


def port_scan(tgt_host, tgt_ports):
    try:
        tgt_ip = gethostbyname(tgt_host)
    except:
        print("[-] Cannot resolve '%s': Unknown host" % tgt_host)
        return
    try:
        tgt_name = gethostbyaddr(tgt_ip)
        print('\n[+] Scan Results for: ' + tgt_name[0])
    except:
        print('\n[+] Scan Result for: ' + tgt_ip)
    setdefaulttimeout(1)
    for tgt_port in tgt_ports:
        print('Scanning port ' + tgt_port)
        thread = Thread(target=conn_scan, args=(tgt_host, int(tgt_port)))
        thread.start()
