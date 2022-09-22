import pywhatkit
import time
from datetime import datetime

#################################### PRE CFG
#group = "DdLx7QOywjKDM2E0EKoVQW" Los Pibes ID
#pywhatkit.sendwhatmsg_to_group(group,msg,hour,minute)
currentDateAndTime = datetime.now()
hour = currentDateAndTime.hour
minute = currentDateAndTime.minute+1

messages = ["Hola Gato Automatizado.", "Qué mirás?"]

phone_numbers = [5491135125222, 5491130493680]

for nmbr in phone_numbers:
    for msg in messages:
        currentDateAndTime = datetime.now()
        hour = currentDateAndTime.hour
        minute = currentDateAndTime.minute+1
        try:
            pywhatkit.sendwhatmsg("+"+str(nmbr),msg,hour,minute)
            print("Successfully Sent!")
            
        
        except: # handling exception
            print("An Unexpected Error!")
    time.sleep(1) # For safety
