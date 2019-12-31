# leelazero_go_selfplay_game_datasets
LeelaZero Go selfplay games are split into single sgf files and classified in weight numbers/hashes.

## Prepare files

* using [batch.py](python/batch.py)
  * unzip xz files
  * remove ^M line ending
  * check integrity of sgf game 

* Manually fix integrity issues which are list in [batch_IntegrityCheck.log](python/batch_IntegrityCheck.log) in repo or in script log

* using [sgfcount.py](python/sgfcount.py)
  * prepare for splitting

* using [sgfclips.py](python/sgfclips.py)
  * split sgf file into small files(5 for now)
  * manually handle big sgf files one by one

* using [split2hash.py](python/split2hash.py)
  * put each sgf game into its hash named folder (8chars)
  * PB/PW in selfplays are the same

## Static Scripts
* shell scripts to come
  * stat_opening_hoshi
  * ...


## You can use these public domain files

  * opening style
  * find joseki
  * as you like ...
  * ...
