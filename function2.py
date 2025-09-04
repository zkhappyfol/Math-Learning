import numpy as np
import matplotlib.pyplot as plt
from sympy import sympify, symbols, lambdify

# vvvvvvvvvvvvvv  在这里添加下面两行 vvvvvvvvvvvvvv
plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体为黑体
plt.rcParams['axes.unicode_minus'] = False    # 解决保存图像是负号'-'显示为方块的问题
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

def plot_function_and_derivatives_v3():
    """
    升级版V3：增加了二阶导数的计算与可视化。
    """
    user_function_str = input("请输入一个关于x的函数 (例如 x**3 - 3*x): ")

    try:
        x = symbols('x')
        expr = sympify(user_function_str)
        
        # --- 新增：计算一阶和二阶导数 ---
        deriv1_expr = expr.diff(x)
        deriv2_expr = deriv1_expr.diff(x) # 对一阶导数再求一次导

        print(f"函数: f(x) = {expr}")
        print(f"一阶导数: f'(x) = {deriv1_expr}")
        print(f"二阶导数: f''(x) = {deriv2_expr}")

        f = lambdify(x, expr, 'numpy')
        df1 = lambdify(x, deriv1_expr, 'numpy')
        df2 = lambdify(x, deriv2_expr, 'numpy') # 新增二阶导数的数值函数

        x_vals = np.linspace(-4, 4, 500) # 优化一下范围以便观察
        y_vals = f(x_vals)
        dy1_vals = df1(x_vals)
        dy2_vals = df2(x_vals) # 新增二阶导数的y值

        # --- 修改：创建3个子图 ---
        fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 15), sharex=True)

        # 1. 绘制原始函数 f(x)
        ax1.plot(x_vals, y_vals, label=f'f(x) = {expr}', color='blue')
        ax1.set_title('原始函数图像 f(x)')
        ax1.set_ylabel('f(x)')
        ax1.grid(True)
        ax1.legend()
        ax1.axhline(0, color='black', linewidth=0.5)

        # 2. 绘制一阶导数 f'(x)
        ax2.plot(x_vals, dy1_vals, label=f"f'(x) = {deriv1_expr}", color='red')
        ax2.fill_between(x_vals, dy1_vals, 0, where=(dy1_vals > 0), color='green', alpha=0.3, label="f'(x) > 0 (递增)")
        ax2.fill_between(x_vals, dy1_vals, 0, where=(dy1_vals < 0), color='orange', alpha=0.3, label="f'(x) < 0 (递减)")
        ax2.set_title("一阶导数 f'(x) - “坡度地图”")
        ax2.set_ylabel("f'(x)")
        ax2.grid(True)
        ax2.legend()
        ax2.axhline(0, color='black', linewidth=0.5)
        
        # --- 新增：绘制二阶导数图像 f''(x) ---
        ax3.plot(x_vals, dy2_vals, label=f"f''(x) = {deriv2_expr}", color='purple')
        ax3.fill_between(x_vals, dy2_vals, 0, where=(dy2_vals > 0), color='cyan', alpha=0.3, label="f''(x) > 0 (开口向上 ∪)")
        ax3.fill_between(x_vals, dy2_vals, 0, where=(dy2_vals < 0), color='magenta', alpha=0.3, label="f''(x) < 0 (开口向下 ∩)")
        ax3.set_title("二阶导数 f''(x) - “弯曲方向地图”")
        ax3.set_xlabel('x')
        ax3.set_ylabel("f''(x)")
        ax3.grid(True)
        ax3.legend()
        ax3.axhline(0, color='black', linewidth=0.5)

        plt.tight_layout()
        plt.show()

    except Exception as e:
        print(f"出错了: {e}")
        print("请确保您的函数语法正确。")

# 运行V3版的绘图工具
# 当您在自己的环境中运行时，请确保取消下面这行代码的注释
plot_function_and_derivatives_v3()