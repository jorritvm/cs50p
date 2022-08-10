# BLACKJACK for CS50P
#### Video Demo: you can watch my final presentation [video on youtube](https://youtu.be/TrvIpftLfYw)

## Goal
The goal is to build a command-line blackjack game as a final project for the CS50P course
The project demonstrates the use of:
- control structures
- 3rd party libraries
- OOP
- testing with pytest

## Rules of the game
### Goal
The player plays alone versus the house. They attempt to beat the dealer at getting a count as close to 21 as possible, without going over 21.

### Betting
Betting is done before the cards are dealt. The player start with $1000 on hand. They must bet a minimum of $1 before the round starts.

### Dealing the cards
The cards are shuffled.
You get dealt 2 cards face up. The dealer get's dealt 1 card face up and one card face down.

### The player's play
It is up to each individual player if an ace is worth 1 or 11. Face cards are 10 and any other card is its pip value. If an ace is worth 1 the hand is called a soft hand. If it is worth 11 the hand is called a hard hand.

The player goes first and must decide whether to **"stand"** (not ask for another card) or **"hit"** (ask for another card in an attempt to get closer to a count of 21, or even hit 21 exactly). A player can go **"bust"** if their count is over 21.

### The dealer's play
When the dealer has served the player, the dealers face-down card is turned up. If the total is 17 or more, the dealer must stand. If the total is 16 or under, they must take a card. The dealer must continue to take cards until the total is 17 or more, at which point the dealer must stand.

If the dealer has an ace, and counting it as 11 would bring the total to 17 or more (but not over 21), the dealer must count the ace as 11 and stand. As such, the game does not follow the 'must hit on soft 17 rule'.

The dealer's decisions are automatic on all plays, whereas the player always has the option of taking one or more cards.

### The winner
- If only the player goes bust, the player loses his bet.
- If both the player and the dealer go bust, the player loses his bet.
- If only the dealer goes bust, the player wins and receives the same amount as his bet.
- If the player has a closer count to 21 than the dealer, the player wins and receives the same amount as his bet.
- If the dealer has a closer count to 21 than the player, the player loses his bet.
- If both the dealer and player have the same count, it is a **stand-off** and the player's bet returns to his purse.

### Game over
If the player's purse is spent, it's game over.

## Features of the game that are not implemented
The implementation does not include:
- splitting pairs
- doubling down
- insurance

For more details on these blackjack techniques, consult google.

## How to play
- make sure you have pip installed the required dependencies
- run ```python project.py``` from the commandline

## Parting words
Have fun, don't lose all your money! And ff you do, don't worry ,it's only 1's and 0's.