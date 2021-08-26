import numpy as np
import time

def best_fit_line():

    x = [[1, 0], [1, 1], [1, 2], [1, 3]]
    y = [[0], [1], [4], [9]]
    
    x_transpose = np.transpose(x)
    prev_times_x = np.matmul(x_transpose, x)
    inverse_of_prev = np.linalg.inv(prev_times_x)
    prev_times_transpose = np.matmul(inverse_of_prev, x_transpose)
    
    return np.matmul(prev_times_transpose, y)

start_time = time.time()

for _ in range(10):
    best_fit_line()

end_time = time.time()

print("python time:", (end_time - start_time) / 10)

# sh 001/pseudoinverse/pseudoinverse.sh