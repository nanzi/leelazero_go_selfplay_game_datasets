# Third part
# 
# nohup python3 sgfclips.py >>sgfclips.log 2>&1 &
#
# manually 1-18
# 
import os
import time
i = 0 #count infile, print in the end to verify wheather all file zipped
num1=0
num1_1= 0
num2= 0
num2_1= 0
num3= 0
num3_1= 0
num4= 0
num4_1= 0
num5 = 0
startTime = time.time()
sgf_dir = 'mSGFs'
count_dir= 'count'
clip_dir="sgfClips"

if not os.path.exists(clip_dir) :
    os.makedirs(clip_dir)

fileNameRaw = "all_1M.sgf" # Change ME 1M~18M remember all_7M num5 issue and all_8M integratycheck
fileName = sgf_dir+"/"+fileNameRaw
countName = count_dir+"/"+fileNameRaw+".txt"
with open(countName) as f:
    content = f.readlines()
for line in content:
    i += 1
    if i == 200000:
        num1 = int(line)
        num1_1 = num1-1
    if i == 400000:
        num2 = int(line)
        num2_1 = num2-1
    if i == 600000:
        num3 = int(line)
        num3_1 = num3-1
    if i == 800000:
        num4 = int(line)
        num4_1 = num4-1
    if i == 1000001:		# change this number with "wc -l count/*.sgf.txt"
        num5 = int(line)

os.system("sed -n '{},{}p' {}/{} >{}/{}1".format(1,   num1_1,sgf_dir,fileNameRaw,clip_dir,fileNameRaw))
os.system("sed -n '{},{}p' {}/{} >{}/{}2".format(num1,num2_1,sgf_dir,fileNameRaw,clip_dir,fileNameRaw))
os.system("sed -n '{},{}p' {}/{} >{}/{}3".format(num2,num3_1,sgf_dir,fileNameRaw,clip_dir,fileNameRaw))
os.system("sed -n '{},{}p' {}/{} >{}/{}4".format(num3,num4_1,sgf_dir,fileNameRaw,clip_dir,fileNameRaw))
os.system("sed -n '{},{}p' {}/{} >{}/{}5".format(num4,num5,  sgf_dir,fileNameRaw,clip_dir,fileNameRaw))

splitTime = time.time()
print("--- %s seconds --- split Finished" % (splitTime - startTime))

