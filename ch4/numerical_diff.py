import numpy as np
import matplotlib.pyplot as plt

# 나쁜 구현의 예
def numerical_diff_bad(f,x):
    h = 1e-50
    return (f(x+h)-f(x)) / h

# 개선한 수치 미분 함수
def numerical_diff(f, x):
    h = 1e-4
    return (f(x+h)-f(x-h)) / (2*h)

# 수치 미분의 예
def function_1(x):
    return 0.01*x**2 + 0.1*x