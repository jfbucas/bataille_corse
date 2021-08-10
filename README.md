# Bataille Corse Simulator

This is the best card game ever.
 - Quick to learn
 - For all ages
 - Hours of intense fun
 - People can leave or jump in any time
 - Flexible rules
 - Resilient to loss of cards

Description of the game on Wikipedia:
https://fr.wikipedia.org/wiki/Bataille_corse

However, one question remains:
how much does the snap influence the victory?

This little simulation code aims to answer this question.


# The results

## If you don't snap at all

- With 2 players, you still have 5% chance of winning:
  - Jef        has won   5% times and was first to snap   0% of the time
  - Christelle has won  94% times and was first to snap 100% of the time

- With 3 players, about 2% chance of winning
  - Jef        has won   2% times and was first to snap   0% of the time
  - Christelle has won  53% times and was first to snap  49% of the time
  - Sophie     has won  44% times and was first to snap  50% of the time

- With 4 players, about 2% chance of winning
  - Jef        has won   2% times and was first to snap   0% of the time
  - Christelle has won  30% times and was first to snap  33% of the time
  - Sophie     has won  35% times and was first to snap  33% of the time
  - Vincent    has won  31% times and was first to snap  33% of the time



## If you win all the snaps

- With 2 players, you have 95% chance of winning:
  - Jef        has won  95% times and was first to snap 100% of the time
  - Christelle has won   4% times and was first to snap   0% of the time

- With 3 players, about 95% chance of winning
  - Jef        has won  95% times and was first to snap 100% of the time
  - Christelle has won   1% times and was first to snap   0% of the time
  - Sophie     has won   3% times and was first to snap   0% of the time

- With 4 players, about 96% chance of winning
  - Jef        has won  96% times and was first to snap 100% of the time
  - Christelle has won   0% times and was first to snap   0% of the time
  - Sophie     has won   1% times and was first to snap   0% of the time
  - Vincent    has won   1% times and was first to snap   0% of the time 

- With 5 players, about 97% chance of winning
  - Jef        has won  97% times and was first to snap 100% of the time
  - Christelle has won   0% times and was first to snap   0% of the time
  - Sophie     has won   0% times and was first to snap   0% of the time
  - Vincent    has won   0% times and was first to snap   0% of the time
  - Laetitia   has won   1% times and was first to snap   0% of the time


## The Jacks

Instinctively, the Jacks are important.
In fact, the Jacks distribution explain the chances of winning even if you don't snap.
Because of the 1-card contract, the Jacks provide an advantage to whoever owns them at the beginning of the game.

If Jef is given all the Jacks at the beginning:
- He has 21% chance of winning without snapping
  - Jef        has won  21% times and was first to snap   0% of the time
  - Christelle has won  78% times and was first to snap 100% of the time

- He has 78% chance of winning with half of the snaps
  - Jef        has won  78% times and was first to snap  50% of the time
  - Christelle has won  21% times and was first to snap  49% of the time

- He has 100% chance of winning with all the snaps
  - Jef        has won  99% times and was first to snap 100% of the time
  - Christelle has won   0% times and was first to snap   0% of the time
 

## Game duration

The number of turns played is influenced by:
- the number of players
- how close the players are in snapping time

Example with 6 players:
- Jef        has won  17% times and was first to snap  16% of the time
- Christelle has won  16% times and was first to snap  16% of the time
- Sophie     has won  16% times and was first to snap  16% of the time
- Vincent    has won  14% times and was first to snap  16% of the time
- Laetitia   has won  17% times and was first to snap  16% of the time
- Gildas     has won  17% times and was first to snap  16% of the time
- Min/Avg/Max number of turns 108/1127/6409


If one player snaps faster than the other ones, the duration of the game is reduced

Example with 6 players:
- Jef        has won  89% times and was first to snap  68% of the time
- Christelle has won   1% times and was first to snap   6% of the time
- Sophie     has won   1% times and was first to snap   6% of the time
- Vincent    has won   2% times and was first to snap   6% of the time
- Laetitia   has won   1% times and was first to snap   6% of the time
- Gildas     has won   2% times and was first to snap   6% of the time
- Min/Avg/Max number of turns 81/478/2551
