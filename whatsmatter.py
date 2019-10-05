####################################
# Author: Charlie Eliphélé AGOSSOU
####################################

import time
import notify2
import requests
import json
import emojis

def job():    
    global a,n    
    data = requests.get('http://guidos.000webhostapp.com/dqfqfezqfezgrt.php')
    a = json.loads(data.content)    
    n.set_urgency(notify2.URGENCY_NORMAL)
    n.set_timeout(10000)
    n.update(emojis.encode(':bell: #Hackerlab2019: Les Finalistes'), emojis.encode('Numéro '+str(a['users'][-1]['id'])+': '+a['users'][-1]['username']+' est qualifié pour le #Hackerlab2019 :smile:'))        

if __name__ == '__main__':    
    first_content,a = "",""
    notify2.init('Hackerlab2019 Qualifications news')
    n = notify2.Notification(None, icon='')
    data = requests.get('http://guidos.000webhostapp.com/dqfqfezqfezgrt.php')
    first_content = json.loads(data.content)
    while True:
        job()        
        if first_content != a:
            n.show()
            first_content = a        
            time.sleep(1)
