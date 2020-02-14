import glob, os, shutil
from datetime import datetime


today = datetime.now()
test = "/Users/jordan/Google Drive/FT/" + today.strftime('%Y'+'-'+'%m'+'-'+'%d')

try:
    os.mkdir(test)
    for i in glob.glob('/Users/jordan/Documents/*.html'):
        # shutil.copy(i, test)
        shutil.move(i, test)
except:
    pass
