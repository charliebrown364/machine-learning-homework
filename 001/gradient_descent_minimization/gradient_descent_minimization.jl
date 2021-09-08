

function f(x, y)
    return 1 + 2*x^2 + 3*y^2
end

function new_x(x, y, alpha, delta)
    central_diff_quotient = (f(x + delta / 2, y) - f(x - delta / 2, y)) / delta
    return x - alpha * central_diff_quotient
end

function new_y(x, y, alpha, delta)
    central_diff_quotient = (f(x, y + delta / 2) - f(x, y - delta / 2)) / delta
    return x - alpha * central_diff_quotient
end

function gradient_descent_minimization(n, starting_point, num_updates, alpha, delta)
    
    x, y = starting_point
    for i in 1:num_updates
        x = new_x(x, y, alpha, delta)
        y = new_y(x, y, alpha, delta)
        if n == 1 && i < 2
            println("iteration: (x, y) =", (x, y))
        end
    end

end

start_time = time_ns()

for n in 1:10
    gradient_descent_minimization(n, [1, 2], 2, 0.001, 0.01)
end

end_time = time_ns()

println("Julia : ", (end_time - start_time) / 10^10)