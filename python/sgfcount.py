##############  Second Part  ##########################
# Fix all_7M.sgf & all_8M.sgf IntegrityCheck issue in batch.log first then run this script 
#
# nohup python3 sgfcount.py >sgfcount.log 2>&1 &
#
import mmap
import os
from past.builtins import xrange

def tail(filename, n):
    """Returns last n lines from the filename. No exception handling"""
    size = os.path.getsize(filename)
    with open(filename, "rb") as f:
        # for Windows the mmap parameters are different
        fm = mmap.mmap(f.fileno(), 0, mmap.MAP_SHARED, mmap.PROT_READ)
        try:
            for i in xrange(size - 1, -1, -1):
                if fm[i] == '\n':
                    n -= 1
                    if n == -1:
                        break
            return fm[i + 1 if i else 0:].splitlines()
        finally:
            fm.close()

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

    splitPiece = 5
    start1,end1,start2,end2,start3,end3,start4,end4,start5,end5 = 1,0,0,0,0,  0,0,0,0,0
    
    countFile = countNFolder+"/"+sgfs_name+".txt"
    countTotal = int(tail(countFile,1))
    end1 = int(countTotal/splitPiece)
	
    start2 = end1+1
    end2 = int(countTotal/splitPiece*min(splitPiece,2))
	
    start3 = end2+1
    end3 = int(countTotal/splitPiece*min(splitPiece,3))

    start4 = end3+1
    end4 = int(countTotal/splitPiece*min(splitPiece,4))
	
    start5 = end4+1
    end5 = int(countTotal)#/splitPiece*min(splitPiece,5))


    os.system("sed -n '{},{}p' {}/{} >{}/{}1".format(start1, end1, trimedSGFsFolder, sgfs_name, clip_dir, sgfs_name))
    os.system("sed -n '{},{}p' {}/{} >{}/{}2".format(start2, end2, trimedSGFsFolder, sgfs_name, clip_dir, sgfs_name))
    os.system("sed -n '{},{}p' {}/{} >{}/{}3".format(start3, end3, trimedSGFsFolder, sgfs_name, clip_dir, sgfs_name))
    os.system("sed -n '{},{}p' {}/{} >{}/{}4".format(start4, end4, trimedSGFsFolder, sgfs_name, clip_dir, sgfs_name))
    os.system("sed -n '{},{}p' {}/{} >{}/{}5".format(start5, end5, trimedSGFsFolder, sgfs_name, clip_dir, sgfs_name))
countTime = time.time()
print("--- %s seconds --- counting Finished" % (countTime - startTime))
