##############  Second Part  ##########################
# Fix all_8M.sgf & all_9M.sgf IntegrityCheck issue in batch.log first then run this script 
#
# python3 sgfcount.py >sgfcount.log 2>&1 &
#

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
