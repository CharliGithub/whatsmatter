####################################
# Author: Eliphélé Charlie AGOSSOU
# Mail: charliepy007@gmail.com
####################################

import sys
import time
import notify2
import requests
import json
import emojis
from requests.exceptions import ConnectionError, Timeout

def job():    
    global a,n,url    
    try:
        data = requests.get(url,timeout=45)
    except (ConnectionError, Timeout) as e:
        print("Can't reach hackerlab results. Please visit http://qualif.hackerlab.bj/resultats.html")
        sys.exit() 
    try:
        a = json.loads(data.content)    
    except ValueError as e:    
        print("Can't reach hackerlab results. Please visit http://qualif.hackerlab.bj/resultats.html")
        sys.exit()
    n.set_urgency(notify2.URGENCY_NORMAL)
    n.set_timeout(10000)
    n.update(emojis.encode(':bell: #Hackerlab2019: Les Finalistes'), emojis.encode('Numéro '+str(a['users'][-1]['id'])+': '+str(a['users'][-1]['username']).capitalize()+' est qualifié pour le #Hackerlab2019 :smile:'))        

if __name__ == '__main__':
    banner = """
    __        ___           _       __  __       _   _            
    \ \      / / |__   __ _| |_ ___|  \/  | __ _| |_| |_ ___ _ __ 
     \ \ /\ / /| '_ \ / _` | __/ __| |\/| |/ _` | __| __/ _ \ '__|
      \ V  V / | | | | (_| | |_\__ \ |  | | (_| | |_| ||  __/ |   
       \_/\_/  |_| |_|\__,_|\__|___/_|  |_|\__,_|\__|\__\___|_|   
                                                                  
    """
    print(banner)
    print("\033[32m[+] \033[0mProgram has started ....  \033[93mDon't close the terminal !\033[0m")
    first_content,a,url = "","",'http://qualif.hackerlab.bj/dqfqfezqfezgrt.php'    
    try:
        data = requests.get(url,timeout=45)
    except (ConnectionError, Timeout) as e:
        print("Can't reach hackerlab results. Please visit http://qualif.hackerlab.bj/resultats.html")
        sys.exit()        
    try:
        first_content = json.loads(data.content)
    except ValueError as e:
        print("Can't reach hackerlab results. Please visit http://qualif.hackerlab.bj/resultats.html")
        sys.exit()        
    notify2.init('Hackerlab2019 Qualifications news')
    n = notify2.Notification(None)   

    while True:
        job()        
        if first_content != a:
            n.show()
            first_content = a
        time.sleep(30)
