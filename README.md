# leelazero_go_selfplay_game_datasets
LeelaZero Go selfplay games are split into single sgf files and classified in weight numbers/hashes.

## Prepare files

* unzip xz files
```bash
# decompress xz file
$ xz -d originFile.sgf.xz
# use -k to keep originFile.sgf.xz not to be deleted
$ xz -d -k originFile.sgf.xz
```
* remove ^M line ending
```bash
$ sed -e 's/^M$//' < originFile.sgf > newFile.sgf
```

* check integrity of sgf game 
```bash
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
  I recommend no more than 10 clips on your own PC, 
  or on a 8GiB memory machine which is economic for a few hours.
  
  You have to **COPY & PASTE** those records splitted on file bundary **MANUALLY**.
* scripts in this repo
  * python
    * [split](python/split.py)
    * [compress](python/compress.py)
  * shell
    * [stat_opening_hoshi](shell/stat_opening_hoshi.sh)
  * ...


## You can use these public domain files

  * opening style
  * find joseki
  * as you like ...
  * ...
