##############  Second Part  ##########################
# Fix all_7M.sgf & all_8M.sgf IntegrityCheck issue first then run this script 
#
# python3 sgfcount.py >sgfcount.log 2>&1 &
#
# Since all_7M.sgf has 999999 games after integrity issue fixed,
# sgfcount.py give all_7M.sgf the 1000000th number which IS the file length in line.
# Manually duplicate the 1000000th number as 1000001st in count/all_7M.sgf.txt.

import os
import time
startTime = time.time()
sgf_list = os.listdir('mSGFs/')

count="count"
if not os.path.exists(count) :
    os.makedirs(count)

for sgfs_name in sgf_list:
    os.system("grep '(;GM' mSGFs/{} -n | grep 'RE' | cut -f1 -d: >count/{}.txt".format(sgfs_name,sgfs_name))
    os.system("sed -n '$=' mSGFs/{} >>count/{}.txt".format(sgfs_name,sgfs_name))
countTime = time.time()
print("--- %s seconds --- count Finished" % (countTime - startTime))