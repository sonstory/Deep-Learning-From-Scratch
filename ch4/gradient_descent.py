import numpy as np
from gradient import numerical_gradient

def gradient_descent(f, init_x, lr=0.01, step_num=100):
    x = init_x
    
    for i in range(step_num):
        grad = numerical_gradient(f,x)
        x -= lr * grad
    return x

# 경사법으로 f(x0,x1) = x0^2 + x1^2의 최솟값 계산
def function_2(x):
    return x[0]**2 + x[1]**2