# leelazero_go_selfplay_game_datasets
LeelaZero Go selfplay games are split into single sgf files and classified in weight numbers/hashes.

# prepare files

* unzip xz files
```bash
$ xz -d originFile.sgf.xz
# use -k to keep originFile.sgf.xz not to be deleted
$ xz -d -k originFile.sgf.xz
```
* remove ^M line ending
```bash
$ sed -e 's/^M$//' < originFile.sgf > newFile.sgf
```

* check integrity of sgf game 
```
$ grep ";B" newFile.sgf -n | grep "(;"
# If no error, there is nothing return.
# Show the game which is ending with error: missing ")" or connect next directly
# But we know it couldn't be only missing one symbol, maybe a lot!
```

* split sgf file into small files(exmaple is 6)
```bash
$ split -n6 newFile.sgf
```
  Although we can split file small enough to get scripts running on small memory vps, 
  I recommend no more than 10 and a 8GiB memory machine is cheap for half a day.
  You have to copy & paste those records splitted on file bundary **MANUALLY**.
* my scripts
    * split.py
    * compress.py
    * both can finish in 3min or so on a 4virtualcpu_8gib vps with python3.6
* You can use your scripts to find something.
    * opening style
    * joseki
    * ...
