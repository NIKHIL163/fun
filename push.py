import os
import datetime

print("\x1B[9m \x1B[40m \x1B [32m")
    
def fileing(i):
    withopen ("Readme.md","w")   
    file.close()

def load():
    start_date = datetime.date (2022, 1, 1)
    end_date = datetime.date (2022, 12, 1)
    delta = datetime.timedelta(days=1)

while(start_date <= end_date):
    start_date +=delta
    mydate = start_date.strftime('%a %d %b %Y')
    print(mydate)
    fileing(mydate)
    os.system("git add .")
    os.system("git commit --date=\"{} 10:00 2023 +05\" -m GitHub-fun".format(mydate))



for i in range (1):
    load()

os.system("git push -f origin master")