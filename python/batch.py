# ####  First  #######
# First download xz file into "zipsFolder" folder.
# Other things will automanticly be done.
# You can change folder name accordingly.
# 
# nohup python3 batch.py >> batch.log 2>&1 &
# 
# When finished, you can delete "zipsFolder" "unzipsFolder" folder whose sha256sum had
# been logged.
# Fix files in "trimedSGFsFolder" folder manually with IntegrityCheck report
# 

import os
import time
startTime = time.time()


#########   Data Part   #############
zipsFolder="XZs"
unzipsFolder="SGFs"
trimedSGFsFolder="mSGFs"
zipsList = os.listdir('{}/'.format(zipsFolder)) # get all folder names

if not os.path.exists(unzipsFolder) :
    os.makedirs(unzipsFolder)
if not os.path.exists(trimedSGFsFolder) :
    os.makedirs(trimedSGFsFolder)
    
#count input files, print in the end to verify whether all file are zipped
i = 0 
for xzs_name in zipsList:
    i += 1
    try:
        os.system('xz -d -k {}/{}'.format(zipsFolder,xzs_name))
        os.system('mv {}/{} {}/'.format(zipsFolder,xzs_name[0:-3],unzipsFolder))

        os.system('sha256sum {}/{}'.format(zipsFolder,xzs_name))
        os.system('sha256sum {}/{}'.format(unzipsFolder,xzs_name[0:-3]))

        os.system("tr -d '\r' < {}/{} > {}/{}".format(unzipsFolder,xzs_name[0:-3],trimedSGFsFolder,xzs_name[0:-3]))

        print("unxz&checksum&tr Complete:{}".format(xzs_name))
    except:
        print("{} Problem on filename".format(xzs_name))


print("XZiped Files List:{},check_list:{}".format(len(zipsList),i))# print logs
xzsTime = time.time()
print("--- %s seconds --- File  " % (xzsTime - startTime))


############    IntegrityCheck Part  ##############
#import os
#import time
#startTime = time.time()
sgf_list = os.listdir('{}/'.format(trimedSGFsFolder))

for sgfs_name in sgf_list:
    try:
        os.system("echo '{}'".format(sgfs_name))
        os.system("grep ';B' {}/{} -n | grep '(;'".format(trimedSGFsFolder,sgfs_name))
        print("Game Integrity Check Complete:{}".format(sgfs_name))
    except:
        print("{} Problem on filename".format(sgfs_name))
IntegrityCheckTime = time.time()
print("--- %s seconds --- IntegrityCheck Finished！ " % (IntegrityCheckTime - startTime))



