# TicTacToe AI
- A simple and elegant GUI to play tictactoe with the computer.
- Main purpose is demonstrate the minimax algorithm and how it choses the optimal path

## Minimax Algorithm
- It is an algorithm which basically just plays all the moves and choses the best suited one after analyzing every move and its future moves till it reaches a terminal state.
- Terminal state is basically win, draw or loss.
- Each state is given points (win=100, draw=0, loss=-100)
- The algorithm calculates moves after going through the path which leads to most points after optimal moves made by computer and player.
- Even though tictactoe has very less combinations compared to other much more complex games I did use memoization and alpha beta pruning to help my understanding of the algorithm

<img width="759" alt="image" src="https://github.com/jenil0108/TicTacToeAI/assets/64329492/9e25fda1-9229-4e9c-8305-ccf1e752bb43">

## Memoization
- The minimax algorithm calculates every single move till terminal state after every move.
- Most of the times the game can reach the same position but in different order of moves.
- To optimize by storing the result we just avoid the redundant calculations of a move's analysis.

## Alpha Beta Pruning
- This is a bit more advanced optimization technique.
- Here if a move leads to immediate win for the opponent in 1 choice we don't need to calculate the others as the opponent will play that only.
- Same goes for the computer if 1 move leads to win no need to calculate the analysis of others.
- This significantly reduces the tree span and optimizes the code exponentially.
