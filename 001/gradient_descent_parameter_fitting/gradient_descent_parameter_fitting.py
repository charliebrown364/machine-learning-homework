import time

alpha = 0.001
delta = 0.01
num_iterations = 10000
points = [[0, 0], [1, 1], [2, 4]]
starting_point = [0, 2]

def rss(b_0, b_1):
    rss = 0
    for point in points:
        rss += (b_0 + b_1 * point[0] - point[1]) ** 2
    return rss

def gradient_descent_parameter_fitting():
    b_0, b_1 = starting_point
    for _ in range(num_iterations):
        b_0 -= alpha * (rss(b_0 + delta, b_1) - rss(b_0 - delta, b_1)) / (2 * delta)
        b_1 -= alpha * (rss(b_0, b_1 + delta) - rss(b_0, b_1 - delta)) / (2 * delta)

start_time = time.time()

for _ in range(10):
    gradient_descent_parameter_fitting()

end_time = time.time()

print((end_time - start_time) / 10)