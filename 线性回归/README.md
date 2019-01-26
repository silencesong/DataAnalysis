## 01.使用梯度下降方法实现线性回归

### 过程

1. 读取训练集的输入数据和输出数据
2. 设定初始模型:y=x+1
3. 根据预测函数y=w0+w1x，记录此次迭代损失值
4. 求损失函数关于w0和w1的偏导数，计算产生下一次迭代的w0和w1
5. 迭代循环1000次，重复3、4步骤
6. 用训练集作为测试集计算实际的预测输出，和实际输出比较
  5.0 -> 5.197342694662536
  5.5 -> 5.423697847192317
  6.0 -> 5.876408152251877
  6.8 -> 6.5554736098412185
  7.0 -> 7.2345390674305605
  
7. 绘制回归曲线，测试值(训练值)和预测值的散点图
![](https://github.com/silencesong/DataAnalysis/blob/master/%E7%BA%BF%E6%80%A7%E5%9B%9E%E5%BD%92/Images/myplot.png)

8. 可视化梯度下降过程中的w0,w1和loss的训练过程
![](https://github.com/silencesong/DataAnalysis/blob/master/%E7%BA%BF%E6%80%A7%E5%9B%9E%E5%BD%92/Images/myplot2.png)

9. 可视化损失函数曲面

![](https://github.com/silencesong/DataAnalysis/blob/master/%E7%BA%BF%E6%80%A7%E5%9B%9E%E5%BD%92/Images/myplot3.png)

### 结论：
1. 从可视化图中可以看出，使用梯度下降的计算方法，迭代1000次后，损失值loss降为0.08742142。
2. 从w0,w1和loss的训练过程中可以看出，前20次迭代loss下降频率很快，之后下降趋于平缓
3. 可以从损失函数曲面上看出梯度下降的路线，损失值越来越小

