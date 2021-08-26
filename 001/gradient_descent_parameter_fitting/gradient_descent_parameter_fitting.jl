alpha = 0.001
delta = 0.01
num_iterations = 10000
points = [[0, 0], [1, 1], [2, 4]]

function rss(b_0, b_1)
    rss = 0
    for point in points
        rss += (b_0 + b_1 * point[1] - point[2]) ^ 2
    end
    return rss
end

function gradient_descent_parameter_fitting(starting_point)
    b_0, b_1 = starting_point
    for _ in 1:num_iterations
        b_0 -= alpha * (rss(b_0 + delta, b_1) - rss(b_0 - delta, b_1)) / (2 * delta)
        b_1 -= alpha * (rss(b_0, b_1 + delta) - rss(b_0, b_1 - delta)) / (2 * delta)
    end
end

start_time = time_ns()

for _ in 1:10
    gradient_descent_parameter_fitting([0, 2])
end

end_time = time_ns()

print((end_time - start_time) / 10^10)