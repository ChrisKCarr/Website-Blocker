import time
from datetime import datetime as dt

hosts_temp=r"D:\Dropbox\pp\block_websites\Demo\hosts"
hosts_path=r"C:\Users\carrc\Desktop\CODEING\Complete-Python-Bootcamp-master\Website_Blocker\Hosts"
redirect="127.0.0.1"
website_list=["www.facebook.com","facebook.com","www.Youtube.com","Youtube.com"]

while True:
    if dt(dt.now().year),dt.now().month,dt.now().day,6) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,22):
        print("Working Hours..")
        with open(hosts_temp, 'r') as file:
            content=file.read()
            print(content)
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+website+"\n")
    else:
        with open(hosts_temp,'r+') as file:
            content=file.readline()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print("Free Hours..")
    time.sleep(5)
