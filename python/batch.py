# ####  First  #######
# First download xz file into "XZs" folder.
# Other things will automanticly be done.
# You can change folder name accordingly.
# 
# nohup python3 batch.py >> batch.log 2>&1 &
# 
# When finished, you can delete "XZs" "SGFs" folder whose sha256sum had been logged.
# Fix files in "mSGFs" folder manually with IntegrityCheck report
# 

import os
import time

#########   Data Part   #############
xzs_list = os.listdir('XZs/') # get all folder names
i = 0 #count infile, print in the end to verify wheather all file zipped
startTime = time.time()
SGFs="SGFs"
mSGFs="mSGFs"

if not os.path.exists(SGFs) :
    os.makedirs(SGFs)
if not os.path.exists(mSGFs) :
    os.makedirs(mSGFs)

for xzs_name in xzs_list:
    i += 1
    try:
        os.system('xz -d -k XZs/{}'.format(xzs_name))
        os.system('mv XZs/{} SGFs/'.format(xzs_name[0:-3]))

        os.system('sha256sum XZs/{}'.format(xzs_name))
        os.system('sha256sum SGFs/{}'.format(xzs_name[0:-3]))

        os.system("tr -d '\r' < SGFs/{} > mSGFs/{}".format(xzs_name[0:-3],xzs_name[0:-3]))

        print("unxz&checksum&tr Complete:{}".format(xzs_name))
    except:
        print("{} Problem on filename".format(xzs_name))


print("xzs_list:{},check_list:{}".format(len(xzs_list),i))# print logs
xzsTime = time.time()
print("--- %s seconds --- File  " % (xzsTime - startTime))


############    IntegrityCheck Part  ##############
#import os
#import time
#startTime = time.time()
sgf_list = os.listdir('mSGFs/')

for sgfs_name in sgf_list:
    try:
        os.system("echo '{}'".format(sgfs_name))
        os.system("grep ';B' mSGFs/{} -n | grep '(;'".format(sgfs_name))
        print("Game Integrity Check Complete:{}".format(sgfs_name))
    except:
        print("{} Problem on filename".format(sgfs_name))
IntegrityCheckTime = time.time()
print("--- %s seconds --- IntegrityCheck Finished！ " % (IntegrityCheckTime - startTime))



