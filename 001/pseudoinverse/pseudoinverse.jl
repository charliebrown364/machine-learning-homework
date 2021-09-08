


function best_fit_line()

    x = [0 1; 1 1; 2 1; 3 1]
    y = [0; 1; 4; 9]

    x_transpose = transpose(x)
    prev_times_x = x_transpose * x
    inverse_of_prev = inv(prev_times_x)
    
    
    return inverse_of_prev * x_transpose * y

end

start_time = time_ns()

for _ in 1:10
    best_fit_line()
end

end_time = time_ns()

println("Julia : ", (end_time - start_time) / 10^10, "")

# sh 001/pseudoinverse/pseudoinverse.sh