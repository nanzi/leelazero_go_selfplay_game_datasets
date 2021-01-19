# leelazero_go_selfplay_game_datasets
LeelaZero Go selfplay games are split into single sgf files and classified in weight numbers/hashes.

## Prepare files

* using [batch.py](python/batch.py)
  * ($ head batch.py) to see instructions
  * main function
    * unzip xz files
    * remove ^M line ending
    * check integrity of sgf game 
  
* Manually fix integrity issues which are list in [batch.log](python/batch.log) in repo or produced by script

* using [sgfcount.py](python/sgfcount.py)
  * ($ head sgfcount.py) to see instructions 
  * main function
    * prepare for splitting in line with sed command
    * split sgf file into small files(5 for now)
    * should use (wc -l count/*.txt) for the last split index
  
* using [split2hash.py](python/split2hash.py)
  * ($ head split2hash.py) to see instructions
  * main function 
    * put each sgf game into its hash named folder (8chars)
    * PB/PW in self-plays are the same
    * PW is more reliable except one missing case in all_2M.sgf

## Static Scripts
* shell scripts
  * stat_opening_hoshi
  * ...


## You can use these public domain files

  * opening style
  * find joseki
  * as you like ...
  * ...
