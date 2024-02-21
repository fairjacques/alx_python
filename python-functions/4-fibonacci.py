def fibonacci_sequence(n):
    if n <= 2:
        return [0, 1][:n]
    fib_seq = fibonacci_sequence(n - 1)
    fib_seq.append(sum(fib_seq[-2:]))
    return fib_seq

print:fibonacci_sequence(6)
print:fibonacci_sequence(1)
print:fibonacci_sequence(0)
print:fibonacci_sequence(20)
