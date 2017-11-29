import time
from datetime import datetime as dt

host_path = "/etc/hosts"
temp_host_path = "hosts"
redirect_ip = "8.8.8.8"
website_list = ["facebook.com", "www.facebook.com"]

#Frequency of the time check in seconds.
check_frequency = 300

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 16):
        print ("Working Hours")
        with open(temp_host_path, 'r+') as hostFile:
            content = hostFile.read()

            for website in website_list:
                if website in content:
                    pass
                else:
                    hostFile.write(redirect_ip + " " + website +"\n")

    else:
        print ("Fun Hours")
        with open(temp_host_path, 'r+') as hostFile:
            content = hostFile.readlines()
            hostFile.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    hostFile.write(line)
            hostFile.truncate()

    time.sleep(check_frequency)
