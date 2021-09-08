

function sum(n)
    total = 0
    for i in 1:n
        total += i
    end
    return total
end

start = time_ns()

for i in 1:10
    sum(10^6)
end

end_time = time_ns()

print("Julia : ", (end_time - start) / 10^10)