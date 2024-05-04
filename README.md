# modelForYakris

some codes for a small modeling question

这是对一道数学建模题目的代码尝试，此处用作记录总结（以及github使用的练习）

整体基本上是很暴力的尝试用python模拟了一下 $10 \times 10$ 的棋格上的海战棋中玩家的行为。从最简单的无策略随机抽取到使用了一些简单策略的抽取，重复试验并计算玩家击沉所有舰船时的平均步数。（也尝试了能不能画出来一次试验中模拟玩家的具体行动（但是因为一些原因放弃了

背景信息等等来自一道国内的数学建模题目。（但除了Set00,Set01,Set03之外其实并没有尝试解决这道题目?

testGrid对应没有策略的随机抽取。

testGridSt1对应在命中之后优先搜索四周的简单策略

testGridSt2对应在命中之后首先搜索四周，出现第二次命中后确定舰船可能存在的方向并直线扫描直到落空的简单策略

testGridSt3在St2的基础之上增加了一些额外的舰船生成规则，包括了一艘舰船的格点周围的8个格点均不可布置其他舰船格点的情况

Set00,Set01,Set03考虑了一些固定的舰船排布的试验

这些尝试均没有进行任何的后续分析与理论分析（在写下这一段的时候应当算是并没有稍稍深入的接触过一点点Markov链之外的随机过程...虽然Markov学的也不够深入emm