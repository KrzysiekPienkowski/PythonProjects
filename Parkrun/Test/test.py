import os
import urllib
import webbrowser
import urllib.parse
import urllib.request


from datetime import date
today = date.today()

# define the name of the directory to be created
parkrunHome = "C:/Users/Maja/Desktop/PARKRUN/"
path = today.strftime(parkrunHome+"%d.%m.%Y")

try:
    os.makedirs(path)
except OSError:
    print ("Creation of the directory %s failed" % path)
else:
    print ("Successfully created the directory %s " % path)

os.system("start \"\" https://webfms-production.parkrun.com/")

