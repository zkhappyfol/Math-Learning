import numpy as np

# 1. 定义我们的函数 f(x) = x^2
def f(x):
    return x**2

# 2. 设定我们想要求导的点
x0 = 1

# 3. 设定一个逐渐变小的间隔 h (也就是 Δx)
h_values = [1, 0.1, 0.01, 0.001, 0.0001, 0.00001]

print(f"我们来计算函数 f(x) = x^2 在 x = {x0} 处的导数近似值：\n")

# 4. 用循环来计算当 h 越来越小时，割线的斜率
for h in h_values:
    # 这是导数定义的直接翻译：(f(x+h) - f(x)) / h
    secant_slope = (f(x0 + h) - f(x0)) / h
    print(f"当间隔 h = {h:<10} 时, 割线斜率 ≈ {secant_slope:.5f}")

print("\n结论：随着h无限趋近于0，割线的斜率完美地趋近于 2。")