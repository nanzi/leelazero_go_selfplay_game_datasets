# Fourth Part
#
# nohup python3 split2hash.py >>split2hash.log 2>&1 &
#
# Split sgf clips into single sgf game, into each network-hash named folder
# Manually 1-18
#
import re
import time
import os

startTime = time.time()

clipArray = ""

j = 1 #1

parseNum = 0 #0

outputFolder = "Selfplays"
mainfile = "all_1M.sgf" # CHANGE ME 1M~18M

while j:

    clipArray = "ed/" + mainfile +str(j)
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
        playerB = ""
        subFolderB=""
        gtpVerRaw=""
        gtpVer=""
        CountPW=0
        ParaB=0


        game = collection[i]
        output = str('(;'+game)
        # sgf info placed ....PB[]PW[]RE[]pattern.BUT some of "PB" chars are missing!!
        # USE "PW" is more reliable.
        fileHeadRaw1 = re.split(r'RE',game)
        fileHeadRaw2 = re.split(r'PW',game) 

        fileHead0 = fileHeadRaw1[0]
        CountPW = fileHeadRaw2[0].count("]")
        # #######    Debug Block    ############
        # print(CountPW)
        # print(fileHead0)
        # exit() 

        fileHead = re.split(r"]",fileHead0)

        ParaB = CountPW-1
        if fileHead[CountPW][0:2]=="PW":
            if fileHead[ParaB][-5:]=="Human":
                playerB = "Human"
            elif fileHead[ParaB][-8:]=="networks":
                playerB = fileHead[CountPW][-8:]
            else :
                playerB = str(fileHead[ParaB][-8:])

            gtpVerRaw = re.split(r" ",str(fileHead[ParaB]))
            gtpVer = str(str(gtpVerRaw[-2:-1])[2:6]).strip("'")
        # Code above is missing one thing:
        # Some networkhash is truncated LONGER(many v1M weights) or SHORTER(only v108) than 8 chars!!
        # AND   ../leela hashname which ALSO 8 chars makes the subfolder cd upwards Selfplays folder.
        else:
        #   ### Debug Info ###
            print("This")
            print(game)
            print(fileHead)
            print(ParaB)
            print("is buggy.")
            exit()

        subFolderB = outputFolder + "/" + playerB + "/"

        if not os.path.exists(subFolderB) :
            os.makedirs(subFolderB)

        fileName = playerB+"_"+str(gtpVer)+"_"+str(parseNum+i)+".sgf"
        outputNameB = subFolderB + fileName
        with open(outputNameB, "w") as o:
            o.write(output)
        i+=1
    parseNum += clipLen
    j+=1

print("--- %s seconds ---" % (time.time() - startTime))
print(mainfile)

