# Last Part
# All things done!
# 
# nohup python3 compress.py >compress.log 2>&1 &
#
import os
import time
startTime = time.time()

dir_list = os.listdir('./Selfplays') # get all folder names
i = 0#count infile, print in the end to verify wheather all file zipped
for dir_name in dir_list:
	i += 1
	try:
		os.system('tar -czf ./Selfplays/{}.tar.gz ./Selfplays/{}/'.format(dir_name, dir_name))
		print("Compression Complete:{}".format(dir_name))
	except:
		print("{} Problem on filename".format(dir_name))

print("dir_list:{},tar_list:{}".format(len(dir_list),i))# print logs

compressTime = time.time()
print("--- %s seconds --- split Finished" % (compressTime - startTime))
