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

def job():    
    global a,n    
    data = requests.get('http://guidos.000webhostapp.com/dqfqfezqfezgrt.php')
    try:
        a = json.loads(data.content)    
    except JSONDecodeError as e:
        print("Can't reach hackerlab results")
        sys.exit()
    n.set_urgency(notify2.URGENCY_NORMAL)
    n.set_timeout(10000)
    n.update(emojis.encode(':bell: #Hackerlab2019: Les Finalistes'), emojis.encode('Numéro '+str(a['users'][-1]['id'])+': '+a['users'][-1]['username']+' est qualifié pour le #Hackerlab2019 :smile:'))        

if __name__ == '__main__':    
    first_content,a = "",""
    data = requests.get('http://guidos.000webhostapp.com/dqfqfezqfezgrt.php')
    if data.status_code != 200: 
        print("Can't reach hackerlab results")
        sys.exit()
    else:
        try:
            first_content = json.loads(data.content)
        except JSONDecodeError as e:
            print("Can't reach hackerlab results")
            sys.exit()        
        notify2.init('Hackerlab2019 Qualifications news')
        n = notify2.Notification(None,icon='')   

    while True:
        job()        
        if first_content != a:
            n.show()
            first_content = a        
            time.sleep(1)
