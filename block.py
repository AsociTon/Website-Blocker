import time #for delaying the code for set seconds using sleep()
from datetime import datetime as dt #dt is a shorthand for writing datetime.datetime
temp_path = "C:\Windows\System32\drivers\etc\hosts"
temp_host_path = "hosts"
redirect = "127.0.0.1"
block_list = ["facebook.com","www.facebook.com","instagram.com","www.instagram.com"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,7) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,17):
        print("Hey you gotta be in college")
        with open(temp_path,"r+") as file:
            content = file.read()
            for item in block_list:
                 if item in content:
                     print("you are blocked")
                 else:
                     file.write(redirect+" "+item+"\n")
    else:
        temp_content = []
        with open(temp_path,"r+") as file:
            content = file.readlines()
            for line in content:
                if any(site in line for site in block_list):
                    print("item spotted")
                    print(line)
                else:
                    temp_content.append(line)
            content = temp_content
            with open(temp_path,"w") as ptr:
                for i in temp_content:
                    ptr.write(i)
        print("Code Man")
    time.sleep(7)
