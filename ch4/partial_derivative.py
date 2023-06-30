from numerical_diff import numerical_diff

def function_2(x):
    return x[0]**2 + x[1]**2

# x0 = 3, x1 = 4일 때 x0에 대한 편미분
def function_tmp1(x0):
    return x0*x0 + 4.0**2.0

# x0 = 3, x1 = 4일 때 x1에 대한 편미분
def function_tmp2(x1):
    return 3.0**2.0 + x1*x1