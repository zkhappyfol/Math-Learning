import matplotlib.pyplot as plt
import numpy as np

# --- 准备工作 ---
# 定义函数和求导点
def f(x):
    return x**2
x0 = 1
y0 = f(x0)

# 生成函数的x, y坐标用于画图
x_range = np.linspace(-1, 3, 400)
y_range = f(x_range)

# --- 开始画图 ---
plt.figure(figsize=(10, 8))

# 1. 画出原始函数曲线
plt.plot(x_range, y_range, label='$f(x) = x^2$', color='blue', linewidth=2)
plt.scatter(x0, y0, color='red', s=100, zorder=5, label=f'Point A ({x0}, {y0})') # 标出我们的点A

# 2. 画几条不同的割线 (h=1, h=0.5)
for h, color in zip([1, 0.5], ['green', 'orange']):
    x1 = x0 + h
    y1 = f(x1)
    slope = (y1 - y0) / h
    # 用点斜式画出割线 y = m(x-x0) + y0
    secant_line = slope * (x_range - x0) + y0
    plt.plot(x_range, secant_line, '--', label=f'Secant line (h={h})', color=color)
    plt.scatter(x1, y1, color=color, s=50, zorder=5) # 标出点B

# 3. 画出真正的切线
# 我们知道在x=1处，导数(斜率)是2
tangent_slope = 2
tangent_line = tangent_slope * (x_range - x0) + y0
plt.plot(x_range, tangent_line, label='Tangent line (slope=2)', color='red', linewidth=2.5)

# --- 美化图像 ---
plt.title('Secant Lines Approaching the Tangent Line')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(True)
plt.legend()
plt.ylim(-1, 9)
plt.xlim(-1, 3)
plt.show()