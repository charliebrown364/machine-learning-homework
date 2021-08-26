import time

def f(x, y):
    return 1 + 2*x**2 + 3*y**2

def new_x(x, y, alpha, delta):
    central_diff_quotient = (f(x + delta / 2, y) - f(x - delta / 2, y)) / delta
    return x - alpha * central_diff_quotient

def new_y(x, y, alpha, delta):
    central_diff_quotient = (f(x, y + delta / 2) - f(x, y - delta / 2)) / delta
    return y - alpha * central_diff_quotient

def gradient_descent_minimization(starting_point, num_updates, alpha, delta):
    
    x, y = starting_point
    
    for _ in range(num_updates):
        x = new_x(x, y, alpha, delta)
        y = new_y(x, y, alpha, delta)

start_time = time.time()

for _ in range(10):
    gradient_descent_minimization([1, 2], 2, 0.001, 0.01)

end_time = time.time()

print((end_time - start_time) / 10)