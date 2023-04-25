#! /bin/python3                                                                                                                                 

import os
import requests
import time
import Secrets

def notif(TEXT,TELEGRAM_API=Secrets.TELEGRAM_API, BOT_TOKEN=Secrets.BOT_TOKEN, CHAT_ID=Secrets.CHAT_ID):

    try:
        link = f"http://{TELEGRAM_API}/bot{BOT_TOKEN}/sendMessage?chat_id={CHAT_ID}&text={TEXT}"
        requests.get(link)
    except Exception as ex:
        print(f"Something went wrong due to :\n{ex}")
        time.sleep(2)
        notif(TEXT)

def server_uptime(IPS=Secrets.IPS, SSH_PORT=Secrets.SSH_PORT, SSH_USER=Secrets.SSH_USER):
    """
    server_uptime gets servers uptime,
    and their hostname via ssh and send 
    them to telegram chat vi telegram api.
    """

    for IP in IPS:
       if IP == "localhost":
           uptime = os.popen("hostname;uptime").read().strip()
       else:
           uptime = os.popen(f"ssh -p {SSH_PORT} {SSH_USER}@{IP} 'hostname;uptime'").read().strip()
       notif(uptime)

if __name__ == '__main__':
    server_uptime()




