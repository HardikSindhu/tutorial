class Fibonacci:
    def __init__(self, n):
        self.n = n

    def generate(self):
        sequence = [0, 1]
        while len(sequence) <= self.n:
            sequence.append(sequence[-1] + sequence[-2])
        return sequence
n = int(input("Enter a number: "))
fib = Fibonacci(n)
print("The Fibonacci sequence up to", n, "is", fib.generate())
