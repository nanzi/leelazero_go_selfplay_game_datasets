# 2. Manual Part
#
# nohup python3 split2hash.py >>split2hash.log 2>&1 &
#
# Split sgf clips into single sgf game, into each network-hash named folder
# Manually 1-20...
#
import re
import time
import os

startTime = time.time()

clipArray = ""

j = 1

parseNum = 0
clip_dir="sgfClips" #ref to sgfclips.py

outputFolder = "Selfplays"

if not os.path.exists(outputFolder) :
    os.makedirs(outputFolder)
    
labelM = "1M" # CHANGE ME  1M~20M... and so on (tar file location of games) 

mainfile = "all_"+labelM+".sgf"

while j:

    clipArray = clip_dir+"/" + mainfile +str(j) 
    if not os.path.exists(clipArray):
        break
    print("--- %s seconds --- clip : %s" % ((time.time() - startTime),j))
    
    
    with open(clipArray) as f:
        file = f.read()
    collection = file.split('(;')
    clipLen=len(collection)
    i = 1

    while i<clipLen:
        output =""
        outputName =""
        fileHeadRaw=""
        fileHead =""
        player = ""
        subFolderBlack=""
        gtpVerRaw=""
        gtpVer=""
        CountPW=0
        ParameterPB=0

        game = collection[i]
        output = str('(;'+game)
        # sgf info placed ....PB[]PW[]RE[]pattern.BUT some of "PB" chars are missing!!
        # USE "PW" is more reliable. Exception: all_2M.sgf line 10814273
        fileHeadRE = re.split(r'RE',game)
        fileHeadPW = re.split(r'PW',game) 

        fileHeadInfo = fileHeadRE[0]
        CountPW = fileHeadPW[0].count("]")
        # #######    Debug Block    ############
        # print(CountPW)
        # print(fileHead0)
        # exit() 

        gameInfo = re.split(r"]",fileHeadInfo)

        ParameterPB = CountPW-1
        if gameInfo[CountPW][0:2]=="PW": #  need to locate and fix broken sgf record with (grep "7ba9d22c\]PB\[" mSGFs/all_2M.sgf -n)
            if gameInfo[ParameterPB][-5:]=="Human":
                player = "Human"
            elif gameInfo[ParameterPB][-8:]=="networks":
                player = gameInfo[CountPW][-8:]
            else :
                player = str(gameInfo[ParameterPB][-8:])

            gtpVerRaw = re.split(r" ",str(gameInfo[ParameterPB]))
            gtpVer = str(str(gtpVerRaw[-2:-1])[2:6]).strip("'")
        # Code above miss some corner cases:
        # Some networkhash is truncated LONGER(many v1M weights) or SHORTER(only v108) than 8 chars!!
        # AND   ../leela hashname which ALSO 8 chars makes the subfolder change directory upwards Selfplays folder.
        else:
        #   ### Debug Info ###
            print("This")
            print(game)
            print(gameInfo)
            print(ParameterPB)
            print("is buggy.")
            exit()

        subFolderBlack = outputFolder + "/" + player + "/"

        if not os.path.exists(subFolderBlack) :
            os.makedirs(subFolderBlack)

        fileName = player+"_"+str(gtpVer)+"_"+labelM+"_"+str(parseNum+i)+".sgf"
        outputNameB = subFolderBlack + fileName
        with open(outputNameB, "w") as o:
            o.write(output)
        i+=1
    parseNum += clipLen
    j+=1

print("--- %s seconds ---" % (time.time() - startTime))
print(mainfile)

