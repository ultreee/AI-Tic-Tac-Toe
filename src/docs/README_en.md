<p align="center">
English | <a href="../../README.md">简体中文</a>
</p>

<h1><img src="../images/logo/ticTacToe.ico" alt="" width="48" height="48">AI Tic-Tac-Toe</h1>
An AI-based tic-tac-toe game.

## Introduction
The game uses artificial intelligence algorithms to simulate human moves.
+ Easy Difficulty: Iterative Deepening Search.
+ Normal Difficulty: Minimax Algorithm.
+ Hard Difficulty: Minimax Algorithm with Pruning Optimization.

## Environment Setup
##### Install dependencies via pip
```bash
pip install -r requirements.txt
```

## Usage Instructions
##### 1、Game Launch
The game entry point is in the game.py file.

##### 2、Move Order
In this game, the red cross moves first, and the blue circle moves second.

##### 3、Difficulty Distinction
+ Easy Difficulty: AI **cannot** consider the optimal solution.
+ Normal Difficulty: AI **can** consider the optimal solution.
+ Hard Difficulty: AI **can** consider the optimal solution, and the response time is **faster**.

##### 4、Operational Delay
At normal difficulty, when AI plays as the first mover, the calculation time is lengthy. Since the game does not employ multi-threading logic, experiencing lag during gameplay is a normal phenomenon.
