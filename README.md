<div align="center">

<p align="center">
简体中文 | <a href="src/docs/README_en.md">English</a>
</p>


<h1><img src="src/images/logo/ticTacToe.ico" alt="" width="48" height="48">AI井字棋</h1>
一个基于AI的井字棋游戏


## 简介
游戏使用人工智能算法模拟人类落子
+ 简单难度：迭代加深搜索
+ 普通难度：极大化极小算法
+ 困难难度：极大化极小算法【剪枝法优化】

## 环境配置
##### 通过pip安装依赖
```bash
pip install -r requirements.txt
```

## 使用说明
##### 1、落子先后手
该游戏中，红叉为先手，蓝圆为后手

##### 2、难度区分
+ 简单难度：AI**无法**考虑到最优解
+ 普通难度：AI**可以**考虑到最优解
+ 困难难度：AI**可以**考虑到最优解，且反应时间**更快**

##### 3、操作延迟
在普通难度下，当AI作为先手进行游戏时，计算时间较长。由于该游戏未采用多线程处理逻辑，因此在运行过程中出现卡顿属于正常现象。

