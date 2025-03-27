# Parallelized-genetic-algorithms
Improve efficiency by using parallelized genetic algorithms to solve the problems of travel agents.

# 并行遗传算法求解旅行商问题（TSP）

## 介绍
本项目使用并行岛模型遗传算法解决 TSP（旅行商问题）。算法采用轮盘赌选择、部分映射交叉（PMX）和交换变异策略。

## 文件结构
- `main.py`：主程序，负责启动多进程岛模型并行遗传算法。
- `config/`：包含超参数和城市坐标。
- `utils/`：提供路径计算、适应度计算、种群初始化等辅助函数。
- `operators/`：包含选择、交叉、变异操作。
- `algorithms/`：存放遗传算法核心代码。
- `README.md`：项目说明文档。

## 运行方式
`python main.py`

## 结果
程序运行后，将输出最优路径及其对应的总距离。
