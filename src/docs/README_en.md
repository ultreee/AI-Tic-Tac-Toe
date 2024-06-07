<div align="center">

<div align="center">

<p align="center">
English | <a href="../../README.md">简体中文</a>
</p>

<h1><img src="../images/logo/ticTacToe.ico" alt="" width="48" height="48">AI Tic-Tac-Toe</h1>
An AI-based tic-tac-toe game

## Introduction
The game uses artificial intelligence algorithms to simulate human moves
+ Easy Difficulty: Iterative Deepening Search
+ Normal Difficulty: Minimax Algorithm
+ Hard Difficulty: Minimax Algorithm with Pruning Optimization

## Environment Setup
##### Install dependencies via pip
```bash
pip install -r requirements.txt
```

## Usage Instructions
##### 1、Move Order
In this game, the red cross goes first, and the blue circle goes second.

##### 2、Difficulty Distinction
+ Easy Difficulty: AI **cannot** consider the optimal solution
+ Normal Difficulty: AI **can** consider the optimal solution
+ Hard Difficulty: AI **can** consider the optimal solution, and the response time is **faster**

##### 3、Operational Delay
At normal difficulty, when AI plays first, the calculation time is lengthy. Since the game does not employ multi-threading logic, experiencing lag during gameplay is a normal phenomenon.
