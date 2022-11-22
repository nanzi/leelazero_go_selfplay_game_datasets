##############  Second Part  ##########################
# Fix all_7M.sgf & all_8M.sgf IntegrityCheck issue in batch.log first then run this script 
#
# nohup python3 sgfcount.py >sgfcount.log 2>&1 &
#
import os
from collections import deque
import re
import time
startTime = time.time()


trimedSGFsFolder = 'mSGFs'
trimedSGFsList = os.listdir('{}/'.format(trimedSGFsFolder))

countNFolder="count"
clip_dir="sgfClips"

if not os.path.exists(countNFolder) :
    os.makedirs(countNFolder)

if not os.path.exists(clip_dir) :
    os.makedirs(clip_dir)


for sgfs_name in trimedSGFsList:
    ### Count game number
    os.system("grep '(;GM' {}/{} -n | grep 'RE' | cut -f1 -d: >{}/{}.txt".format(trimedSGFsFolder, sgfs_name, countNFolder, sgfs_name))
    os.system("sed -n '$=' {}/{} >>{}/{}.txt".format(trimedSGFsFolder, sgfs_name, countNFolder, sgfs_name))

    ### Split into smaller size for less memory burden.

    splitPiece = 20
    end=list(range(splitPiece))

    countFile = countNFolder+"/"+sgfs_name+".txt"
    with open(countFile) as f:
        r  = re.search(r"\d+",str(deque(f,1)))
        print(r.group())
        countTotal = int(r.group())

        for i in range(0,splitPiece):
            end[i] = int(countTotal/splitPiece*min(splitPiece,i+1))

        os.system("sed -n '{},{}p' {}/{} >{}/{}{}".format(1, end[0], trimedSGFsFolder, sgfs_name, clip_dir, sgfs_name,1))

        for i in range(1,splitPiece):
            os.system("sed -n '{},{}p' {}/{} >{}/{}{}".format(end[i-1]+1, end[i], trimedSGFsFolder, sgfs_name, clip_dir, sgfs_name,i+1))
countTime = time.time()
print("--- %s seconds --- counting Finished" % (countTime - startTime))
