import numpy as np
import matplotlib.pyplot as plt
from sympy import sympify, symbols, lambdify

# vvvvvvvvvvvvvv  在这里添加下面两行 vvvvvvvvvvvvvv
plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体为黑体
plt.rcParams['axes.unicode_minus'] = False    # 解决保存图像是负号'-'显示为方块的问题
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

def plot_function_and_derivative():
    """
    一个交互式工具，用于接收用户输入的函数字符串，
    然后绘制该函数及其导数的图像。
    """
    # --- 1. 获取用户输入的函数 ---
    user_function_str = input("请输入一个关于x的函数 (例如 x**3 - 3*x 或 sin(x)): ")

    try:
        # --- 2. 使用 SymPy 进行符号数学处理 ---
        # 定义符号 'x'
        x = symbols('x')
        # 将字符串安全地转换为一个数学表达式
        expr = sympify(user_function_str)
        # 自动计算该表达式的导数
        deriv_expr = expr.diff(x)

        print(f"您输入的函数是: f(x) = {expr}")
        print(f"程序计算出的导数是: f'(x) = {deriv_expr}")

        # --- 3. 将符号表达式转换为可用于数值计算的函数 ---
        # 这一步是连接符号数学和数值绘图的关键桥梁
        f = lambdify(x, expr, 'numpy')
        df = lambdify(x, deriv_expr, 'numpy')

        # --- 4. 设置绘图范围和生成数据点 ---
        x_vals = np.linspace(-3, 3, 500)
        y_vals = f(x_vals)
        dy_vals = df(x_vals)

        # --- 5. 使用 Matplotlib 绘图 ---
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10), sharex=True)

        # 绘制原始函数 f(x)
        ax1.plot(x_vals, y_vals, label=f'f(x) = {expr}', color='blue')
        ax1.set_title('原始函数图像 f(x)')
        ax1.set_ylabel('f(x)')
        ax1.grid(True)
        ax1.legend()
        ax1.axhline(0, color='black', linewidth=0.5)

        # 绘制导数函数 f'(x)
        ax2.plot(x_vals, dy_vals, label=f"f'(x) = {deriv_expr}", color='red')
        # 填充导数大于0和小于0的区域
        ax2.fill_between(x_vals, dy_vals, where=(dy_vals > 0), color='green', alpha=0.3, label="f'(x) > 0 (f(x) 递增)")
        ax2.fill_between(x_vals, dy_vals, 0, where=(dy_vals < 0), color='orange', alpha=0.3, label="f'(x) < 0 (f(x) 递减)")
        ax2.set_title("导函数图像 f'(x) - 函数的“坡度地图”")
        ax2.set_xlabel('x')
        ax2.set_ylabel("f'(x)")
        ax2.grid(True)
        ax2.legend()
        ax2.axhline(0, color='black', linewidth=0.5)

        # 显示图像
        plt.tight_layout()
        plt.show()

    except Exception as e:
        print(f"出错了: {e}")
        print("请确保您的函数语法正确，例如使用 '**' 表示乘方，'*' 表示乘法。")

# 运行我们的绘图工具
# 当您在自己的环境中运行时，请确保取消下面这行代码的注释
plot_function_and_derivative()