#import the built in library datetime..
from datetime import datetime

#setting the end time to 24-05-2021 at 8:00PM
endTime = datetime(2021,5,24,20)

#Lists to sites You want to block...
#BlockSites = ['www.facebook.com','facebook.com','twitter.com','www.twitter.com']

#storing the hosts.txt file path into a variable and mapping it to IP address redirect
hostFilePath = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"

def BlockSites():
    if datetime.now() < endTime:
        print("The WebSite is Blocked...")
        with open(hostFilePath,'r+') as hostfile:
            hostcontent = hostfile.read()
            for sites in BlockSites:
                if sites not in hostcontent:
                    hostfile.write(redirect+" " + sites + "\n")
    else:
        print("Unblocking WebSites...")
        with open(hostFilePath,'r+') as hostfile:
            lines = hostfile.readlines()
            hostfile.seek(0)
            for line in lines:
                if not any(site in line for site in BlockSites):
                    hostfile.write(line)
            hostfile.truncate()

if __name__ == "__main__":
    BlockSites()
            
