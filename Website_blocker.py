import time
from datetime import datetime as dt

hosts_temp="hosts" 
hosts_path=r"C:\Windows\System32\drivers\etc\hosts" #This should be the path to your hosts file on your OS. 
redirect="127.0.0.1"
website_list=["ENTER IN WEBSITE HERE"] 

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,6) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,22):
        #Enter in the times you want the websites to be blocked above, and when they should be unblocked. 
        print("Busy hours..")
        with open(hosts_path, 'r+') as file:
            content=file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+website+"\n")
    else:
        with open(hosts_path, 'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print("Free time..")
    time.sleep(5)
